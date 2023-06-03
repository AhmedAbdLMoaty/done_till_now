# Generated by Django 4.2 on 2023-04-22 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_permission_role_role_id_role_role_role_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='Role_Role_ID',
            new_name='permission_has_role',
        ),
        migrations.RenameField(
            model_name='permission',
            old_name='Permission_ID',
            new_name='permission_id',
        ),
        migrations.RenameField(
            model_name='permission',
            old_name='Permission_Name',
            new_name='permission_name',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='Role_Role_ID',
            new_name='role_has_user',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='Role_id',
            new_name='role_id',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='Role_name',
            new_name='role_name',
        ),
    ]
