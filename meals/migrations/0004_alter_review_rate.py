# Generated by Django 4.2.5 on 2023-10-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_remove_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=2),
        ),
    ]