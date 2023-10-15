from django.urls import path 
from .views import *
from . import views

urlpatterns = [
    path('',home,name = 'hometodo'),
    path('view/',Get_all_Tasks,name = 'view'),
    path('task-details/<int:pk>/',Get_Task,name='details'),
    path('create/',create_Task,name='create'),
    path('delete/<int:pk>/',delete_Task,name='delete'),
    path('task-update/<int:pk>/',update_Task.as_view(),name='Update'),
    path('done-task/<int:pk>/',done_Task,name='done')
    
]