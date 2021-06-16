from django.urls import path 
from . import views
from django.conf.urls import url, include


app_name = 'project'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
#     url(r'^delete/(?P<pk>\d+)/$', views.ProjectDeleteView.as_view(),
#         name='project_delete'),
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'project', views.ProjectViewSet, basename='project')
urlpatterns = router.urls