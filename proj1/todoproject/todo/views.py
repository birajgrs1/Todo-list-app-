from django.shortcuts import render,redirect
from .models import TodoProj
def todo_list(request):
    todos=TodoProj.objects.order_by('-id')
    # todos=TodoProj.objects.get()
    # todos=TodoProj.objects.all()
    return render(request,'todo/home.html',{'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')  
        TodoProj.objects.create(title=title, description=description)  

    return redirect('todo_list')


def complete_todo(request,todo_id):
    todo=TodoProj.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect('todo_list')

def delete_todo(request,todo_id):
    todo=TodoProj.objects.get(id=todo_id)
    todo.delete()
    
    return redirect('todo_list')


        
        