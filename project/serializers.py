
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_name','task_description','status','created_at','updated_at']

class ProjectSerializer(serializers.ModelSerializer):

	tasks = TaskSerializer(many=True, read_only=True)

	class Meta:
		model = Project
		fields = ['id','user','project_name','description','slug','start_date','end_date','created_at','updated_at','tasks']
