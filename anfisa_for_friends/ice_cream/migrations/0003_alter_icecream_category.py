# Generated by Django 3.2.16 on 2024-09-07 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20240907_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ice_creams', to='ice_cream.category', verbose_name='Категория'),
        ),
    ]
