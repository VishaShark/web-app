from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Client
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = Client.objects.get(email=email)
            request.session['user_id'] = user.id
            return redirect('profile')
        else:
            messages.error(request, 'Неверные учетные данные.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно. Войдите в систему.')
            return redirect('login')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Client.objects.get(id=user_id)
        return render(request, 'users/profile.html', {'user': user})
    else:
        return redirect(request, 'login')