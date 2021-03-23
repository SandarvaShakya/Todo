from todolist.models import TaskList
from django.shortcuts import redirect, render
from todolist.forms import TaskForm


def index(request):
    task = TaskList.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form, 'tasks': task}
    return render(request, 'todolist/index.html', context)


def completed(request, primary_key):
    task = TaskList.objects.get(id=primary_key)
    task.completed = True
    task.save()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


def delete(request, primary_key):
    task = TaskList.objects.get(id=primary_key)
    task.delete()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
