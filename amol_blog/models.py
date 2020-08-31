from django.db import models
from django.contrib.auth.models import User
import uuid


class Slideshow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=4000)
    short_desc = models.CharField(max_length=15000)
    long_dec = models.CharField(max_length=10485)
    photo = models.ImageField(upload_to='slideshow/', blank=True)
    date = models.DateField(auto_now_add=True)

class Latest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=40000)
    short_desc = models.CharField(max_length=15000)
    long_dec = models.CharField(max_length=10485)
    photo = models.ImageField(upload_to='burning/')
    date = models.DateField(auto_now_add=True)
    
class Comment(models.Model):
   id = models.UUIDField(default=uuid.uuid4, primary_key=True)
   created_at = models.DateTimeField(auto_now_add=True, null=True )
   name = models.CharField(max_length=2500)
   email = models.CharField(max_length=3000)
   comment = models.CharField(max_length=3000)
   post = models.ForeignKey(Slideshow, related_name="Slideshow", on_delete=models.CASCADE, null=True)
   post2 = models.ForeignKey(Latest, related_name="Latest", on_delete=models.CASCADE, null=True)

class Messages(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=35)
    msg = models.CharField(max_length=300)

class Subscribers(models.Model):
    email = models.CharField(max_length=50) 

class Profile_pic(models.Model):
    prof_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    pic = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=30, null=True)
    bio = models.CharField(max_length=50, null=True)



   
    
