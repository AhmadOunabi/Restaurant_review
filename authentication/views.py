from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignupForm,UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.



def user_signup(request):
    if request.method =='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            form.save()
        redirect('/created')
            
    else:
        form=SignupForm()
    return render (request,'registration/signup.html',{'form':form})



@login_required
def user_profile(request):
    user_data=User.objects.filter(username=request.user)
    return render(request,'registration/profile.html',{'user_data':user_data})






def user_created(request):
    
    return render(request,'registration/user_created.html')