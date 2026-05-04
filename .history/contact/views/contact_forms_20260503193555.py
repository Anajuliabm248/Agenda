from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact
from contact.models import Contact


def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            return redirect('contact:update', contact_id=ContactForm)

        return render(
            request,
            'contact/create.html',
            context
        )

    return render(
        request,
        'contact/create.html',
        {'form': ContactForm()}
    )

def update(request, contact_id):
    contact = get_object_or_404(Contact, contact_id=contact_id, show=True)
    form_action = reverse('contact:update', kwargs={'contact_id': contact_id})

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('contact:index')

        return render(
            request,
            'contact/create.html',
            {'form': form}
        )

    return render(
        request,
        'contact/create.html',
        {'form': ContactForm()}
    )