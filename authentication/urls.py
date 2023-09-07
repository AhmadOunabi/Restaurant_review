from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import user_created,user_signup,user_profile


urlpatterns = [
    path('signup', user_signup),
    path('profile', user_profile),
]
