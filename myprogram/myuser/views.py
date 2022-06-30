from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as  authlogin,logout as authlogout
from trainee.models import *
from professor.models import *

# Create your views here.
def loginview(req):
    if (req.session.get('username') is None):
            if (req.method == 'GET'):
                return render(req, 'myuser/login.html')
            else:
                # check user cred in myuser
                if req.POST['usertype'] =='trainee':
                    alluser = trainee.objects.filter(username=req.POST['username'], password=req.POST['password'])
                else:
                    alluser = professor.objects.filter(username=req.POST['username'], password=req.POST['password'])

                # check user cred in authuser
                authuserobject = authenticate(username=req.POST['username'], password=req.POST['password'])

                if (len(alluser) > 0 and authuserobject is not None):
                    req.session['username'] = alluser[0].username
                    authlogin(req, authuserobject)
                    return render(req, 'myuser/home.html')
                else:
                    print('errrrro')
                    context = {}
                    context['error'] = 'error'
                    return render(req, 'myuser/login.html', context)
    else:
            return render(req, 'myuser/login.html')

def signupview(req):
    if req.method == 'GET':
        return render(req, 'myuser/signup.html')
    else:
        if req.POST['usertype'] == 'trainee':
            trainee.objects.create(username=req.POST['username'], email=req.POST['email'], password=req.POST['password'])
            User.objects.create_user(username=req.POST['username'], email=req.POST['email'], password=req.POST['password'], is_staff=True)
        else:
            professor.objects.create(username=req.POST['username'], email=req.POST['email'],password=req.POST['password'])
            User.objects.create_user(username=req.POST['username'], email=req.POST['email'], password=req.POST['password'], is_superuser=True, is_staff=True)
        return render(req,'myuser/home.html')

def homeview(req):
    if req.method == 'GET':
        return render(req, 'myuser/home.html')
    else:
        return render(req, 'myuser/home.html')

def accessusers(req):
    context={}
    context['prof']=professor.objects.all()
    context['train'] = trainee.objects.all()

    return render(req,'myuser/display.html',context)


def logout(req):
    if (req.session.get('username') is None and req.user.is_authenticated()):
        req.session.clear()
        authlogout(req,req.user)
    return render(req,'index.html')