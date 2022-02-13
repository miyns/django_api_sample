# Generated by Django 4.0.2 on 2022-02-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flamingo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('is_freemium', models.BooleanField(default=False, verbose_name='freemium')),
                ('priority', models.IntegerField(verbose_name='priority')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Service',
                'db_table': 'services',
                'ordering': ['priority'],
            },
        ),
    ]