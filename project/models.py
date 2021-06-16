# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User



STATUS = (('TODO' , 'TODO'),
		  ('WIP' , 'WIP'),
		  ('ONHOLD' , 'ONHOLD'),
		  ('DONE' , 'DONE')) 


class Project(models.Model):

	user = models.ForeignKey(User , on_delete=models.CASCADE)
	project_name = models.CharField(max_length=100)
	description = models.TextField(max_length=512)
	slug = models.SlugField(max_length=40)
	start_date = models.DateField()
	end_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.project_name


class Task(models.Model):

	project = models.ForeignKey(Project,related_name='tasks',on_delete=models.CASCADE)
	task_name = models.CharField(max_length=100)
	task_description = models.TextField(max_length=512)
	status = models.CharField(max_length=100 , choices=STATUS)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.task_name + ' - ' + self.project.project_name