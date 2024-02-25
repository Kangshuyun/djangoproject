from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = [ ]

class NewTaskForm(forms.Form):
    tasks = forms.CharField(label = "new Task")
   
# Create your views here.
def index(request):
    return render(request , "tasks/index.html" ,{ "tasks" : tasks})


def add(request):
    if request.method == "POST":
       
       form = NewTaskForm(request.POST)

       if form.is_valid():
           
           task = form.cleaned_data["tasks"] #

           tasks.append(tasks)                    

           return HttpResponseRedirect(reverse("tasks:index"))
       else:
           return render(request, "tasks/add.html" , { "form" : form})

    return render(request, "tasks/add.html", { "form":NewTaskForm() })