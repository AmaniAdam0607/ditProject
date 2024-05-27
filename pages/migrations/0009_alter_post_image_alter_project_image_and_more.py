# Generated by Django 5.0.4 on 2024-05-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image1',
            field=models.FileField(default='default.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image2',
            field=models.FileField(default='default.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images'),
        ),
    ]
