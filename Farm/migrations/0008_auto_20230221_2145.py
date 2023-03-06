# Generated by Django 3.1.1 on 2023-02-21 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Farm', '0007_auto_20230221_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('image', models.FileField(upload_to='static/pictures/farm/gallery')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Farm.farm')),
            ],
        ),
        migrations.DeleteModel(
            name='FarmGalery',
        ),
    ]
