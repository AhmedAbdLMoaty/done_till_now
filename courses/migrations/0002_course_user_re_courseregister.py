# Generated by Django 4.2 on 2023-04-26 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userroles_rolepermetion'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user_re',
            field=models.ManyToManyField(null=True, to='users.user'),
        ),
        migrations.CreateModel(
            name='CourseRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('user_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
