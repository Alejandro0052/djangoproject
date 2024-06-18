from django import forms 

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label="Descripcion de la tarea",
        widget=forms.Textarea)
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Name of Project", max_length=200)