from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('level1/',views.level1_view,name="level1"),
    
    path('level2/',views.level2_view,name="level2"),
    path('level21/',views.level21_view,name="level21"),
    path('level22/',views.level22_view,name="level22"),

    path('level3/',views.level3_view,name="level3"),
    path('level31/',views.level31_view,name="level31"),
    
    path('level4/',views.level4_view,name="level4"),

    path("signup/", SignUpView.as_view(), name="signup"),

  
]

