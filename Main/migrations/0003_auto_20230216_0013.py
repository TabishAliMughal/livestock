# Generated by Django 3.1.1 on 2023-02-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20230216_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpageslider',
            name='image',
            field=models.FileField(default='abc', upload_to='./assets/pictures/slider'),
            preserve_default=False,
        ),
    ]
