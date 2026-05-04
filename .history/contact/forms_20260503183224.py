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


    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
        )

    # O método clean é usado para validar os dados do formulário. Ele é chamado automaticamente quando o formulário é enviado e pode ser usado para adicionar validações personalizadas. 
    def clean(self):
        cleaned_data = super().clean()
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if len(first_name) < 3 or len(first_name) > 50:
            self.add_error(
                'first_name', 
                ValidationError('O nome deve conter entre 3 e 50 caracteres.', 
                                code='invalid'
                )
            )
        
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        
        if len(last_name) < 3 or len(last_name) > 50:
            self.add_error(
                'last_name', 
                ValidationError('O sobrenome deve conter entre 3 e 50 caracteres.', 
                                code='invalid'
                )
            )
        
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if Contact.objects.filter(email=email).exists():
            self.add_error(
                'email', 
                ValidationError('Este e-mail já está em uso.', 
                                code='invalid'
                )
            )
        
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        if Contact.objects.filter(phone=phone).exists():
            self.add_error(
                'phone', 
                ValidationError('Este telefone já está em uso.', 
                                code='invalid'
                )
            )
        if re.match(r'^(\(\d{2}\)\s?|9\d{4}-?\d{4}|\d{4}-?\d{4}|\d{5}-?\d{4})$', phone) is None:
            self.add_error(
                'phone', 
                ValidationError('O telefone deve estar no formato (99)99999-9999.', 
                                code='invalid'
                )
            )
        
        return phone
            