from django.forms import ModelForm
from Animals.models import Animal , AnimalExpences , AnimalProducts , AnimalGroups


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = [
            'type',
            'farm',
            'animal',
            'age',
            'image',
        ]

class AnimalExpenceForm(ModelForm):
    class Meta:
        model = AnimalExpences
        fields = [
            'animal',
            'expence',
            'unit',
            'qty',
            'date',
            'time',
        ]

class AnimalProductForm(ModelForm):
    class Meta:
        model = AnimalProducts
        fields = [
            'animal',
            'product',
            'unit',
            'qty',
            'date',
            'time',
        ]


class AnimalGroupsForm(ModelForm):
    class Meta:
        model = AnimalGroups
        fields = [
            'farm',
            'type',
            'group',
            'animals',
        ]
