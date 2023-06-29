# type:ignore

from django.shortcuts import render, redirect
from contact.forms import ContactForms
from django.urls import reverse


def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForms(data=request.POST)
        context = {
            'forms': form,
            'form_action': form_action
        }
        if form.is_valid():
            form.save()
            return redirect('contact:update')
        return render(
            request,
            'contact/create.html',
            context=context
        )
    context = {
        'forms': ContactForms()
    }
    return render(
        request,
        'contact/create.html',
        context=context
    )


def update(request, contact_id):
    form_action = reverse('contact:update')
    if request.method == 'POST':
        form = ContactForms(data=request.POST)
        context = {
            'forms': form,
            'form_action': form_action
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)
        return render(
            request,
            'contact/create.html',
            context=context
        )
    context = {
        'forms': ContactForms()
    }
    return render(
        request,
        'contact/create.html',
        context=context
    )
