import os

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

import django
django.setup()

#Fake POP Script

import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']

def add_topic():
    t , created = Topic.objects.get_or_create(top_name = random.choice(topics))
    if created:
     t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #Create the topic for the entry
        top = add_topic()

        #create the fake data

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry

        webpg = Webpage.objects.get_or_create(topic = top , name = fake_name, url = fake_url)[0]
       
       #crreate the access page

        access_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]


if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating Successfull")
