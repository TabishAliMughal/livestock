from django.shortcuts import render
from Farm.models import Farm , FarmGallery
from Animals.models import Animal , AnimalTypes , AnimalGroups
from django.contrib.auth.decorators import login_required
from Authentication.user_handeling import allowed_users, admin_only


def nav(request):
    farm = Farm.objects.get(user = request.user.pk)
    types = AnimalTypes.objects.all()
    available_types = []
    for i in types:
        animals = Animal.objects.filter(type = i , farm = farm)
        if len(animals):
            available_types.append({ 'type' : i.type , 'slug' : i.slug })
    request.session['nav'] = available_types

@login_required(login_url='Auth:Login')
@allowed_users(allowed_roles=['FarmOwner'])
def Dashboard(request):
    nav(request)
    farm = Farm.objects.get(user = request.user.pk)
    groups = AnimalGroups.objects.filter(farm = farm)
    gallery = [i.getImage() for i in FarmGallery.objects.filter(farm = farm)]
    expences = Animal.objects.filter(farm = farm)
    context = {
        'farm' : farm ,
        'groups' : groups ,
        'gallery' : gallery ,
    }
    return render(request , 'Farm/Dashboard.html' , context)

