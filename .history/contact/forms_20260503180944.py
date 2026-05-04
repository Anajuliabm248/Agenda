from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    
    # O método __init__ é um método especial em Python. Ele é usado para inicializar os atributos do objeto e configurar o formulário.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personaliza os rótulos, placeholders e ajuda para os campos do formulário.
        
        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['email'].label = 'E-mail'
        self.fields['phone'].label = 'Telefone'

        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nome'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Sobrenome'})
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Telefone'})

        self.fields['phone'].help_text = '(99)99999-9999'


    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
        )
