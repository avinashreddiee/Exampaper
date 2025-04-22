"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    
    path('loginaction/', views.loginaction, name='loginaction'),
    
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    

    path('addstaff/', views.addstaff, name='addstaff'),
    path('addstaffaction/', views.addstaffaction, name='addstaffaction'),
    path('viewstaff/', views.viewstaff, name='viewstaff'),
    
    
    
    path('teachersignup/', views.teachersignup, name='teachersignup'),
    path('teachersignupaction/', views.teachersignupaction, name='teachersignupaction'),
    path('paper_request/',views.paper_request_def, name="paper_request"),
    
    
    path('shome/', views.shome, name='shome'),
    path('slogout/', views.slogout, name='slogout'),
    path('viewteachers/', views.viewteachers, name='viewteachers'), 
    path('viewpaperrequest/', views.viewpaperrequest, name='viewpaperrequest'), 
    path('aviewpaperrequests/', views.aviewpaperrequests, name='aviewpaperrequests'), 
    path('paperrequestcomplete/', views.paperrequestcomplete, name="paperrequestcomplete"),

    path('thome/', views.thome, name='thome'),
    path('tlogout/', views.tlogout, name='tlogout'),
    path('teacher_paper_reqs/', views.teacher_paper_reqs, name="teacher_paper_reqs"),
    
    path('uploadpaper/', views.uploadpaper, name="uploadpaper"),
    path('viewresponses/', views.viewresponses, name="viewresponses"),
    path('finalizepaper/', views.finalizepaper,name='finalizepaper'), 
    path('viewpdf/<str:op>/', views.viewpdf, name="viewpdf"),
    path('uploadipfs/', views.uploadipfs, name="uploadipfs"),
    path('downloadfromipfs/', views.downloadfromipfs, name='downloadfromipfs'),
    path('viewfile/', views.viewfile, name="viewfile"),

    path('view_paper/<str:paper>/', views.view_paper, name="view_paper"),
    path('rsignup/', views.rsignup, name="rsignup"),
    path('rsignupaction/', views.rsignupaction, name="rsignupaction"),
    path('viewpapers/', views.viewpapers, name="viewpapers"),

    path('rhome/', views.rhome, name='rhome'),
    path('rlogout/', views.rlogout, name='rlogout'),
    path('downloadfromipfs2/', views.downloadfromipfs2, name="downloadfromipfs2")
    

    
    

   
    
    

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)