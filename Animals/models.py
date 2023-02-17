from django.db.models import *
from Farm.models import Farm

SPAN = (
    ('daily' , "Daily"),
    ('weekly' , "Weekly"),
    ('monthly' , "Monthly"),
    ('quarter' , "Quarter"),
    ('twice' , "Twice"),
    ('yearly' , "Yearly"),
)

class AnimalExpences(Model):
    id = AutoField(primary_key=True , auto_created=True)
    expence = CharField(max_length=50)
    repeated = BooleanField()
    repeating_span = CharField(max_length=50,choices=SPAN,blank=True,null=True)
    def __str__(self):
        return self.expence

class AnimalTypes(Model):
    id = AutoField(primary_key=True , auto_created=True)
    type = CharField(max_length=50)
    in_expences = ManyToManyField(AnimalExpences , related_name='in_expences')
    out_expences = ManyToManyField(AnimalExpences , related_name='out_expences')
    image = FileField(upload_to="static/pictures/animals/",null=True,blank=True)
    lifespan = IntegerField(null=True)
    def __str__(self):
        return self.type

class Animal(Model):
    id = AutoField(primary_key=True , auto_created=True)
    type = ForeignKey(AnimalTypes , on_delete=PROTECT)
    farm = ForeignKey(Farm , on_delete=PROTECT)
    name = CharField(max_length=50)
    age = IntegerField(verbose_name='Months')
    def __str__(self):
        return self.name
