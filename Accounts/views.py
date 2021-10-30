from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def approveEmp(req, email):
    print(email)
    subject = 'EtecCube Interns'
    message = 'Hey login in with this credintials/n profEmail: '+"@etchcube.com/n password: India@123"
    to = email
    send_mail(subject, message, settings.EMAIL_HOST_USER, to)
    return redirect('Admin')
    

def rejectEmp(req):
    subject = 'EtecCube Interns'
    message = "Your documents are not clear, please resend it!"
    to = [self.email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, to)
    return redirect('Admin')