from django.urls import path
from . import views

#added app name so links don't crosslink and link unneccesary pages due to toomany index.html files
app_name = 'tasks'

urlpatterns =[
    path("index/" , views.index , name ="index"),
    path("add/" , views.add , name="add"),
]