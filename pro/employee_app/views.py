from django.shortcuts import render,redirect,get_object_or_404
from .models import employee
from .forms import EmployeeForm


def home(request):
    a=employee.objects.all()
    return render(request,"home.html",{'employee':a})

def add(request):
    form=EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,"form.html",{"form":form})

def edit(request,id):
    b=get_object_or_404(employee,id=id)
    form=EmployeeForm(request.POST or None,instance=b)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,"form.html",{"form":form})

def delete(request,id):
    d=get_object_or_404(employee,id=id)
    d.delete()
    return redirect('home')

