from django.contrib import admin
from django.contrib.auth.models import User
from .models import * 
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)  
class UserModel(UserAdmin):
    list_display = ['username', 'user_type' , 'first_name' ,   'password' ,]




