# Generated by Django 3.0.6 on 2020-05-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200515_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborate',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
