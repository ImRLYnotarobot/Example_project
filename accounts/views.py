from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponse

from .forms import UserCreationForm, UserLoginForm


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        # return redirect()
        return redirect(reverse('group_list'))
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return redirect(reverse('group_list'))
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    next = request.GET.get('next', reverse('group_list'))
    logout(request)
    return redirect(next)
