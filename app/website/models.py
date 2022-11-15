from email.mime import image
from enum import unique
from tabnanny import verbose
from django.conf import settings
from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
#import helpers      

from django.contrib.auth.models import AbstractUser





class Competence(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name 


class Personal_Experience(models.Model):
    JOBS_CHOICES = (
            ('Paint','Paint'),
            ('Electricity','Electricity'),
            ('Plumbing','Plumbing'),
            ('Masonry','Masonry'),
            ('Industriel automation', 'Industriel automation'),
            ('Web developer','Web developer'),
            ('truck driver','truck driver'),
    )
    user = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE)
    competence = models.ManyToManyField(Competence, null=True, blank=True)
    experience =  models.TextField(default=None, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)
    main_job = models.CharField(max_length=100, null=True,blank=True, default=None,choices=JOBS_CHOICES)
  
    
    def __str__(self):
        return self.user.username


class PostJob(models.Model):
    user = models.ForeignKey(User, related_name='post',on_delete=models.CASCADE, blank=True, null=True)
    adress = models.EmailField(max_length=254,blank=True, null=True )
    title = models.CharField(max_length=100)
    description = models.TextField(default=None, null=True, blank=True)
    min_salary = models.FloatField(default=None, null=True, blank=True)
    max_salary = models.FloatField(default=None, null=True, blank=True)
    location = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return self.title




class Qualification(models.Model):
    job_id = models.IntegerField() 
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name




class UserProfile(models.Model):
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default="")
    image = models.ImageField(default='website/profile1.jpg', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Category(models.Model):
       
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="category")
    name = models.CharField(max_length=100, null=False, blank=False)
   # image = models.ImageField(null=True, blank=False, upload_to="static/img")
    description = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name 
 





        
        



'''

class Post(models.Model):30
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True,upload_to = None)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255 ,default='coding')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User,null=True, blank=True, default=None)
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + ' ' + str(self.author) 
    def get_absolute_url(self):
        return reverse('home') 
           


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='post_  comments', on_delete=models.CASCADE)      
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % (self.post.title,self.name) 

'''


class MultipleImage(models.Model):
    images = models.FileField()






  

  





 





