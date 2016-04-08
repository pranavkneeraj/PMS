from user.models import User, UniqueRegistration
from datetime import datetime
from datetime import timedelta
from django.core.mail import get_connection, EmailMultiAlternatives
from django.conf import settings
def send_mail(email_list):
    email_subject = "Complete Your Registration"
    message_list = []
    connection = get_connection(
                username=settings.EMAIL_HOST_USER, password=settings.EMAIL_HOST_PASSWORD, fail_silently=False)
    for email in email_list:
        print("inside for")
        student = User.objects.get(email=email)
        print("user", student)
        try:
            unique_code = UniqueRegistration.objects.get(student=student)
        except:
            unique_code = UniqueRegistration(user=student, valid_to=datetime.now()+timedelta(hours=24*7))
            unique_code.save()
        link = "<a href='http://127.0.0.1:8000/user/registration/{}'>click here</a>".format(unique_code.code)
        html_message = "<h1>Hello {}</h1>For registration {}".format(student.first_name,link)
        message = EmailMultiAlternatives(email_subject, '', None, [email])
        message.attach_alternative(html_message, 'text/html')
        message_list.append(message)
    response = connection.send_messages(message_list)
