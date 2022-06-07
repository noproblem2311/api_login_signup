from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')



class Category(models.Model):
    name: models.CharField(max_length=100, null=False, unique=True )


class Course(models.Model):
    subject: models.CharField(max_length=255, null=False)
    description: models.TextField(null=True, blank=True)
    created_date: models.DateTimeField(auto_now_add=True)
    updated_date: models.DateTimeField(auto_now=True)
    active: models.BooleanField(default=True) 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class Login(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    

class sign_up(models.Model):
    user_name: models.CharField(max_length=100, null=False)
    email = models.EmailField(blank=True)
    password: models.CharField(max_length=50, null=False)
    birthday: models.DateTimeField(auto_now_add=True)
    
    




