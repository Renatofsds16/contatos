#type:ignore
from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# Create your views here.
def index(request):
    title = 'contacts'
    contacts = Contact.objects.all().filter(show=True).order_by('-id')
    context = {'contacts': contacts, 'title': title}
    return render(request, 'contact/index.html', context=context)

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id), show=True)
    context = {'contact': single_contact,}
    return render(request, 'contact/contact.html', context=context)