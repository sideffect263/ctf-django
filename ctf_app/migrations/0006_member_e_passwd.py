# Generated by Django 4.2.7 on 2023-11-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_app', '0005_levelspassed_level4'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='e_passwd',
            field=models.CharField(default='password_testing', max_length=50, verbose_name=''),
            preserve_default=False,
        ),
    ]
