# Generated by Django 3.2.5 on 2021-09-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_product_claimed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
    ]
