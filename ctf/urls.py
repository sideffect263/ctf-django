"""
URL configuration for ctf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import TemplateView
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from movies.views import Movie_view_set,Action_movie_view,Comedy_movie_view
from new_app import views
from ctf_app import views as home_use
router = routers.SimpleRouter()
router.register('movies',Movie_view_set)
router.register('action',Action_movie_view)
router.register('comedy',Comedy_movie_view)



urlpatterns = [
    #actual admin
    path('adminson/', admin.site.urls),

    
    path("", home_use.home_view, name="home"),
    
    path('ctf_app/',include('ctf_app.urls')),
    path('food/',include('food.urls')),
    
    path('register/',user_views.register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path('profile/',user_views.profilepage,name="profile"),
    
    path('movies/',include(router.urls)),
    
    path('movie_list/',views.movie_list,name="movie_list"),
    
    path('shop/',include('shop.urls')),
    
    #admin honeypot
    path('admin/', include('admin_honeypot.urls')),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

