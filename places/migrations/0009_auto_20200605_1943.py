# Generated by Django 3.0.7 on 2020-06-05 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20200605_1942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['position'], 'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
    ]
