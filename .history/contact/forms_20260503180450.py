from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nome' },{'label': 'Nome' })
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Sobrenome', 'label': 'Sobrenome' })
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail', 'label': 'E-mail' })
        self.fields['phone'].widget.attrs.update({'placeholder': 'Telefone', 'label': 'Telefone', 'helper-text': '(99)99999-9999'})


    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
        )
