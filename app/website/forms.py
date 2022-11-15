from pydoc import describe
from secrets import choice
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from .models import *

#Personal_Experience


##PerExp



class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email' ,'password1', 'password2', 'groups']



class UserUpdateForm(forms.ModelForm):
    
   
    class Meta:
        model = User
        fields = ('username', 'email')  

class UserForm(ModelForm):  
    class Meta:
        model = User
        fields = ['username','email']    
            


class PerExpPostForm(forms.ModelForm):
    
    class Meta:
        model = Personal_Experience
        fields = ['user', 'competence', 'experience', 'description', 'main_job']

class PerExpGetForm(forms.ModelForm):
    class Meta:
        model =  Personal_Experience
        fields =  ['user', 'competence', 'experience', 'description', 'main_job']

class UserExForm(ModelForm):
    class Meta:
        model = Personal_Experience
        fields = ['experience','main_job']



class GetPostJobPageForm(forms.ModelForm):
    class Meta:
        model = PostJob
        fields = ['user','title', 'description','min_salary','max_salary','adress', 'location']

class PostPostJobPageForm(forms.ModelForm):
    class Meta:
        model = PostJob
        fields = ['title', 'description','adress','min_salary','max_salary', 'location']

class GetCategoryPageForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['user','name','description']



class PostCategoryPageForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']

        
