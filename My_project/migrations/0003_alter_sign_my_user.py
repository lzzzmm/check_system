# Generated by Django 3.2.2 on 2021-08-01 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles_app', '0003_alter_userprofile_user'),
        ('My_project', '0002_alter_sign_my_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='my_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserProfiles_app.userprofile', verbose_name='签到人'),
        ),
    ]
