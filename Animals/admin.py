from django.contrib import admin
from Animals.models import AnimalExpences , AnimalTypes , Animal


admin.site.register(AnimalExpences)
admin.site.register(AnimalTypes)
admin.site.register(Animal)