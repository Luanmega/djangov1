# Generated by Django 4.0 on 2021-12-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendas', '0002_alter_tiendas_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiendas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
