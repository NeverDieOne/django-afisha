# Generated by Django 3.0.7 on 2020-06-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20200605_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='position',
            field=models.IntegerField(default=1, verbose_name='Позиция'),
            preserve_default=False,
        ),
    ]
