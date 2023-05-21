# Generated by Django 4.2 on 2023-05-21 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_permission_permission_name_and_more'),
        ('freelance', '0002_alter_job_descriotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_descriotion', models.CharField(max_length=1000)),
                ('image_urls', models.CharField(max_length=1000)),
                ('audio_urls', models.CharField(max_length=1000)),
                ('videos_urls', models.CharField(max_length=1000)),
                ('attachements_urls', models.CharField(max_length=1000)),
                ('project_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]