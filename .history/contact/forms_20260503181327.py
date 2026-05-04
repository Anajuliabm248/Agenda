from django import forms

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
        def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')
            return 
            