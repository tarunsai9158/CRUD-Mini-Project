from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StudentDatabase
from django.contrib import messages

def index(request):
    data=StudentDatabase.objects.all()
    context = {"data": data}
    return render(request, 'index.html',context)




def insert(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query = StudentDatabase(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request, "Data Inserted Successfully")
        return redirect("/")

    return render(request, 'index.html')


def updatedata(request,id):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        
        edit=StudentDatabase.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,"Data Updates Successfully")
        return redirect("/")
    
    d=StudentDatabase.objects.get(id=id)
    context = {"d": d}
    return render(request, 'edit.html',context)


def deletedata(request,id):
    d=StudentDatabase.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")
    return redirect('/')
    
