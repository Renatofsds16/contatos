# type:ignore
from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForms
from django.urls import reverse
from contact.models import Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:loguin_views')
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForms(request.POST, request.FILES)
        context = {
            'forms': form,
            'form_action': form_action
        }
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)
        return render(
            request,
            'contact/create.html',
            context=context
        )
    context = {
        'forms': ContactForms(),
        'form_action': form_action
    }
    return render(
        request,
        'contact/create.html',
        context=context
    )


@login_required(login_url='contact:loguin_views')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True,
        owner=request.user,
    )
    form_action = reverse('contact:update', args=(contact_id,))
    if request.method == 'POST':
        form = ContactForms(request.POST, request.FILES, instance=contact)
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
        'forms': ContactForms(instance=contact),
        'form_action': form_action
    }
    return render(
        request,
        'contact/create.html',
        context=context
    )


@login_required(login_url='contact:loguin_views')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user,
    )
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
