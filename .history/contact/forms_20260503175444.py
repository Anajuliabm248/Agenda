from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona a classe CSS 'form-control' a cada campo do formulário
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
        )
