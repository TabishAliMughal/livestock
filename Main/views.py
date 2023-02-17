from django.shortcuts import render
from Animals.models import AnimalTypes
from Main.models import MainPageSlider
import random


def MainPage(request):
    animals = AnimalTypes.objects.all()
    slider = MainPageSlider.objects.all()
    slid = []
    for i in slider:
        slid.append(i)
    random.shuffle(slid)
    total_slider = len(slider)
    context = {
        'animals' : animals ,
        'slider' : slider ,
        'total_slider' : total_slider ,
    }
    return render(request , 'Main/MainPage.html' , context)
    