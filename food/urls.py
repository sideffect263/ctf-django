from . import views
from django.urls import path , include
app_name = 'food'
urlpatterns = [
    path('',views.Index_Class_View.as_view(),name="index"),
    
    path('<int:pk>',views.food_class_detail.as_view(),name='detail'),
    
    path('item/',views.item,name = "item"),
    path('add/',views.Create_view_class.as_view(),name='create_item'),
    
    path('update/<int:id>',views.update_item,name='update_item'),
    path('delete/<int:id>',views.delete_item,name="delete_item"),
]
