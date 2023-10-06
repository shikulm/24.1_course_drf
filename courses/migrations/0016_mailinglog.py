# Generated by Django 3.2.12 on 2023-09-20 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0015_auto_20230919_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_mailing', models.DateTimeField(auto_now_add=True, verbose_name='дата и время рассылки')),
                ('last_update', models.DateTimeField(blank=True, null=True, verbose_name='дата обновления курса')),
                ('status', models.CharField(choices=[('ok', 'Успешно'), ('fail', 'Ошибка')], default='ok', max_length=150, verbose_name='статус')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailing_log', to='courses.course', verbose_name='курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailing_log', to=settings.AUTH_USER_MODEL, verbose_name='покупатель')),
            ],
            options={
                'verbose_name': 'Запись журнала рассылки',
                'verbose_name_plural': 'Журнал рассылок',
                'ordering': ['-datetime_mailing'],
            },
        ),
    ]
