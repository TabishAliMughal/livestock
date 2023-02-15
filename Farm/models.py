from django.db.models import *

class Farm(Model):
    id = AutoField(primary_key=True , auto_created=True)
    name = CharField(max_length=100)
    owner = CharField(max_length=50)
    phone = CharField(max_length=11,null=True , blank=True)
    mobile = CharField(max_length=11,)
    email = EmailField(null=True , blank=True)
    address = CharField(max_length=250)
    def __str__(self):
        return self.name
