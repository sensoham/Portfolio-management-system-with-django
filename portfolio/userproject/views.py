from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/accounts/login/")
def project_list(request):
	projects = Project.objects.all().order_by("-date")
	return render(request, 'userproject/project_list.html', {'projects':projects})

	
@login_required(login_url="/accounts/login/")	
def project_detail(request,pk):
	project = Project.objects.get(pk=pk)
	return render(request, 'userproject/project_detail.html', {'project':project})



@login_required(login_url="/accounts/login/")
def project_create(request):
	if request.method == 'POST':
		form = forms.CreateProject(request.POST)
		if form.is_valid():
			inst = form.save(commit=False)
			inst.author = request.user
			inst.save()
			return redirect('projects:list')
	
	else:
		form = forms.CreateProject()
	return render(request, 'userproject/project_create.html', {'form':form})