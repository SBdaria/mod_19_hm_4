from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

def sign_up_by_html(request):
    users_buyer = Buyer.objects.all()
    users = [i.name for i in users_buyer]
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            Buyer.objects.create(name=username, balance=1000, age=int(age))
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html', context=info)

def sign_up_by_django(request):
    users_buyer = Buyer.objects.all()
    users = [i.name for i in users_buyer]
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=1000, age=int(age))
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
        info['form'] = form
    return render(request, 'registration_page.html', context=info)



def homepage(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'homepage.html', context)

def gamespage(request):
    games = Game.objects.all()
    context = {
        'title': 'Игры',
        'games': games
    }
    return render(request, 'games.html', context)

def boxpage(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, 'box.html', context)