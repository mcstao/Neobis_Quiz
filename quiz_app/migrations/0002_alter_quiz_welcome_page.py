# Generated by Django 4.2.9 on 2024-01-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='welcome_page',
            field=models.TextField(default='Добро пожаловать на квиз по'),
        ),
    ]