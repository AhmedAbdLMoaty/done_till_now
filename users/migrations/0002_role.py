# Generated by Django 4.2 on 2023-04-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('Role_id', models.AutoField(primary_key=True, serialize=False)),
                ('Role_name', models.CharField(max_length=45)),
            ],
        ),
    ]
