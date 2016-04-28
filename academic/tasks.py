#from celary import task
from user.models import User
#@task
def get_eligible_student_and_send_mail(campus_drive):
    print("hiii", campus_drive)
    special_criteria_list = SpecialCriteria.objects.filter(campus_drive=campus_drive)
    academic_details = AcademicDetail.objects.filter(hsc_percentage__gte=campus_drive.throughout, ssc_percentage__gte=campus_drive.throughout, ug_percentage__gte=campus_drive.throughout, exprience__gte=campus_drive.exprience, no_of_gap__lte=campus_drive.no_of_gap).select_related()
