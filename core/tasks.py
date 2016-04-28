from django.core.mail import get_connection, EmailMultiAlternatives
from celery import task
from django.conf import settings
from user.models import User
from django.db.models import Q
from academic.models import AcademicDetail, Interested
def get_registration_mail_body(user_list):
    print('users', user_list)
    message_list = []
    email_subject = "Complete Your Registration"
    for user in user_list:
        print("user", user)
        # try:
        #unique_code = UniqueRegistration.objects.get(student=student)
        # except:
        #     unique_code = UniqueRegistration(user=student, valid_to=datetime.now()+timedelta(hours=24*7))
        #     unique_code.save()
        link = "<a href='http://127.0.0.1:8000/user/registration/{}'>click here</a>".format(user['id'])
        html_message = "<h1>Hello {}</h1>For registration {}".format(user['first_name'], link)
        email = user['email']
        message = EmailMultiAlternatives(email_subject, '', None, [email])
        message.attach_alternative(html_message, 'text/html')
        message_list.append(message)
    return message_list

def get_placement_notification_mail_body(user_list, campus_drive):
    message_list = []
    email_subject = "About Placement Notification"
    for user in user_list:
        print("user", user)
        # try:
        #unique_code = UniqueRegistration.objects.get(student=student)
        # except:
        #     unique_code = UniqueRegistration(user=student, valid_to=datetime.now()+timedelta(hours=24*7))
        #     unique_code.save()
        link = "For confirm Joining <a href='http://127.0.0.1:8000/user/registration/{}'>click here</a>".format(user.id)
        html_message = "<h1>Hello {}</h1> you are placed in  {}. If you want to join the company then visit link below. {}".format(user.first_name,campus_drive['company_name'], link)
        email = user.email
        message = EmailMultiAlternatives(email_subject, '', None, [email])
        message.attach_alternative(html_message, 'text/html')
        message_list.append(message)
    return message_list


def get_campus_drive_notification_mail_body(student_list, campus_drive):
    message_list = []
    email_subject = "Placement Drive Notification"
    for student in student_list:
        print("user", student)
        Interested(campus_drive=campus_drive, student=student).save()
        #Interested(campus_drive=campus_drive, student=student).save()
        # try:
        #unique_code = UniqueRegistration.objects.get(student=student)
        # except:
        #     unique_code = UniqueRegistration(user=student, valid_to=datetime.now()+timedelta(hours=24*7))
        #     unique_code.save()
        link = "<a href='http://127.0.0.1:8000/student/placement/campusdrive_interest/{}/{}'>click here</a>".format(student.id,campus_drive.id)
        html_message = "<h1>Hello {}</h1><strong>{}</strong> is coming for campus drive. To show your interest to attend the drive please visit this link  {}. If not just ignore".format(student.first_name, campus_drive.company_name,link)
        email = student.email
        message = EmailMultiAlternatives(email_subject, '', None, [email])
        message.attach_alternative(html_message, 'text/html')
        message_list.append(message)
    return message_list

def get_coursewise_studentlist(campus_drive):
    pg_course_mapping = {'MCA':'MCA', 'MSc(Computer Science)':'MSc(Computer Science)', 'PG':['MCA', 'MSc(Computer Science)']}
    ug_course_mapping = {'UG': ['be','bca', 'Bsc(Computer Science)'], "UG Except BE/B.Tech": ['bca', 'Bsc(Computer Science)'], 'BE/B.Tech': 'be'}
    ug_course_list = []
    pg_course_list = []
    print(campus_drive.course_list)
    for course in campus_drive.course_list:
        ug_course = ug_course_mapping.get(course, None)
        pg_course = pg_course_mapping.get(course, None)
        if ug_course:
            ug_course_list = ug_course_list + ug_course if type(ug_course) is list  else ug_course_list.append(ug_course)
        if pg_course:
            pg_course_list = pg_course_list + pg_course if type(pg_course) is  list else pg_course_list.append(pg_course)

    print(ug_course_list, pg_course_list)
    academic_details = AcademicDetail.objects.filter(Q(ug_course__in=ug_course_list)| Q(pg_course__in=pg_course_list))
    print(academic_details)
    result_queryset = AcademicDetail.objects.none()
    if ug_course_list:
        result_queryset = result_queryset | academic_details.filter(ug_course__in=ug_course_list, ug_passout_year__in=campus_drive.batch_year)
    if pg_course_list:
        result_queryset = result_queryset | academic_details.filter(pg_course__in=pg_course_list, pg_passout_year__in=campus_drive.batch_year)
    # if 'be' in ug_course_list:
    #     be_academic_detail = academic_details.filter(current_ug_sem__in=[7,8])
    #     result_queryset = result_queryset | be_academic_detail
    # if 'Bsc(Computer Science)' in ug_course_list or 'bca' in ug_course_list:
    #     bsc_academic_detail = academic_details.filter(current_ug_sem__in=[5,6])
    #     result_queryset = result_queryset | bsc_academic_detail
    # if 'MSc(Computer Science)' in pg_course_list:
    #     msc_academic_detail = academic_details.filter(current_pg_sem__in=[3,4])
    #     result_queryset = result_queryset | msc_academic_detail
    # if 'mca' in pg_course_list:
    #     mca_academic_detail = academic_details.filter(current_pg_sem__in=[5,6])
    #     result_queryset = result_queryset | mca_academic_detail
    return  result_queryset


def get_eligible_student_and_send_mail(campus_drive):


    academic_details = get_coursewise_studentlist(campus_drive)
    if academic_details:
        students = [academic_detail.student for academic_detail in academic_details]
        print("final", students)
        send_mail(students, "campus_drive", campus_drive)
    #students = [student in ]
    # if campus_drive.criteria_type == 'both':
    #     special_criterias = SpecialCriteria.objects.filter(campus_drive=campus_drive)
    #     for special_criteria in special_criterias:
    #         special_criteria_for

    # print(academic_details)
    #

    #students = AcademicDetail.objects.select_related()

@task
def send_mail(user_list, email_type, campus_drive=None):

    connection = get_connection(
        username=settings.EMAIL_HOST_USER, password=settings.EMAIL_HOST_PASSWORD, fail_silently=False)
    if email_type=='registration':
        message_list = get_registration_mail_body(user_list)
    if email_type=="campus_drive":
        message_list = get_campus_drive_notification_mail_body(user_list, campus_drive)
    if email_type=="placement":
        message_list = get_placement_notification_mail_body(user_list, campus_drive)

    response = connection.send_messages(message_list)
