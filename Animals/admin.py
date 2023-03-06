from django.contrib import admin
from Animals.models import ExpencesAndProduct , AnimalTypes , Animal , AnimalExpences , AnimalProducts , AnimalGroups


class AnimalExpencesModel(admin.ModelAdmin):
    list_display = [
        'animal',
        'expence',
        'QTY',
        'date',
        'time',
    ]

class AnimalProductsModel(admin.ModelAdmin):
    list_display = [
        'animal',
        'product',
        'QTY',
        'date',
        'time',
    ]

admin.site.register(ExpencesAndProduct)
admin.site.register(AnimalTypes)
admin.site.register(Animal)
admin.site.register(AnimalExpences , AnimalExpencesModel)
admin.site.register(AnimalProducts , AnimalProductsModel)
admin.site.register(AnimalGroups)