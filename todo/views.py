from django.shortcuts import render, redirect
from .models import*
from .forms import*
# Create your views here

def todo(request):
    model = Mytodo.objects.all()
    form = Todoform()
    if request.method== 'POST':
        form = Todoform(request.POST)
        if form.is_valid:
            form.save()
    return render(request, 'home.html', {'model':model, 'form':form})


def updateitem(request, pk):
    task = Mytodo.objects.get(id=pk)
    updateform = Todoform(instance=task)
    if request.method=="POST":
        updateform=Todoform(request.POST, instance=task)
        if updateform.is_valid:
            updateform.save()
            model = Mytodo.objects.all()
            form = Todoform()
            return render(request, 'home.html', {'model':model, 'form':form})

    return render(request, 'update.html', {'task':task, 'updateform':updateform})

def deleteitem(request, pk):
    task = Mytodo.objects.get(id=pk)
    task.delete()
    return redirect('todo')

