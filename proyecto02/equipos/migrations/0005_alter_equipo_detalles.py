# Generated by Django 4.0.3 on 2022-04-02 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0004_equipo_hdd_alter_equipo_ram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='detalles',
            field=models.TextField(max_length=255, null=True, verbose_name='Detalles'),
        ),
    ]
