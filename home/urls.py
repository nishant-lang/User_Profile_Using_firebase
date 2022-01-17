from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('login',views.login,name="login"),
    path('logedin',views.logedin,name="logedin"),
    path('logout',views.logout,name="logout"),
    path('signup',views.signup,name="signup"),
    path('signedup',views.signedup,name="signedup"),
    path('reset/', views.reset,name="reset"),
    path('postReset/', views.postReset,name="postReset"),
   
]