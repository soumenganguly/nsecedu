from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.

class Login(forms.Form):
    username=forms.IntegerField()
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)

class General_notice(models.Model):
    headline=models.CharField(max_length=100)
    details=models.TextField(max_length=1200)
    files=models.FileField(upload_to='files',null=True)
    date=models.DateField()
    def __unicode__(self):
        return self.headline

class Member_notice(models.Model):
    headline=models.CharField(max_length=100)
    details=models.TextField(max_length=1200)
    files=models.FileField(upload_to='files',null=True)
    date=models.DateField()
    def __unicode__(self):
        return self.headline

class Student_member(models.Model):
    CHOICES=(('AEIE','AEIE'),('BME','BME'),('CSE','CSE'),('ECE','ECE'),('EE','EE'),('CE','CE'),('ME','ME'),('IT','IT'),('BCA','BCA'),('BBA','BBA'),('MBA','MBA'),('MTECH','MTECH'))
    idn=models.IntegerField()
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    password=models.CharField(max_length=100)
    dob=models.DateField()
    email=models.EmailField()
    contact_no=models.IntegerField()
    department=models.CharField(max_length=100,choices=CHOICES)
    doj=models.DateField()
    def __unicode__(self):
        return self.firstname

class Faculty_member(models.Model):
    CHOICES=(('ENGINEERING','ENGINEERING'),('MANAGEMENT','MANAGEMENT'))
    idn=models.IntegerField()
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    contact_no=models.IntegerField()
    department=models.CharField(max_length=100,choices=CHOICES)
    doj=models.DateField()
    def __unicode__(self):
        return self.firstname
    
class Search(forms.Form):
    CHOICES=(('FACULTY','faculty'),('STUDENT','student'))
    searchtext=forms.CharField(max_length=30)
    group=forms.ChoiceField(choices=CHOICES)

class File(forms.Form):
    text=forms.CharField(max_length=100)
    files=forms.FileField()

class FileUpload(models.Model):
    user_id=models.IntegerField()
    text=models.CharField(max_length=100,help_text="Please upload PDF files only")
    files=models.FileField(upload_to='files')

class Post(forms.Form):
    post=forms.CharField(max_length=1200,widget=forms.Textarea)
    date=forms.DateField()

class PostUpload(models.Model):
    user_id=models.IntegerField()
    post=models.CharField(max_length=1200)
    date=models.DateField()
