# Generated by Django 3.0.7 on 2020-06-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20200605_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(db_index=True, verbose_name='Короткое описание'),
        ),
    ]
