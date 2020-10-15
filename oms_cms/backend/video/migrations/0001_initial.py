# Generated by Django 2.2.4 on 2019-08-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('link', models.CharField(max_length=1500, verbose_name='Ссылка')),
                ('slug', models.SlugField(max_length=500, unique=True, verbose_name='slug')),
                ('video_id', models.CharField(default='', max_length=1500, verbose_name='Id видео')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Превью')),
                ('duration', models.IntegerField(default=0, verbose_name='Продолжительность')),
                ('url', models.CharField(default='', max_length=1000, verbose_name='Сгенерированная ссылка')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
