from django.urls import path 
from .views import *
from . import views

urlpatterns = [
    path('',home,name = 'hometodo'),
    path('task-details/<int:pk>/',Get_Task,name='details'),
    path('delete/<int:pk>/',delete_Task,name='delete'),
    path('task-update/<int:pk>/',update_Task.as_view(),name='Update'),
    path('done-task/<int:pk>/',done_Task,name='done'),

    path('create-category/',Category_taskCreateView.as_view(), name = "create_category"),
    path('delete-category/<int:pk>/',Category_taskDeleteTask.as_view(),name='delete_category'),
    path('Done-category-tasks/<int:pk>/',Done_category_Tasks,name='all_category_done'),
    path('Un-Do-category-tasks/<int:pk>/',Un_Done_category_Tasks,name='all_category_undo'),



    
    path('update-category/<int:pk>/',update_Category.as_view(),name='update_category'),
    path('create-task/',TaskCreateView.as_view(), name='create_Task'),
    path('list-tasks/<int:pk>/',TasksListView.as_view(),name='List-tasks'),
]