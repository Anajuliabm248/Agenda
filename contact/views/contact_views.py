from django.shortcuts import render

# Create your views here.

def index(request):
    print('contatos | index')
    context= {
        'title': 'Contato',
        'head': 'Contato',
    }
    return render(
        request,
        'contact/index.html',
        context
    )
