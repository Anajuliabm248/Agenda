
from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
# Create your views here.

def create(request):


    context= {
    }

    return render(
        request,
        'contact/create.html',
        context
    )
