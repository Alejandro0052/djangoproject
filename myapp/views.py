#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request,'Index.html')

def hello(request, username):
    print(username)
    return HttpResponse('<h2>Hello %s</h2>' % username)
    

def about(request):
    return HttpResponse('<h1>About us</h1>')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
   # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s ' % task.title)

