

from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

# def index(request):
# 	latest_project_list = Project.objects.all()
# 	template = loader.get_template('project/index.html')
# 	context = {
# 	    'latest_project_list': latest_project_list,
# 	}
# 	return HttpResponse(template.render(context, request))


# def ProjectDetailView(request,pid):

# 	project_queryset = Project.objects.get(pk=pid)
# 	print(project_queryset)
# 	template = loader.get_template('project/detail.html')
# 	context = {
# 	    'project': project_queryset,
# 	}
# 	return HttpResponse(template.render(context, request))


class IndexView(generic.ListView):
    template_name = 'project/index.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Project.objects.all()


class DetailView(generic.DetailView):

	print("-=-=")

	model = Project
	template_name = 'project/detail.html'

class ProjectDetailView(DetailView):

	model = Project
	template_name = 'project/detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ProjectDeleteView(generic.DeleteView):
	model = Project
	success_url = reverse_lazy('project:detail')




# ============ DRF CODE ================ #


from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework import permissions, status, viewsets, views

class ProjectViewSet(viewsets.ViewSet):
	"""
	Example empty viewset demonstrating the standard
	actions that will be handled by a router class.

	If you're using format suffixes, make sure to also include
	the `format=None` keyword argument for each action.
	"""

	queryset = Project.objects.all()
	project_serializer_class = ProjectSerializer

	def get_project_object(self, pk):
		return Project.objects.get(pk=pk)

	def get_task_object(self, pk):
		return Task.objects.get(pk=pk)

	def list(self, request):
		queryset = Project.objects.all()
		serializer = ProjectSerializer(queryset, many=True)
		return Response(serializer.data)
		

	def create(self, request):

		project_serializer = self.project_serializer_class(data=request.data)
		context = {}
		
		if project_serializer.is_valid():
			project_instance = Project.objects.create(**project_serializer.validated_data)
			project_instance.save()
			context['project'] = project_serializer.data
			
			if request.data['tasks']:
				task_list = []
				for entry in request.data['tasks']:
					task_list.append(Task(**entry,project=project_instance))
				task_instance = Task.objects.bulk_create(task_list)
				task_serializer = TaskSerializer(task_instance,many=True)
				context['project']['task'] = task_serializer.data

			return Response(context, status=status.HTTP_201_CREATED)

		return Response({
		'status': 'Bad request',
		'message': 'Project could not be created with received data.'
		}, status=status.HTTP_400_BAD_REQUEST)


		

	def retrieve(self, request, pk=None):
		print("--==r")
		pass

	def update(self, request, pk=None):
		print("==---==")
		pass

	def partial_update(self, request, pk=None):
		project_object = self.get_project_object(pk)
		serializer = ProjectSerializer(project_object, data=request.data, partial=True) # set partial=True to update a data partially
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=201)
		return Response("wrong parameters",status=400)
		

	def destroy(self, request, pk=None):
		print("==--d-==")

		pass