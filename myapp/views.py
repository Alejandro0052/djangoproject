#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

from django.shortcuts import render
# Create your views here.


def index(request):
    title='Django Course!!'
    return render(request,'Index.html', { 
        'title' : title
    })

def about(request):
    username = 'fazt'
    return render(request,'About.html', {
        'username' : username
    })


def hello(request, username):
    print(username)
    return HttpResponse('<h2>Hello %s</h2>' % username)
    

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects' : projects
    })

def tasks(request):
 #   task = Task.objects.get(title=title)
    return render(request,'tasks.html')

