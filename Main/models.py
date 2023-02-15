from django.db.models import *


class MainPageSlider(Model):
    id = AutoField(primary_key=True,unique=True)
    caption = CharField(max_length=500,blank=True,null=True)
    image = FileField(upload_to="./assets/pictures/slider")
    flow = IntegerField(auto_created=True,blank=True,null=True)