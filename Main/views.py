from django.shortcuts import render
from Animals.models import AnimalTypes
from Main.models import MainPageSlider
import random


def MainPage(request):
    animals = AnimalTypes.objects.all()
    slider = list(MainPageSlider.objects.all())
    random.shuffle(slider)
    total_slider = len(slider)
    context = {
        'animals' : animals ,
        'slider' : slider ,
        'total_slider' : total_slider ,
    }
    return render(request , 'Main/MainPage.html' , context)
    