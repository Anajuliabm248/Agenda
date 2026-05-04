from contact.models import Contact

class ContactForm(forms.ModelForm):
    #a classe MeContactada para configurar o formulário, indicando qual modelo ele representa e quais campos devem ser incluídos no formulário.
    class Meta: 
        model = Contact
        fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        )
    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error('first_name', 'O campo nome é obrigatório.') #adiciona um erro ao campo 'first_name' se ele estiver vazio, indicando que o campo é obrigatório.
        self.add_error('last_name', 'O campo sobrenome é obrigatório.') #adiciona um erro ao campo 'last_name' se ele estiver vazio, indicando que o campo é obrigatório.
        self.add_error('email', 'O campo email é obrigatório.') #adiciona um erro ao campo 'email' se ele estiver vazio, indicando que o campo é obrigatório.
        self.add_error('phone', 'O campo telefone é obrigatório.') #adiciona um erro ao campo 'phone' se ele estiver vazio, indicando que o campo é obrigatório.

        return super().clean() #chama o método clean da classe pai para garantir que a validação padrão do formulário seja execut
