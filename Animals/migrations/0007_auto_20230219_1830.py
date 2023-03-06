# Generated by Django 3.1.1 on 2023-02-19 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Farm', '0003_expenceunits'),
        ('Animals', '0006_auto_20230219_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalexpences',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Farm.units'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animalproducts',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Farm.units'),
            preserve_default=False,
        ),
    ]