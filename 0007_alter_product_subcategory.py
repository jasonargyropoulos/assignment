# Generated by Django 4.0.4 on 2022-07-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_subcategory_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='uncatogrized', max_length=255),
        ),
    ]
