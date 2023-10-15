from rest_framework import serializers
from .models import *


class task_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'