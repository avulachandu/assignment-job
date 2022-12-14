# Generated by Django 3.2 on 2022-12-05 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_productioncolour_productionimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productioncolour',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
        migrations.AlterField(
            model_name='productionimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.productioncolour'),
        ),
    ]
