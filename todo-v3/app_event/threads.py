import threading
from django.conf import settings
from django.core.mail import send_mail


class send_invite_email(threading.Thread):
    def __init__(self, name, email, event_id):
        self.name = name
        self.email = email
        self.event_id = event_id
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Invitation Email"
            message = f"{self.name} has invited you to collabrate.\nFollow the link to join event.\nhttp://127.0.0.1:8000/invite/{self.event_id}/"
            email_from = settings.EMAIL_HOST_USER
            print("Email send started")
            send_mail(subject , message ,email_from ,[self.email])
            print("Email send finished")
        except Exception as e:
            print(e)


class invite_accepted(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Event invite accepted"
            message = f"The email id {self.email} has accepted event invite"
            email_from = settings.EMAIL_HOST_USER
            print("Email send started")
            send_mail(subject , message ,email_from ,[self.email])
            print("Email send finished")
        except Exception as e:
            print(e)



class invite_rejected(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Event invite denied"
            message = f"The email id {self.email} has rejected event invite"
            email_from = settings.EMAIL_HOST_USER
            print("Email send started")
            send_mail(subject , message ,email_from ,[self.email])
            print("Email send finished")
        except Exception as e:
            print(e)