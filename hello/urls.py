from django.urls import path
from . import views

#added app name so links don't crosslink and link unneccesary pages due to toomany index.html files
app_name = "hello"

urlpatterns=[
    path("" , views.index , name="index"),
     path("index1" , views.index1 , name="index1"),
   path("<str:name>" ,views.greet , name ="greet"),
   
    ]


