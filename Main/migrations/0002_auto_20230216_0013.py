# Generated by Django 3.1.1 on 2023-02-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpageslider',
            name='caption',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='mainpageslider',
            name='flow',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
    ]
