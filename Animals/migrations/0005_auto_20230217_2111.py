# Generated by Django 3.1.1 on 2023-02-17 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Animals', '0004_auto_20230216_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaltypes',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/pictures/animals/'),
        ),
    ]