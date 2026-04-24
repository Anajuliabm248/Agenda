from django.db import models
from django.contrib.auth.models import User

'''
#CRUD -> cria a migração para uma nova tabela
Para fazer as migrações:
python manage.py makemigrations
python manage.py migrate
'''

#id -> primary key
#first_name -> sring
#last_name -> string
#phone -> string
#email -> email
#created_date -> data
#description -> text
#category -> foreing key
#show -> boolean
#owner -> foreing key
#picture -> imagem

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Contact(models.Model):
    #o id ja é gerado automaticamente pelo Django
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True) #pega a data e hora atual da criação do novo contato
    description = models.TextField(blank=True) #opicional
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%y/%m/') #na pasta pictures ele cria uma pasta com ano e mês para ficar mais organizado
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True) #pode ser CASCADE também
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    #forma de definir o nome do contato no models de admin
    def __str__(self):
        return f'{self.first_name} {self.last_name}'






