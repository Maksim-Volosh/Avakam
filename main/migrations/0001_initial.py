# Generated by Django 4.2.15 on 2024-11-26 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('active', models.BooleanField(default=True)),
                ('field_type', models.CharField(choices=[('checkbox', 'Чекбоксы (множественный выбор)'), ('radio', 'Кнопки (один выбор)'), ('range', 'Диапазон (от-до)')], max_length=20)),
                ('options', models.TextField(help_text="Для 'checkbox' и 'radio' варианты через запятую. Для 'range' оставьте пустым.")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='main.category')),
            ],
        ),
    ]