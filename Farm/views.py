from django.shortcuts import render , redirect
from Farm.models import Farm , FarmGallery
from Animals.models import Animal , AnimalTypes , AnimalGroups

def nav(request):
    farm = Farm.objects.get(user = request.user.pk)
    types = AnimalTypes.objects.all()
    available_types = []
    for i in types:
        animals = Animal.objects.filter(type = i , farm = farm)
        if len(animals):
            available_types.append({ 'type' : i.type , 'slug' : i.slug })
    # return available_types
    request.session['nav'] = available_types

def Dashboard(request):
    nav(request)
    farm = Farm.objects.get(user = request.user.pk)
    groups = AnimalGroups.objects.filter(farm = farm)
    gallery = [i.getImage() for i in FarmGallery.objects.filter(farm = farm)]
    expences = Animal.objects.filter(farm = farm)
    print(expences)
    context = {
        'farm' : farm ,
        'groups' : groups ,
        'gallery' : gallery ,
    }
    return render(request , 'Farm/Dashboard.html' , context)

