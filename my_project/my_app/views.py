from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import NewsFilms
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from .serializers import NewsFilmsSerializers, UserSerializer


# Create your views here.
def base(request):
    context = {}
    if not request.user.is_authenticated:
        context['user'] = request.GET.get('username')
        return render(request, 'main_page.html', context=context)
    else:
        context['user'] = None
        return render(request, 'main_page.html', context=context)

def main_page(request):
    news = NewsFilms.objects.all().order_by('-created_at')
    news = news[:2]
    context = {
        'news': news,
    }
    return render(request, 'main_page.html', context=context)

def news_page(request):
    news = NewsFilms.objects.all().order_by('-created_at')
    context = {
        'news': news
    }
    return render(request, 'news_page.html', context=context)

def registration(request):
    info = {}
    len_info = len(info)
    users_list = set()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        email = request.POST.get('email')
        users = User.objects.all()
        for user in users:
            users_list.add(user.username)
        if username in users_list:
            info['error'] = 'Такой пользователь уже существует'
            return render(request, 'registration_page.html', context=info)
        elif repeat_password != password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', context=info)
        elif int(age) < 16:
            info['error'] = 'Вы должны быть старше 16'
            return render(request, 'registration_page.html', context=info)
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            return render(request, 'registration_page.html',
                          context={'wellcome': f'Поздравляю вы зарегистрированы, теперь можете авторизоваться'})
    else:
        return render(request, 'registration_page.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user_login(request, user)
            return HttpResponseRedirect('/main/')
        else:
            return render(request, 'login_view.html', {'context': 'Вы ввели Логин/Пароль неправильно попробуйте войти еще раз'})
    else:
        return render(request, 'login_view.html')

def logout(request):
    user_logout(request)
    return render(request, 'logout.html')

def new_page(request, id):
    post = NewsFilms.objects.get(id=id)
    print(post)
    context = {
        'news': post
    }
    return render(request, 'new_page.html', context=context)

class NewsFilmsAPIView(generics.ListAPIView):
    queryset = NewsFilms.objects.all()
    serializer_class = NewsFilmsSerializers


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
