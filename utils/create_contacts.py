import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000 #vão ser criados 1000 objetos

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = 'Agenda.settings'
settings.USE_TZ = False

django.setup()

#tudo acima foi criado só para conseguir usar o from contact.models import Category, Contact abaixo

if __name__ == '__main__':
    import faker #biblioteca para gerar dados fakes para testar a aplicação

    from contact.models import Category, Contact

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos', 'Trabalho', 'Faculdade']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()  #salva as categorias criadas

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):  #cria um dicionario de contatos com o faker
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = random_text = fake.text(max_nb_chars=100)
        category = choice(django_categories)  #escolhe a categoria aleatoriamente
        print(first_name, email)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:  #se existem contatos cria todos os eles
            Contact.objects.bulk_create(django_contacts)



