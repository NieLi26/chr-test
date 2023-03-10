# Generated by Django 4.1.7 on 2023-02-18 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test2", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicio",
            name="estado",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="fecha_ingreso",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="inversion",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="mapa",
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="nombre",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="region",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="tipo",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="tipologia",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="titular",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
