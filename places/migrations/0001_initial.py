# Generated by Django 3.0.7 on 2020-06-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='Название')),
                ('description_short', models.TextField(db_index=True, verbose_name='Короткое описание')),
                ('description_long', models.TextField(db_index=True, verbose_name='Длинное описание')),
                ('lat', models.CharField(db_index=True, max_length=50, verbose_name='Широта')),
                ('lng', models.CharField(db_index=True, max_length=50, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
    ]
