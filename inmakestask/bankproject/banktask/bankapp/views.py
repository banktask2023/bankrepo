from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import Application
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['login']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"home.html")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if username=='':
            messages.info(request, "Fields cannot be Empty")
            return render(request,"register.html")
        elif password=='':
            messages.info(request, "Fields cannot be Empty")
            return render(request,"register.html")
        elif cpassword =='':
            messages.info(request, "Fields cannot be Empty")
            return render(request,"register.html")
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')

        return redirect('/')

    return render(request, "register.html")


def home(request):
    return render(request,"home.html")

def application(request):
    return render(request,"application.html")

def final(request):
   if request.method == 'POST':
       aname = request.POST['aname']
       adob = request.POST['adob']
       aage = request.POST['aage']
       if aname == '':
           messages.info(request, "Name field cannot be Empty")
           return render(request, "application.html")
       elif adob == '':
           messages.info(request, "DOB field cannot be Empty")
           return render(request, "application.html")
       elif aage == '':
           messages.info(request, "Age field cannot be Empty")
           return render(request, "application.html")
       appli=Application()
       appli.aname = request.POST.get('aname')
       appli.adob = request.POST.get('adob')
       appli.aage = request.POST.get('aage')
       appli.save()
       report_item = {'aname': aname, 'adob': adob, 'aage': aage}
       return render(request,"final.html",report_item)

def logout(request):
    auth.logout(request)
    return redirect('/')
