# from calendar import c
# from pyexpat import model
# from multiprocessing import context
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from pydoc import describe
# from tkinter.tix import Form
# from urllib import response
# from django.urls import reverse_lazy
# from xml.etree.ElementTree import Comment
import io
from os import ctermid
import profile
from unicodedata import category
from django.db.models import Q
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.core.mail import send_mail

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import *
from .forms import *
from .filters import OrderFilter


# =========== HOME PAGE ===========

def home(request):
    offers = PostJob.objects.all().order_by('timestamp')
    

    if request.GET.get('q') != None :
        
        q = request.GET.get('q')

        offers = PostJob.objects.filter(
        Q(title__icontains=q) | 
        Q(location__icontains=q)
        )
        # offers1 = set(offers1).intersection(set(offers))
        # offers = list(offers1)
    
    offers_count = offers.count()
    form = GetPostJobPageForm(offers)
    
    context = {
        "jobs":form.data,
        "offers_count":offers_count
    }    
    return render(request, 'website/home.html', context=context)


def indexprofileView(request):

    if request.GET.get('q') != None :
            q = request.GET.get('q') 

            offers = PostJob.objects.filter(
                Q(title__icontains=q) | 
                Q(location__icontains=q)
        )

    elif request.user.groups.first().name == 'employer':
        offers = PostJob.objects.filter(user=request.user)
    else :
        offers = PostJob.objects.all()

        # offers1 = set(offers1).intersection(set(offers))
        # offers = list(offers1)
    offers_count = offers.count()
    form = GetPostJobPageForm(offers)
    
    context = {
            "jobs":form.data,
            "offers_count":offers_count,
            "current_user":request.user
    }  
    return render(request, 'website/home_user.html', context=context)




  


# =========== CONNECT VIEWS ===========
@csrf_exempt
def registerPage(request):
    
    
    form = CreateUserForm()
    if request.method == 'POST':
        post_form = CreateUserForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            username = post_form.cleaned_data.get('username')
            # set the username to the request session for the next registration step
            request.session["username"] = username    
            user_group = post_form.cleaned_data.get('groups')[0].name
            grp = Group.objects.get(name=user_group)
            user = User.objects.get(username=username)
            grp.user_set.add(user)
        
        
            messages.success(request, 'Account was created for ' + user.username)
            
            if user_group == "employee" : 
                return redirect('Personal_Experience')
            
            return redirect('login')

        else:

            messages.error(request, f'Account is not created successfuly, please try again ')

            return redirect('register')
            
    else:
        if request.user.is_authenticated:
            return redirect('login')

        else:
            groups = [{'name' : 'Candidate account Employee'  , 'home':1},{'name' : 'Recuiter account Employer', 'home':2}]

            context = {
                'form':form,
                'groups' : groups
                }
            return render(request, 'website/signup.html' ,context=context)


 # =========== PERSONAL EXPERIENCE REGISTRATION VIEWS ===========

def PerExpView(request):
    

    if request.method == "GET":
        # print('im here ')
        exp = Personal_Experience.objects.all()
        form = PerExpGetForm()
        context = {
            "form":form,
            "exp":exp
        }
        return render(request, 'website/perexp.html', context=context)

    if request.method == "POST":
    
        data = request.POST.copy()


        username = request.session["username"]
        print("username = ",username)
        user = User.objects.get(username=username)
        
        data.update({'user': user})
        
        print("data == ", data)
        form = PerExpPostForm(data)
        if form.is_valid():
            form.save()
            return redirect('login')    
        else:
            print('im here ', form.errors)
            exp = Personal_Experience.objects.all()
            form = PerExpGetForm()
            context = {
                "form":form,
                "exp":exp
            }
            return render (request, "website/perexp.html", context=context)

    # return redirect('login') 



 # =========== LOGIN VIEWS ===========
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home-user')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                    messages.info(request,'Username Or password is incorrect' )
                    context = {}
                    return render(request, 'website/login.html', context)
        return render(request, 'website/login.html')  



  # =========== USER PROFILE VIEWS ===========  
   	
@login_required
def userProfile(request):

    user = request.user
    group = user.groups.first().name
    
    if group =="employee" :
        if Personal_Experience.objects.filter(user=user).exists() : 
            per = Personal_Experience.objects.get(user=user)
            form = PerExpGetForm(per).data
    else :
        form = None 


   
    context = {
    "user_group" : group ,
    'user':user,
    'per':form
    
    }        
    return render(request, 'website/profile.html', context=context)




'''
def addproject(request):

    form = PostCategoryPageForm()
    cat = Category.objects.all()
    if request.method == 'POST':
        form = PostCategoryPageForm()
        data = request.POST.copy()
        print('data 1== \n',data)
        data.update({'user': request.user})
        print('data 2==',data)

        form = GetCategoryPageForm(data)
        if form.is_valid():
            print('in the save function')
            form.save(request.user)
            return redirect('user-profile')
        else:
            print('your form is"n valid', form.errors)    

    context = {
        'cats':cat,
        'form': form
    }

    return render(request, 'website/add_project.html', context)    

       


def viewProjectCategory(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "website/details_project.html", {'category':category})          

# @login_required(login_url='login')
# def gallery(request):
#     user = request.user
#     category = request.GET.get('category')
#     if category == None:
#         photos = Photo.objects.filter(category__user=user)
#     else:
#         photos = Photo.objects.filter(
#             category__name=category, category__user=user)

#     categories = Category.objects.filter(user=user)
#     context = {'categories': categories, 'photos': photos}
#     return render(request, 'website/user-profile.html', context)


# @login_required(login_url='login')
# def viewPhoto(request, pk):
#     photo = Photo.objects.get(id=pk)
#     return render(request, 'website/photo.html', {'photo': photo})




    
# @login_required(login_url='login')
# def addPhoto(request):
#     categories = Category.objects.all()
#     if request.method == 'POST':
#         data = request.POST
#         images = request.FILES.getlist('images')

#         if data['category'] != 'none':
#             category = Category.objects.get(id=data['category'])
#         elif data['category_new'] != '':
#                 category, created = Category.objects.get_or_create(
#                     name=data['category_new'])
#         else:
#             category = None

#         for image in images:   

#             photo = Photo.objects.create(
#                 category=category,
#                 description=data['description'],
#                 image=image,
#             )

#         return redirect('gallery')
#     context = {'categories': categories}   
#     return render(request, 'website/user-profile.html', context)     

    
  '''      

# =========== USER RECRITER VIEWS ===========  




#@login_required
#def userhomeView(request):
 #   user_group = []
  #  for group in request.user.groups.all():
   #     user_group.append(group.name)
    #print("user_group = ",user_group)
    #jobs = PostJob.objects.all()
    #form = GetPostJobPageForm(jobs)


    #context = {
    #    "user_group" : user_group,
     #   "jobs":form.data
    
   # }    
    #return render(request, 'website/user-home.html', context=context)



        



 # =========== LOGOUT VIEWS ===========

def logoutUser(request):
    logout(request)

    return redirect('home')




 # =========== UPDATE VIEWS ===========

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)


    if request.method == 'POST':
        

        form = UserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('user-profile')

    return render(request, 'website/update-user.html', {'form': form})



# =========== POST JOBS VIEWS ===========

def post_jobPage(request):
    form = PostPostJobPageForm()



    if request.method == "POST":
        form = PostPostJobPageForm()
        data = request.POST.copy()
        data.update({'user': request.user})

        
        form = GetPostJobPageForm(data)
        if form.is_valid():
            form.save(request.user)
            return redirect('home-user')
    context = {'form':form}

    return render(request, "website/post.html", context)




 # =========== Offers VIEWS ===========

def offersPage (request):

    offers1=None
    if request.GET.get('q') != None :
        
        q = request.GET.get('q')

        offers = PostJob.objects.filter(
            Q(title__icontains=q) | 
            Q(location__icontains=q)
        )
        
        offers1 = Personal_Experience.objects.filter(
            Q(main_job__icontains=q)
        )



    elif request.user.groups.first().name == 'employer':
        offers = PostJob.objects.filter(user=request.user)
    else :
        offers = PostJob.objects.all()
   
    

  
        # offers1 = set(offers1).intersection(set(offers))
        # offers = list(offers1)
    
    offers_count = offers.count()
    form = GetPostJobPageForm(offers)
    form1 = GetPostJobPageForm(offers1)
   
    

    context = {
        "jobs":form.data,
        "main_jobs":form1.data,

        "offers_count":offers_count,
        "current_user":request.user
    }  
    return render(request, 'website/offer.html', context=context)



def OfferdetailsView(request,pk):
    
    posts = PostJob.objects.get(pk=pk)
    form = GetPostJobPageForm(posts)
    print("###########")
    context = {
        "posts":form.data
    }
    

    return render(request, 'website/offer-page.html', context=context)





 # =========== CATEGORY VIEWS ===========

def Jobs_list_view(request):
    JOBS_CHOICES =['Paint','Electricity','Masonry','Plumbing','Industriel automation',
    'Web developer','truck driver']


    context={
        'main_job':JOBS_CHOICES
        
            }
    return render(request, 'website/jobs.html', context=context)  




 
def updateofferView(request, pk):
    offer = PostJob.objects.get(id=pk)
    form = PostPostJobPageForm(instance=offer)

    if request.method == "POST":
        form = PostPostJobPageForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('home-user')

    context = {'form': form}
    return render (request, 'website/update-offer.html', context)

def deleteofferView(request, pk):
    offer = PostJob.objects.get(id=pk)
    if request.method == "POST":
        offer.delete()
        return redirect('/')
    context = {'job':offer}
        

    return render (request, 'website/delete-offer.html', context)
    
    

     
'''
    if request.method == "POST":
        data = request.POST.copy()
        data.update({'user': request.user})


        form = PostPostJobPageForm(data)

        if form.is_valid():
            form.save()
    return render(request, "website/post.html", {})
'''
           



def all_category_personal_experience(request,job):
    all_category_personal_experience = Personal_Experience.objects.filter(main_job=job)
    form = PerExpGetForm(all_category_personal_experience)
  
    context={
        "all_category_personal_erxperience":form.data
    }

    return render(request, 'website/all_category_personal_experience.html', context=context)




def user_personal_experience(request,pk):
    # userpro = Personal_Experience.objects.get(pk=pk)
    user_personal_experience = Personal_Experience.objects.get(pk=pk)
    user_categories = Category.objects.filter(user=user_personal_experience.user)
    form = PerExpGetForm(user_personal_experience)
    
    
    context={
        "user_personal_experience":form.data,
        "user_categories":user_categories
    }        
    
    return render(request, 'website/user_personal_experience.html', context=context)   

'''
def searchViewPage(request,job):
    searching =  Personal_Experience.objects.filter(mai_job=job)  
    form = PerExpGetForm(searching)
    context = {
        "searching":form.data
    }  
    return render(request, 'website/search_job.html', context=context)



'''







 # =========== ABOUT VIEWS ===========


def about(request):
    return render(request,'website/about.html', {}) 




 # =========== CONTACT VIEWS ===========

def contact(request):

    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        #send an email 
        send_mail(
            subject, # subject
            message, # message
            email, # from email
            ['filmmachine@gisb.dz'], # to email 
        )
        return render(request, 'website/contact.html',{'subject':subject}) 

    else:

        return render(request, 'website/contact.html', {} ) 








    






