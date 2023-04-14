# Generated by Django 4.1.7 on 2023-04-14 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restraunt',
            fields=[
                ('RestrauntID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Rating', models.FloatField(default=0)),
                ('NumRatings', models.IntegerField()),
                ('Description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Rating', models.FloatField(default=0)),
                ('NumRatings', models.IntegerField()),
                ('Description', models.CharField(max_length=200)),
                ('Price', models.FloatField()),
                ('Calories', models.IntegerField()),
                ('RestrauntID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.restraunt')),
            ],
        ),
    ]