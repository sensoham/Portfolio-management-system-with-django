from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from userproject.models import Project
from . import views

app_name = 'projects'

urlpatterns = [ url(r'^$', views.project_list, name="list"), 
				url(r'^(?P<pk>\d+)$', views.project_detail, name="detail"),
				url(r'^create/$', views.project_create, name="create")] 