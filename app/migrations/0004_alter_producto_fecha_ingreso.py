# Generated by Django 5.1.1 on 2024-11-06 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_producto_fecha_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_ingreso',
            field=models.DateField(),
        ),
    ]