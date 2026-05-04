from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['email'].label = 'E-mail'
        self.fields['phone'].label = 'Telefone'

        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nome'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Sobrenome'})
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Telefone'})


    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
        )
