# Generated by Django 3.0.7 on 2024-05-18 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
