from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import escape


# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, default="")
    middleName = models.CharField(max_length=50, default="")
    lastName = models.CharField(max_length=50, default="")
    mobile1 = models.IntegerField( default="")
    mobile2 = models.IntegerField( default="")
    email = models.CharField(max_length=30, default="")
    gender = models.CharField(max_length=10, default="")
    age = models.IntegerField(default="")
    dateOfBirth = models.DateField()
    address = models.CharField(max_length=100, default="")
    joinDate = models.DateField()
    lastUpdated = models.DateField()
    adharCard = models.ImageField(upload_to="accounts/images", default="")
    panCard = models.ImageField(upload_to="accounts/images", default="")
    tenthResult = models.ImageField(upload_to="accounts/images", default="")
    twelthResult = models.ImageField(upload_to="accounts/images", default="")
    offerLetter = models.ImageField(upload_to="accounts/images", default="")
    workingLoc = models.CharField(max_length=30, default="")
    salary = models.IntegerField( default="")
    device = models.CharField(max_length=30, default="")
    maratialStatus = models.CharField(max_length=30, default="")
    department= models.CharField(max_length=30, default="")
    def image_tag(self):
        return u'<img src="%s" />'
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    def save(self, *args, **kwargs):
        subject = 'EtecCube Interns'
        message = 'Hey login in with this credintials/n profEmail: '+self.firstName+"@etchcube.com/n password: India@123"
        to = [self.email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, to)
        super(Employee, self).save(*args, **kwargs)
    # def __str__(self):
    #     return self.name+" - Rs: "+str(self.salary)


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

class login(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    userName =  models.CharField(max_length=50, default="")
    userPassword = models.CharField(max_length=50, default="")

class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    module = models.CharField(max_length=30, default="")
    name =  models.CharField(max_length=50, default="")

 

