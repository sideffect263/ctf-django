# Generated by Django 4.2.7 on 2023-12-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_app', '0008_levelspassed_level5'),
    ]

    operations = [
        migrations.AddField(
            model_name='levelspassed',
            name='level6',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='levelspassed',
            name='level7',
            field=models.CharField(default='', max_length=50),
        ),
    ]
