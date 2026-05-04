import re

from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    
    # O método __init__ é um método especial em Python. Ele é usado para inicializar os atributos do objeto e configurar o formulário.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personaliza os rótulos, placeholders e ajuda para os campos do formulário.
        # ver mais em django widgets
        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['email'].label = 'E-mail'
        self.fields['phone'].label = 'Telefone'

        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nome'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Sobrenome'})
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Telefone'})

        self.fields['phone'].help_text = '(99)99999-9999'

    
    # A classe Meta é usada para configurar o formulário, indicando qual modelo ele representa e quais campos devem ser incluídos no formulário.
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'description',
            'category'
        )

    # O método clean é usado para validar os dados do formulário. Ele é chamado automaticamente quando o formulário é enviado e pode ser usado para adicionar validações personalizadas. 
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if first_name == last_name:
            self.add_error(
                'last_name', 
                ValidationError('O sobrenome deve ser diferente do nome.', 
                                code='invalid'
                )
            )
            
        if len(first_name) < 3 or len(first_name) > 50:
            self.add_error(
                'first_name', 
                ValidationError('O nome deve conter entre 3 e 50 caracteres.', 
                                code='invalid'
                )
            )
            
        if len(last_name) < 3 or len(last_name) > 50:
            self.add_error(
                'last_name', 
                ValidationError('O sobrenome deve conter entre 3 e 50 caracteres.', 
                                code='invalid'
                )
            )
            
        if Contact.objects.filter(email=email).exists():
            self.add_error(
                'email', 
                ValidationError('Este e-mail já está em uso.', 
                                code='invalid'
                )
            )
        
        if Contact.objects.filter(phone=phone).exists():
            self.add_error(
                'phone', 
                ValidationError('Este telefone já está em uso.', 
                                code='invalid'
                )
            )
        if not re.match(r'^\(?\d{2}\)?\s?9?\d{4}[-.\s]?\d{4}$', phone):
            self.add_error(
                'phone', 
                ValidationError('O telefone deve estar no formato (99)99999-9999.', 
                                code='invalid'
                )
            )
            