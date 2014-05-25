from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from django.contrib.auth import authenticate,login,logout
from web.models import Login,General_notice,Member_notice,Search,FileUpload,File,Faculty_member,Student_member,Post,PostUpload
from django.http import Http404
from django.contrib.auth.models import User
from django.db import connection

con=connection.cursor()

# Create your views here.

def index(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template('web/index.html')
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def log(request):
    if request.method=='POST':
        template=loader.get_template('web/login.html')
        notice=Member_notice.objects.order_by('-date')[:4]
        gen_notice=General_notice.objects.order_by('-date')[:4]
        form=Login(request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            passw=form.cleaned_data['password']
            user=authenticate(username=uname,password=passw)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    '''t=loader.get_template('web/userhome.html')
                    context=RequestContext(request,{'user':user,'notice':notice,})
                    return HttpResponse(t.render(context)) '''
                    # return HttpResponseRedirect(reverse('profile',args=(user.username,)))
                    return redirect('home',user.id)
                   
                else:
                    return HttpResponse('<html><head><title>Netaji Subhash Engineering College</title></head><body>Your account has been deactivated</body></html>')
            else:
                invt=loader.get_template('web/invalid_login.html')
                context=RequestContext(request,{
                    'form':form,
                    'notice':gen_notice,
                })
                return HttpResponse(invt.render(context))
        else:
            template=loader.get_template("web/invalid_login.html")
            context=RequestContext(request,{
                'form':form,
                'notice':gen_notice,
                })
            return HttpResponse(template.render(context))
    else:
        template=loader.get_template('web/login.html')
        notice=Member_notice.objects.order_by('-date')[:4]
        gen_notice=General_notice.objects.order_by('-date')[:4]
        form=Login()
        context=RequestContext(request,{
            'form':form,
            'notice':gen_notice,
        })
        return HttpResponse(template.render(context))

def placements(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/placements.html")
    context=RequestContext(request,{
        'notice':notice,
        })
    return HttpResponse(template.render(context))


def home(request,user_id):
    user=User.objects.get(id=user_id)
    if user.is_authenticated:
        notice=Member_notice.objects.order_by('-date')[:4]
        template=loader.get_template("web/userhome.html")
        context=RequestContext(request,{
            'user':user,
            'notice':notice,
        })
        return HttpResponse(template.render(context))
    else:
        raise Http404
    

def dirdesk(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template('web/dirdesk.html')
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def dept(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template('web/departments.html')
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def facst(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template('web/faculty.html')
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def campusmap(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template('web/campusmap.html')
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def map(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template('web/map.html')
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def notice(request):
    if request.user.is_authenticated():
        allnotice=Member_notice.objects.all()
        notice=Member_notice.objects.order_by('-date')[:4]
        template=loader.get_template("web/noticeallmem.html")
        context=RequestContext(request,{
            'allnotice':allnotice,
            'notice':notice,
            })
        return HttpResponse(template.render(context))
    else:
        allnotice=General_notice.objects.all()
        notice=General_notice.objects.order_by('-date')[:4]
        template=loader.get_template("web/noticeall.html")
        context=RequestContext(request,{
            'notice':notice,
            'allnotice':allnotice,
        })
        return HttpResponse(template.render(context))

def logout_(request):
    template=loader.get_template("web/logout.html")
    logout(request)
    context=RequestContext(request,{})
    return HttpResponse(template.render(context))

def avenir(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/avenir.html")
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def avenir_images(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/avenir_images.html")
    context=RequestContext(request,{
        'notice':notice,
        })
    return HttpResponse(template.render(context))

def phoenix(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/phoenix.html")
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def nixal(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/nixal.html")
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def nixal_images(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/nixal_images.html")
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def reset_pass(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/resetpass.html")
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def forgot_pass(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/forgotpass.html")
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def search(request):
    template=loader.get_template("web/search.html")
    allnotice=Member_notice.objects.all()
    notice=Member_notice.objects.order_by('-date')[:4]
    if request.method=='POST':
        form=Search(request.POST)
        if form.is_valid():
            name=form.cleaned_data['searchtext']
            category=form.cleaned_data['group']
            if category=='FACULTY':                             #If the search is done on faculty.
                user=Faculty_member.objects.all().filter(firstname=name)
                context=RequestContext(request,{
                    'allnotice':allnotice,
                    'notice':notice,
                    'users':user,
                    'form':form,
                })
                return HttpResponse(template.render(context))
            else:                                     #If the search is done on the student.
                user=Student_member.objects.all().filter(firstname=name)
                context=RequestContext(request,{
                    'allnotice':allnotice,
                    'notice':notice,
                    'users':user,
                    'form':form,
                    })
                return HttpResponse(template.render(context))
        else:
            context=RequestContext(request,{
                'allnotice':allnotice,
                'notice':notice,
                'form':form,
                })
            return HttpResponse(template.render(context))
    else:
        form=Search()
        context=RequestContext(request,{
            'allnotice':allnotice,
            'notice':notice,
            'form':form,
        })
        return HttpResponse(template.render(context))
            
def aeie(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/aeie.html")
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def bme(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/bme.html")
    context=RequestContext(request,{'notice':notice,})
    return HttpResponse(template.render(context))

def ce(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/ce.html")
    context=RequestContext(request,{'notice':notice,})
    return HttpResponse(template.render(context))

def cse(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/cse.html")
    context=RequestContext(request,{'notice':notice,})
    return HttpResponse(template.render(context))

def ee(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/ee.html")
    context=RequestContext(request,{'notice':notice,})
    return HttpResponse(template.render(context))

def ece(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/ece.html")
    context=RequestContext(request,{'notice':notice,})
    return HttpResponse(template.render(context))

def it(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/it.html")
    context=RequestContext(request,{'notice':notice})
    return HttpResponse(template.render(context))

def me(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/me.html")
    context=RequestContext(request,{'notice':notice,})
    return HttpResponse(template.render(context))

def bba(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/bba.html")
    context=RequestContext(request,{'notice':notice,})
    return HttpResponse(template.render(context))

def mba(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/mba.html")
    context=RequestContext(request,{'notice':notice,})
    return HttpResponse(template.render(context))

def contact(request):
    notice=General_notice.objects.order_by('-date')[:4]
    template=loader.get_template("web/contact.html")
    context=RequestContext(request,{
        'notice':notice,
    })
    return HttpResponse(template.render(context))

def fileupload(request):
    template=loader.get_template("web/file.html")
    allnotice=Member_notice.objects.all()
    notice=Member_notice.objects.order_by('-date')[:4]
    if request.method=='POST':
        form=File(request.POST,request.FILES)
        if form.is_valid():
            #Do something with the file,store the file somewhere 
            text=form.cleaned_data['text']
            instance=FileUpload(user_id=request.user.username,text=text,files=request.FILES['files'])
            instance.save()
            files=FileUpload.objects.all().filter(user_id=request.user.username)
            context=RequestContext(request,{
                'allnotice':allnotice,
                'notice':notice,
                'files':files,
                'form':form,
                })
            return HttpResponse(template.render(context))
        else:
            return HttpResponse('<html><head><title></title><body>Not uploaded</body></html>')
    else:
        fileform=File()
        files=FileUpload.objects.all().filter(user_id=request.user.username)
        context=RequestContext(request,{
            'allnotice':allnotice,
            'notice':notice,
            'form':fileform,
            'files':files,
        })
        return HttpResponse(template.render(context))

def profiles(request,user_idn):
    template=loader.get_template("web/profile.html")
    notice=Member_notice.objects.order_by('-date')[:4]
    allnotice=Member_notice.objects.all()
    files=FileUpload.objects.all().filter(user_id=user_idn)
    student_user=Student_member.objects.filter(idn=user_idn)
    faculty_user=Faculty_member.objects.filter(idn=user_idn)
    posts=PostUpload.objects.all().filter(user_id=user_idn)
    user=request.user
    if len(student_user)==0:
        context=RequestContext(request,{
            'users':faculty_user,
            'files':files,
            'notice':notice,
            'allnotice':allnotice,
            'posts':posts,
            'user':user,
            })
    else:
        context=RequestContext(request,{
            'users':student_user,
            'files':files,
            'notice':notice,
            'allnotice':allnotice,
            'posts':posts,
            'user':user,
            })
    return HttpResponse(template.render(context))

def post(request):
    template=loader.get_template("web/post.html")
    notice=Member_notice.objects.order_by('-date')[:4]
    allnotice=Member_notice.objects.all()
    if request.method=='POST':
        form=Post(request.POST)
        if form.is_valid():
            post=form.cleaned_data['post']
            date=form.cleaned_data['date']
            instance=PostUpload(user_id=request.user.username,post=post,date=date)
            instance.save()
            posts=PostUpload.objects.all().filter(user_id=request.user.username)
            context=RequestContext(request,{
                'form':form,
                'notice':notice,
                'allnotice':allnotice,
                'posts':posts,
                })
        else:
            context=RequestContext(request,{
                'form':form,
                })
        return HttpResponse(template.render(context))
    else:
        form=Post()
        posts=PostUpload.objects.all().filter(user_id=request.user.username)
        context=RequestContext(request,{
            'posts':posts,
            'form':form,
            'notice':notice,
            'allnotice':allnotice,
            })
        return HttpResponse(template.render(context))

def remove_post(request,post_id):
    template=loader.get_template("web/post_remove.html")
    post=PostUpload.objects.get(id=post_id)
    post.delete()
    context=RequestContext(request,{})
    return HttpResponse(template.render(context))
    

