# Generated by Django 3.0.8 on 2021-04-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
