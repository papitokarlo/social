# Generated by Django 4.2.3 on 2023-08-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('last_name', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=264, unique=True)),
                ('user_name', models.CharField(default='', max_length=128)),
            ],
        ),
    ]