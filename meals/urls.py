from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import MealList,MealsDetail


urlpatterns = [
    path('',MealList.as_view()),
    path('<slug:pk>', MealsDetail.as_view()),
]
