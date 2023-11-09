from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy

from .serializer import *
from .models import *

from rest_framework import status, viewsets, generics
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth.models import User,Group
from django.core.paginator import EmptyPage, Paginator

from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse



class Category_taskCreateView(LoginRequiredMixin,CreateView):
    model = Category_task
    fields = ['Name','priority']
    template_name = 'Category_taskCreate_form.html'
    success_url = reverse_lazy('hometodo')
    def form_valid(self, form):
        form.instance.Cat_Author = self.request.user
        return super().form_valid(form)

class Category_taskDeleteTask(LoginRequiredMixin,DeleteView):
    model = Category_task
    template_name = 'category_task_confirm_delete.html'
    context_object_name  ='category'
    success_url = reverse_lazy('hometodo')

class update_Category(LoginRequiredMixin,UpdateView):
    model = Category_task
    fields = ["Name",'priority']
    template_name = 'Category_update.html'
    success_url = reverse_lazy('hometodo')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = ['Name', 'Category', 'deadline', 'discrption']
    template_name = 'create_task_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.completed = False
        return super().form_valid(form)
    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        form.fields['Category'].queryset = Category_task.objects.filter(Cat_Author=self.request.user)
        return form
    def get_success_url(self):
        category_id = self.object.Category.pk
        return reverse('List-tasks', kwargs={'pk': category_id})


class TasksListView(LoginRequiredMixin,ListView):
    model = Tasks
    template_name = 'task_List.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        category = Category_task.objects.get(pk=self.kwargs['pk'])
        return Tasks.objects.filter(Category = category)


class update_Task(LoginRequiredMixin,UpdateView):
    model =Tasks
    fields = ['Name','Category','deadline','discrption','completed']
    template_name = 'task_update.html'
    def get_success_url(self):
        category_id = self.object.Category.pk
        return reverse('List-tasks', kwargs={'pk': category_id})
    

# ------------------------------------------------





@login_required()

def Get_Task(request, pk):
    task_obj = Tasks.objects.get(pk = pk)
    return render(request, 'task_details.html',{'task':task_obj})

    
@login_required()
def delete_Task(request,pk):
    task_objs = Tasks.objects.get(pk = pk)
    task_objs.delete()
    pkk = task_objs.Category.pk
    list_tasks_url = reverse('List-tasks', kwargs={'pk': pkk})
    return redirect(list_tasks_url)

@login_required()
def done_Task(request,pk):
    task_obj = Tasks.objects.get(pk = pk)
    task_obj.completed = True
    task_obj.save()
    pkk = task_obj.Category.pk
    list_tasks_url = reverse('List-tasks', kwargs={'pk': pkk})
    return redirect(list_tasks_url)


@login_required() 
def home(request):
    user = request.user
    Categorys = Category_task.objects.filter(Cat_Author = user).order_by('-priority')
    return render(request,'Welcome_Base_Todo.html',{"category":Categorys})


@login_required()
def Done_category_Tasks(request,pk):
    Categorys = Category_task.objects.get(pk = pk)
    tasks = Tasks.objects.filter(Category = Categorys)
    for task in tasks:
        task.completed = True
        task.save()
    list_tasks_url = reverse('List-tasks', kwargs={'pk': pk})
    return redirect(list_tasks_url)

@login_required()
def Un_Done_category_Tasks(request,pk):
    Categorys = Category_task.objects.get(pk = pk)
    tasks = Tasks.objects.filter(Category = Categorys)
    for task in tasks:
        task.completed = False
        task.save()
    list_tasks_url = reverse('List-tasks', kwargs={'pk': pk})
    return redirect(list_tasks_url)

@login_required()
def all(request):
    user = request.user
    tasks = Tasks.objects.filter(user = user)
    Category = Category_task.objects.filter(Cat_Author =user).order_by('priority')
    return render(request, 'tasks_list_all_categorys.html',{'tasks':tasks,'Category':Category})

 