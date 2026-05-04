
from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    print('contatos | index')
    contacts = Contact.objects.filter(show=True).order_by('id')

    #o paginator do django é uma classe para a criação de paginação em lista de objetos
    #ver mais sobre ele em: https://docs.djangoproject.com/en/4.2/topics/pagination/
    paginator = Paginator(contacts, 10)  # Exibe 10 contatos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {
    }

    return render(
        request,
        'contact/index.html',
        context
    )
