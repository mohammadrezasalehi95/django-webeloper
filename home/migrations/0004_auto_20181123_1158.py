# Generated by Django 2.1.3 on 2018-11-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='home/static/Screenshot from 2018-11-23 14-44-25.png', upload_to='home/static/'),
        ),
    ]
