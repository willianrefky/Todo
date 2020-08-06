from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    # logika simpan
    if request.method=='POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/')

    isi ={
        'tasks' : tasks,
        'form' : form,
    }
    return render(request, 'tasks/list.html', isi)

def update(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)

    # logika update
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    isi = {
        'form' : form
    }
    return render(request, 'tasks/update_task.html', isi)

def deleteItem(request, pk):
    item = Task.objects.get(id=pk)

    # logika hapus
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    isi={
        'item' : item,
    }
    return render(request, 'tasks/delete_task.html', isi)