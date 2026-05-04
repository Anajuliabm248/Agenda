from django.shortcuts import redirect, render
from django.urls import reverse
from contact.forms import ContactForm


def create(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

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
