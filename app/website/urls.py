from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
   


    
    path('login', views.loginPage, name='login'),
    path('signup', views.registerPage, name='register'),
    path('perexp', views.PerExpView, name='Personal_Experience'),

    path('profile', views.userProfile, name="user-profile"),
    #path('add-project/', views.addproject, name='add_project'),
    #path('photo/<str:pk>', views.viewProjectCategory, name='photo'),


    path('home-user/', views.indexprofileView, name='home-user'),
    path('update-user/', views.updateUser, name="update-user"),
    path ('post/', views.post_jobPage, name ='post'),

    
    path('offers/', views.offersPage, name='offers'),
    path('offer-page/<int:pk>/', views.OfferdetailsView, name='offer_details'),

    path ('update-offer/<str:pk>', views.updateofferView, name ='update-offer'),
    path ('delete-offer/<str:pk>', views.deleteofferView, name ='delete-offer'),





    path('logout', views.logoutUser, name='logout'),

    




    #path('offer.html', views.offer, name='offer'),

    path('jobs/', views.Jobs_list_view, name='category'),
    path('jobs/<str:job>/all-personal-experience/', views.all_category_personal_experience, name='all_users'),
    path('user-personal-experience/<int:pk>/', views.user_personal_experience, name='users_personal_experience'),







    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    # path('add/', views.addPhoto, name="add"),
    # path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    # path('gallery/', views.gallery, name='gallery'),


    

    #path('user-home', views.userhomeView, name="user-home"),


  ] 


