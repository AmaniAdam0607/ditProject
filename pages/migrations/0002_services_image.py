# Generated by Django 5.0.4 on 2024-05-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.FileField(default='default.jpeg', upload_to='images'),
        ),
    ]
