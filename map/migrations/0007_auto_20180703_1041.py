# Generated by Django 2.0.6 on 2018-07-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20180703_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='synopsis_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
