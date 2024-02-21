from django.contrib import admin
from django.urls import path
from sytemApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexPage,name="index"),
    path('signup',views.SignupPage,name="signup"),
    path('dashboard/',views.Dashboard,name="dashboard"),
    path('single/', views.SinglePage, name="single"),
    path('login/',views.LoginPage,name="login"),
    path('home/',views.HomePage,name="home"),
    path('home/homenxt/',views.HomeNext,name="homenxt"),
    path('home/index/',views.LogoutPage,name="index"),
    path('index/',views.IndexPage,name="index"),
    path('index/signup',views.SignupPage,name="signup"),
    path('index/login/',views.LoginPage,name="login"),
    path('homenxt/',views.HomeNext,name="homenxt"),
    path('home/homenxt/single/', views.SinglePage, name="single"),
    path('dashboard/index', views.IndexPage, name="index"),
    path('group', views.GroupPage, name="group"),
    path('home/homenxt/group/', views.GroupPage, name="group"),
    path('home/homenxt/group/dashboard01', views.Dashboard01, name="dashboard01"),
    path('dashboard01', views.Dashboard01, name="dashboard01"),
    
]