from . import views
from django.urls import path , include
app_name = 'shop'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('shop/checkout/',views.checkout,name="checkout"),
]