# Generated by Django 3.0.7 on 2020-06-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20200603_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='position',
            field=models.IntegerField(blank=True, null=True, verbose_name='Позиция'),
        ),
    ]
