import threading, uuid
from django.conf import settings
from django.core.mail import send_mail
from .models import *


class send_forgot_link(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        try:
            otp = uuid.uuid4()
            obj = UserModel.objects.get(email=self.email)
            obj.otp = otp
            obj.save()
            print(otp)
            subject = "OTP to change password"
            message = f"The OTP to change your account password\n {otp}"
            print("Email send started")
            send_mail(subject , message ,settings.EMAIL_HOST_USER ,[self.email])
            print("Email send finished")
        except Exception as e:
                print(e)