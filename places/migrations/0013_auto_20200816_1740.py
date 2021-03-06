# Generated by Django 3.0.7 on 2020-08-16 17:40

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_auto_20200816_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Длинное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, db_index=True, verbose_name='Короткое описание'),
        ),
    ]
