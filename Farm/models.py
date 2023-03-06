from django.db.models import *
from django.contrib.auth.models import User
from autoslug import *

class Farm(Model):
    id = AutoField(primary_key=True , auto_created=True)
    user = OneToOneField(User , on_delete=PROTECT)
    farm = CharField(max_length=100)
    slug = AutoSlugField(populate_from='farm')
    owner = CharField(max_length=50)
    phone = CharField(max_length=11,null=True , blank=True)
    mobile = CharField(max_length=11,)
    email = EmailField(null=True , blank=True)
    address = CharField(max_length=250)
    def __str__(self):
        return self.farm

class ExpenceUnits(Model):
    id = AutoField(primary_key=True , auto_created=True)
    farm = ForeignKey(Farm , on_delete=PROTECT)
    unit = CharField(max_length=100)
    def __str__(self):
        return self.unit

class ProductUnits(Model):
    id = AutoField(primary_key=True , auto_created=True)
    farm = ForeignKey(Farm , on_delete=PROTECT)
    unit = CharField(max_length=100)
    class Meta:
        unique_together = ('farm', 'unit')
    def __str__(self):
        return self.unit

class FarmGallery(Model):
    id = AutoField(primary_key=True , auto_created=True)
    farm = ForeignKey(Farm , on_delete=PROTECT)
    image = FileField(upload_to="static/pictures/farm/gallery")
    def __str__(self):
        return self.farm.farm
    def getImage(self):
        if self.image:
            return str(self.image)[7:]
        else:
            return str("Images/no-img.png")