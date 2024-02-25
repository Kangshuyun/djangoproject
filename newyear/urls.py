from django.urls import path
from . import views

#added app name so links don't crosslink and link unneccesary pages due to toomany index.html files
app_name = "newyear"
urlpatterns =[
    path("" , views.index , name = "index"),
]