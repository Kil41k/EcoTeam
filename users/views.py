from django.shortcuts import render, redirect, get_object_or_404

from main.models import Projects
from .forms import UserChangeData, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout

from .models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegistrationForm
    return render(request, 'users/register.html', {'form': form, 'title': 'Регистрация | EcoTeam'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {
        'form': form,
        'title': 'Вход | EcoTeam'
    })

def userChangeView(request):
    if request.method == 'POST':
        form = UserChangeData(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index')
    else:
        form = UserChangeData(instance=request.user)
    return render(request, 'users/redak.html', {'form': form, 'title': 'Редактирование профиля | EcoTeam'})
            

def logoutview(request):
    logout(request.user)
    return redirect('index')

def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    completed = user.projectss.filter(is_completed=True)
    active = user.projectss.filter(is_completed=False)
    context = {
        'completed': completed,
        'user': user,
        'active': active,
        'title': 'Профиль | EcoTeam'
    }
    return render(request, 'users/profile.html', context)

def complete(request, aproj_id):
    proj = get_object_or_404(Projects, id=aproj_id)
    proj.is_completed = True
    proj.save()
    return redirect('profile', request.user.id)
