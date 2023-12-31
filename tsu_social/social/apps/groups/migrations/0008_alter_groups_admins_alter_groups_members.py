# Generated by Django 4.2.4 on 2023-08-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_users_user_alter_user_table'),
        ('groups', '0007_alter_groups_admins_alter_groups_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='groups_admin', to='user.user'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='groups_member', to='user.user'),
        ),
    ]
