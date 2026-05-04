
from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms #classe para criar formulários personalizados
# Create your views here.

# Formulário para criar um contato
class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        )

def create(request):
    context= {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )
