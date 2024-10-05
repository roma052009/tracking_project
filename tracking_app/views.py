from django.shortcuts import render, get_object_or_404, redirect
from tracking_app.models import User, Task
from django.db.models import Q
from datetime import datetime

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        usernames = User.objects.values_list('name', flat=True)
        if name in usernames:
            return render(request, 'sign_up.html', {'name_text': "Користувач з цим іменем вже існує"})
        else:
            user = User.objects.create(name=name, password=password, email=email)
            request.session['user_id'] = user.id
            return redirect('tasks_list')
    
    return render(request, 'sign_up.html', {'name_text': ""})

def log_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.get(name=name)

        if password == user.password:
            request.session['user_id'] = user.id
            return redirect('tasks_list')
        else:
            return render(request, 'log_in.html', {'password_text': "Пароль невірний"})
    return render(request, 'log_in.html', {'password_text': ""})

def tasks_list(request):
    tasks = Task.objects.filter(receiver_id = request.session['user_id'])
    return render(request, 'tasks_list.html', {'tasks': tasks, 'name': User.objects.get(id=request.session['user_id']).name})

def tasks_from_you(request):
    tasks = Task.objects.filter(giver_id = request.session['user_id'])
    return render(request, 'tasks_from_you.html', {'tasks': tasks, 'name': User.objects.get(id=request.session['user_id']).name})

def creating_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        stat = request.POST.get('stat')
        term = request.POST.get('term')
        receiver = User.objects.get(id = request.POST.get('receiver'))
        print("Name:", name)
        print("Description:", description)
        print("Stat:", stat)
        print("Term:", term)
        print("Receiver ID:", request.POST.get('receiver'))
        print("Giver ID:", request.session.get('user_id'))
        Task.objects.create(name=name, description=description, stat=stat, term=term, giver_id=User.objects.get(id = request.session['user_id']), receiver_id=receiver)

    return render(request, 'creating_task.html', {'users': User.objects.all()})

