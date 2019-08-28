from django.shortcuts import render, redirect, get_object_or_404
from MusaApp.models import *
def index(request):
    return render(request, 'project/index.html')
def project(request,id):
    
    p=Project.objects.get(id=id)
    return render(request, 'project/project.html',context={'name':p})

def AllProject(request):
    Items =Project.objects.all()
    context={'Items':Items,
             }
    return  render(request, 'project/allproject.html',context)