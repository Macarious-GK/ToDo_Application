from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category_task(models.Model):
    Name = models.CharField(max_length=255)
    Creation_day = models.DateField(auto_now=True)
    Cat_Author = models.ForeignKey(User,on_delete=models.CASCADE)
    PRIORITY_CHOICES = [(i, str(i)) for i in range(1, 11)] 
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    def __str__(self):
        return self.Name
    



class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Category = models.ForeignKey(Category_task,on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Creation_day = models.DateField(auto_now=True)
    deadline = models.DateTimeField()
    discrption = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.Name