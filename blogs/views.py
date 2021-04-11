from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .forms import CreateUserForm,Loginform
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.

def index(request):
    post=Post.objects.all()
    return render(request,'index.html',{'post':post})

def signup(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect("login")
    context={'form':form}
    return render(request,'signup.html',context)     


def login(request):
 if not request.user.is_authenticated:
    if request.method == 'POST':
        form=Loginform(request=request, data=request.POST)
        if form.is_valid():
         uname=form.cleaned_data['username']
         upass=form.cleaned_data['password']
        
         user=authenticate(username=uname,password=upass)
         request.session['user'] = user.id
         if user is not None:
             auth_login(request, user)
             return redirect("Blog")
    else:
       form=Loginform()
    context={'form':form}
    return render(request,'login.html',context)

 else:
     return redirect("Blog")


def Logout(request):
    request.session.clear()
    return redirect("login")




 
def blogdesc(request,id):

    pi=Post.objects.filter(pk=id)
    print(pi)

    return render(request,'blogdesc.html',{'pi':pi[0]})