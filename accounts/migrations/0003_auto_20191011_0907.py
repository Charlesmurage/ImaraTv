# Generated by Django 2.2.6 on 2019-10-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191011_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='invite_reason',
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
