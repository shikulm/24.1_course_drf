# Generated by Django 3.2.12 on 2023-09-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=1500, null=True, verbose_name='цена'),
        ),
    ]
