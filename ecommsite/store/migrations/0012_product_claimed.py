# Generated by Django 3.2.5 on 2021-09-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210911_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='claimed',
            field=models.BooleanField(default=True),
        ),
    ]
