# Generated by Django 3.1.3 on 2021-06-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_catogery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catogery',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
