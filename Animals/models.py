from django.db.models import *
from Farm.models import Farm , ExpenceUnits , ProductUnits
from autoslug import *

SPAN = (
    ('daily' , "Daily"),
    ('weekly' , "Weekly"),
    ('monthly' , "Monthly"),
    ('quarter' , "Quarter"),
    ('twice' , "Twice"),
    ('yearly' , "Yearly"),
)

class ExpencesAndProduct(Model):
    id = AutoField(primary_key=True , auto_created=True)
    expence = CharField(max_length=50)
    repeated = BooleanField()
    repeating_span = CharField(max_length=50,choices=SPAN,blank=True,null=True)
    def __str__(self):
        return self.expence

class AnimalTypes(Model):
    id = AutoField(primary_key=True , auto_created=True)
    type = CharField(max_length=50)
    slug = AutoSlugField(populate_from='type')
    expences = ManyToManyField(ExpencesAndProduct , related_name='expences')
    product = ManyToManyField(ExpencesAndProduct , related_name='product')
    image = FileField(upload_to="static/pictures/animals/",null=True,blank=True)
    lifespan = IntegerField(null=True)
    def __str__(self):
        return self.type
    def getImage(self):
        return str(self.image)[7:]

class Animal(Model):
    id = AutoField(primary_key=True , auto_created=True)
    type = ForeignKey(AnimalTypes , on_delete=PROTECT)
    farm = ForeignKey(Farm , on_delete=PROTECT)
    animal = CharField(max_length=50)
    age = IntegerField(verbose_name='Months')
    image = FileField(upload_to="static/pictures/animals/",null=True,blank=True)
    def __str__(self):
        return self.animal
    def getImage(self):
        if self.image:
            return str(self.image)[7:]
        else:
            return str("Images/no-img.png")

class AnimalExpences(Model):
    id = AutoField(primary_key=True , auto_created=True)
    animal = ForeignKey(Animal , on_delete=PROTECT)
    expence = ForeignKey(ExpencesAndProduct , on_delete=PROTECT)
    unit = ForeignKey(ExpenceUnits , on_delete=PROTECT)
    qty = CharField(max_length=5)
    date = DateField()
    time = TimeField()
    timestamp = DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('animal', 'expence','date')
    def __str__(self):
        return "{}".format(self.animal)
    def QTY(self):
        return "{} {}".format(self.qty,self.unit)

class AnimalProducts(Model):
    id = AutoField(primary_key=True , auto_created=True)
    animal = ForeignKey(Animal , on_delete=PROTECT)
    product = ForeignKey(ExpencesAndProduct , on_delete=PROTECT)
    unit = ForeignKey(ProductUnits , on_delete=PROTECT)
    qty = CharField(max_length=5)
    date = DateField()
    time = TimeField()
    timestamp = DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('animal', 'product','date')
    def __str__(self):
        return "{}".format(self.animal)
    def QTY(self):
        return "{} {}".format(self.qty,self.unit)

class AnimalGroups(Model):
    id = AutoField(primary_key=True , auto_created=True)
    farm = ForeignKey(Farm , on_delete=PROTECT)
    type = ForeignKey(AnimalTypes , on_delete=PROTECT)
    group = CharField(max_length=100)
    animals = ManyToManyField(Animal , related_name='animals')
    def __str__(self):
        return self.group