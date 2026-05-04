
from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms #classe para criar formulários personalizados
# Create your views here.

# Formulário para criar um contato
class ContactForm(forms.ModelForm):
    #a classe Meta é usada para configurar o formulário, indicando qual modelo ele representa e quais campos devem ser incluídos no formulário.
    class Meta: 
        model = Contact
        fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        )

def create(request):
    if request.method == 'POST': #verifica se o método da requisição é POST, indicando que o formulário foi enviado.
        context= {
            'form': ContactForm(data=request.POST) #instancia o formulário, passando os dados do POST se houver, ou None caso contrário.
        }

        return render(
            request,
            'contact/create.html',
            context
        )
    context = {
        'form': ContactForm() #instancia o formulário vazio para exibir na página de
    