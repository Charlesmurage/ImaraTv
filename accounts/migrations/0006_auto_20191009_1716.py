# Generated by Django 2.2.6 on 2019-10-09 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191009_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Counties'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='major_skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Major'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='minor_skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Minor'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='urban_centre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Urban'),
        ),
    ]
