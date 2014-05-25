from django.contrib import admin
from django.contrib.auth.models import User
from web.models import Student_member,Faculty_member,General_notice,Member_notice

# Register your models here.
class Student_user(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        name=obj.idn
        fname=obj.firstname
        lname=obj.lastname
        password=obj.password
        email=obj.email
        dob=obj.dob
        contact_no=obj.contact_no
        dept=obj.department
        doj=obj.doj
        u=User.objects.create(username=name,email=email,first_name=fname,last_name=lname)
        u.set_password(password)
        u.save()
        user=Student_member.objects.create(idn=name,firstname=fname,lastname=lname,email=email,dob=dob,doj=doj,contact_no=contact_no,department=dept)
        user.save()

class Faculty_user(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        name=obj.idn
        fname=obj.firstname
        lname=obj.lastname
        password=obj.password
        email=obj.email
        contact_no=obj.contact_no
        dept=obj.department
        doj=obj.doj
        u=User.objects.create(username=name,email=email,first_name=fname,last_name=lname)
        u.set_password(password)
        u.save()
        user=Faculty_member.objects.create(idn=name,firstname=fname,lastname=lname,email=email,doj=doj,contact_no=contact_no,department=dept)
        user.save()
        
admin.site.register(Student_member, Student_user)
admin.site.register(Faculty_member,Faculty_user)
admin.site.register(General_notice)
admin.site.register(Member_notice)
