# Generated by Django 3.2.12 on 2023-09-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_lesson_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_link',
            field=models.CharField(blank=True, help_text='url для оплаты', max_length=150, null=True, verbose_name='url для оплаты'),
        ),
    ]
