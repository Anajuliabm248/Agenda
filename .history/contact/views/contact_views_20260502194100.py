from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.db.models import Q

# Create your views here.

def index(request):
    print('contatos | index')
    contacts = Contact.objects.filter(show=True).order_by('id')

    paginator = Paginator(contacts, 10)  # Exibe 10 contatos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

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
    search_value = request.GET.get('q', '').strip()

    if not search_value:
        return redirect('contact:index')

    #icontains é case insensitive, ou seja, não diferencia maiúsculas de minúsculas
    #icontains é um filtro de consulta do Django que é usado para realizar buscas em campos de texto; 
    #Ele é utilizado para verificar se um determinado valor está contido em um campo de texto, independentemente de como as letras estão capitalizadas.
    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value)  |
                Q(phone__icontains=search_value)      |
                Q(email__icontains=search_value)
        ) \
        .order_by('id')

    context= {
        'title': 'Contatos -  Agenda',
        'contacts': contacts,
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, id = contact_id, show = True)

    # O título da página é o nome do contato seguido de " - Agenda"
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