from django.contrib import admin
from django.urls import path
from student_details.views import *
urlpatterns = [
    path('',index, name="index"),
    path('insert',insert, name="insert"),
    path('update/<id>',updatedata, name="update"),
    path('delete/<id>',deletedata, name="delete"),
   

]