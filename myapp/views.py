#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import  render, redirect, get_list_or_404
from .forms import CreateNewTask, CreateNewProject

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
    tasks = Task.objects.all()
    return render(request,'tasks.html', {
            'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
       return render(request, 'create_task.html', {
       'form': CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
       return render(request, 'create_project.html', {
       'form' : CreateNewProject()
    })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_list_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    print(project)
    return render(request, 'detail.html',{
        'project': project,
        'tasks':tasks
    })
    
