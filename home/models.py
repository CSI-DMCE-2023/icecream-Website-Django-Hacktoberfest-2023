
from django.db import models


# Create your models here.
#makemigrations= create changes and store it in file_
#migrate= apply pending changes created by makemigrations

class user(models.Model):
    fname=models.CharField(max_length=20,default=20 )
    lname=models.CharField(max_length=20,default=20 )
    username=models.CharField(max_length=20,default=20 )
    email=models.CharField(max_length=100,default=20 )
    password=models.CharField(max_length=50,default=20 )
    accountcreated=models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name =models.CharField(max_length=20,default=20 )
    email =models.CharField(max_length=202,default=20)
    phone =models.CharField(max_length=20,default=20)
    desc =models.TextField(max_length=200,default=20)
    date =models.DateField()


class login(models.Model):
    username=models.CharField(max_length=20,default=20 )
    lastlogin=models.DateTimeField(auto_now=True)
    
class comments(models.Model):
    fname=models.CharField(max_length=20,default=20 )
    lname=models.CharField(max_length=20,default=20 )
    username=models.CharField(max_length=20,default=20 )
    city=models.CharField(max_length=100,default=20 )
    state=models.CharField(max_length=50,default=20 )
    zip=models.CharField(max_length=50,default=20 )
    gender=models.CharField(max_length=50,default=20 )
    comments=models.CharField(max_length=100,default=20 )
    commenttime=models.DateTimeField(auto_now_add=True)
    
class cartitem(models.Model):
    username=models.CharField(max_length=20,default=20 )
    item=models.CharField(max_length=20,default=20 )
    noofitem=models.IntegerField(default=0)
    itemrate=models.IntegerField(default=0)
    
    
    
    
    