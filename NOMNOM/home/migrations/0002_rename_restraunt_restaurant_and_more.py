# Generated by Django 4.1.7 on 2023-04-14 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restraunt',
            new_name='Restaurant',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='RestrauntID',
            new_name='RestaurantID',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='RestrauntID',
            new_name='RestaurantID',
        ),
    ]
