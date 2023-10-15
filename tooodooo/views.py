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
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required



@login_required()

def Get_all_Tasks(request):
    user = request.user
    task_objs = Tasks.objects.filter(user = user)
    return render(request,'task_List.html',{'tasks':task_objs})

@login_required()

def Get_Task(request, pk):
    task_obj = Tasks.objects.get(pk = pk)
    return render(request, 'task_details.html',{'task':task_obj})



@login_required()

def create_Task(request):
    if request.method == 'POST':
        user = request.user
        taskname = request.POST['taskname']
        task_deadline = request.POST['deadline']
        task_discrption = request.POST['discrption']


        create_task = Tasks.objects.create(user = user,
            Name = taskname,
            deadline = task_deadline,
            discrption= task_discrption,)
        create_task.save()
        return redirect('view')
    return render(request,'create_task_page.html')

class update_Task(UpdateView):
    model =Tasks
    fields = ['Name','deadline','discrption','completed']
    template_name = 'task_update.html'
    success_url = reverse_lazy('view')
    
@login_required()

def delete_Task(request,pk):
    task_objs = Tasks.objects.get(pk = pk)
    task_objs.delete()
    return redirect('view')

@login_required()

def done_Task(request,pk):
    task_obj = Tasks.objects.get(pk = pk)
    task_obj.completed = True
    task_obj.save()
    return redirect('view')


@login_required()

def home(request):
    return render(request,'Welcome_Base_Todo.html')

