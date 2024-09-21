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
            # return redirect('places_list')
    
    return render(request, 'sign_up.html', {'name_text': ""})

def log_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.get(name=name)

        if password == user.password:
            request.session['user_id'] = user.id
            return redirect('places_list')
        else:
            return render(request, 'log_in.html', {'password_text': "Пароль невірний"})
    return render(request, 'log_in.html', {'password_text': ""})