from django.shortcuts import redirect, render
from django.urls import reverse
from contact.forms import ContactForm


def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
            'form': form,
            
        }

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

def update(request, contact_id):
    form_action = reverse('contact:update', kwargs={'contact_id': contact_id})

    if request.method == 'POST':
        form = ContactForm(request.POST)

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