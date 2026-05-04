from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona a classe CSS 'form-control' a cada campo do formulário
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nome', 'label' })
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Sobrenome' })
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail' })
        self.fields['phone'].widget.attrs.update({'placeholder': 'Telefone' 'helper-text': '(99)99999-9999'})


    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
        )
