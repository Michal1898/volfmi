from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from person_creator.humaniser.humaniser import random_person
from volfmi.humaniser2.models import Person

from random import getrandbits

class PeopleView(View):
  def get(self, request):
    Person.objects.all().delete()
    n=random_person(bool(getrandbits(1)))
    n=requests.get('https://humaniser2.herokuapp.com/?sex=female&count=10')
    n=n.json()
    for m in n:

      print(m)
      firstname = m.get("firstname")
      surname = m.get("surname")
      gender = m.get("gender")
      birthdate = datetime.date.today()
      city = m.get("city")
      street = m.get("street")
      if street =="":
        street = city
      house_no = m.get("house_no")
      plz = m.get("plz")
      print(firstname, surname, gender, birthdate, city, street, house_no, plz)
      n=Person(
        firstname = firstname,
        surname = surname,
        gender = gender,
        birthdate = datetime.date.today(),
        city = city,
        street = street,
        house_no = house_no,
        plz = plz)

      n.save()
    return render(
      request, template_name='person_list_1.html' ,
      context={'people' : Person.objects.all()}
    )

class PeopleListView(ListView):
  template_name = 'person_list_2.html'
  model = Person
