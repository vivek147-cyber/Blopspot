# Generated by Django 3.0.8 on 2021-04-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210411_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(default='', upload_to='settings.MEDIA_ROOT'),
        ),
    ]