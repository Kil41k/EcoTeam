from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateForm, CommentSend
from .models import Projects, Category, Comment
from users.models import User


def indexview(request):
    projs = Projects.objects.filter(is_completed=False)
    cats = Category.objects.all()
    query = request.GET.get('q', '')  # получаем параметр q из GET-запроса
    users = User.objects.none()  # пустой QuerySet по умолчанию

    if query:
        users = User.objects.filter(username__icontains=query)
    context = {'projs': projs, 'cats': cats, 'title': 'Главная страница | EcoTeam', 'users': users, 'query': query}
    return render(request, 'main/index.html', context)

def category(request, cat_id):
    cat = get_object_or_404(Category, id=cat_id)
    context = {
        'title': 'Категория | EcoTeam',
        'projs': Projects.objects.filter(category=cat, is_completed=False),
        'cats': Category.objects.all()
    }
    return render(request, 'main/index.html', context)

@login_required
def about(request, proj_id):
    proj = get_object_or_404(Projects, id=proj_id)
    comments = Comment.objects.filter(proj=proj)
    if request.method == 'POST':
        form = CommentSend(data=request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.user = request.user
            comm.proj = proj
            comm.save()
            return redirect('about', proj.id)
    else:
        form = CommentSend
    context = {
        'title': 'О проекте | EcoTeam',
        'proj': proj,
        'coms': comments,
        'form': form
    }
    return render(request, 'main/about.html', context)

def completeproj(request, proj_id):
    proj = get_object_or_404(Projects, id=proj_id)
    proj.is_completed = True
    return redirect('profile', request.user.id)

def joinproj(request, proj_id):
    proj = get_object_or_404(Projects, id=proj_id)
    proj.participants.add(request.user)
    return redirect('about', proj_id)

def create(request):
    err = None
    if request.method == 'POST':
        form = CreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.user = request.user
            proj.save()
            proj.participants.add(request.user)
            return redirect('index')
        else:
            err = form.errors
    else:
        form = CreateForm
    return render(request, 'main/create.html', {'form': form, 'title': 'Создание проекта | EcoTeam', 'errors': err})