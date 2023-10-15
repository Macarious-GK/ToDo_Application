from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    discrption = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.Name