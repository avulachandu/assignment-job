# Generated by Django 3.2 on 2022-12-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productioncolour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField()),
                ('image', models.CharField(choices=[('r', 'red'), ('b', 'blue'), ('g', 'green'), ('b', 'black')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Productionimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
