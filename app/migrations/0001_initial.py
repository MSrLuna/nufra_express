# Generated by Django 5.1.1 on 2024-10-30 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(default='', max_length=14)),
                ('nombre', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=255)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(default='', max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.usuario')),
                ('apellido', models.CharField(max_length=150)),
            ],
            bases=('app.usuario',),
        ),
        migrations.CreateModel(
            name='Picker',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.usuario')),
                ('apellido', models.CharField(max_length=150)),
            ],
            bases=('app.usuario',),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('fecha_ingreso', models.DateField()),
                ('precio_unitario', models.FloatField()),
                ('disponible', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.categoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenesCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(default='', max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.usuario')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('stock_actual', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('fecha_actualizacion', models.DateField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.producto')),
            ],
        ),
        migrations.CreateModel(
            name='CarroCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.usuario')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.roles'),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_boleta', models.IntegerField(default=0)),
                ('fecha', models.DateField()),
                ('total', models.FloatField()),
                ('rut_cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.venta')),
            ],
        ),
    ]