from django.shortcuts import render,redirect
from .models import Meal
from django.views import generic
from .forms import Rating_form
from django.contrib.auth.models import User
# Create your views here.

class MealList(generic.ListView):
    model= Meal
    



class MealsDetail(generic.DetailView):
    model = Meal



def meal_rating(request,id):
    if request.method == 'POST':
        form=Rating_form(request.POST)
        print(request.user)
        meal=Meal.objects.get(id=id)
        print(meal)
        # #Get the data from html and Save it
        # if form.is_valid():
        #     user=User.objects.get(username=request.user)
        #     meal=Meal.objects.get(id=id)
        #     rate=3
        #     form.save()
        #     return redirect('/')
        # else:
        #     print('THERE IS A PROBLEM')
        
    else:
        form=Rating_form()
    return render(request,'meals/review.html',{'form':form})
        