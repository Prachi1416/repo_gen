from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm



def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    template_name = 'auth_app/register.html'
    context = {'form':form}
    return render(request, template_name, context)

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('stu_list')
    template_name = 'auth_app/login.html'
    context = {'form':form}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login_url')




