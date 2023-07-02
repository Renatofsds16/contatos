# type:ignore
from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'usuario registrado')
            return redirect('contact:index')
    context = {'forms': form}
    return render(request, 'contact/register.html', context)


def loguin_views(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('contact:index')
        else:
            messages.error(request, 'loguin invalido')
    return render(
        request,
        'contact/loguin_views.html',
        {'forms': form}
    )


def logout(request):
    auth.logout(request)
    return redirect('contact:loguin_views')


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            {'forms': form}
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {'forms': form}
        )
    form.save()
    return render(
            request,
            'contact/register.html',
            {'forms': form},
            )
