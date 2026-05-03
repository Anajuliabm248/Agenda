from django.http import Http404
from django.shortcuts import render, get_object_or_404
from contact.models import Contact
# Create your views here.

def index(request):
    print('contatos | index')
    contacts = Contact.objects.filter(show=True).order_by('id')

    context= {
        'title': 'Contatos -  Agenda',
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    
    
    contacts = Contact.objects.filter(show=True).order_by('id')

    context= {
        'title': 'Contatos -  Agenda',
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, id = contact_id, show = True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - Agenda'

    context= {
        'title': site_title,
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )