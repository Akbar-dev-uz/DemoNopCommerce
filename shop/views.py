from django.contrib.auth.models import User
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'shop/index.html')


def news_archive(request):
    news_list = ["good"]
    return render(request, 'news/archive.html', {'news_list': news_list})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Создаем пользователя через User.objects.create_user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']  # автоматически хешируется
            )
            messages.success(request, 'Регистрация прошла успешно. Войдите в систему.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Неверный логин или пароль")

    return render(request, "shop/login.html")


def logout_view(request):
    logout(request)
    return redirect('login')
