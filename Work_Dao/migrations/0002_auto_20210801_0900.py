# Generated by Django 3.2.2 on 2021-08-01 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles_app', '0002_alter_userprofile_user'),
        ('Work_Dao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advise',
            name='hander',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Advise_hander_UserProfile', to='UserProfiles_app.userprofile', unique=True, verbose_name='处理人'),
        ),
        migrations.AlterField(
            model_name='advise',
            name='proposer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposer_UserProfile', to='UserProfiles_app.userprofile', unique=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicant_UserProfile', to='UserProfiles_app.userprofile', unique=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='hander',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Apply_hander_UserProfile', to='UserProfiles_app.userprofile', unique=True),
        ),
        migrations.AlterField(
            model_name='task_list',
            name='Distributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Distributor_UserProfile', to='UserProfiles_app.userprofile', unique=True, verbose_name='分配人'),
        ),
        migrations.AlterField(
            model_name='task_list',
            name='people_work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='people_work_UserProfile', to='UserProfiles_app.userprofile', unique=True, verbose_name='指定员工'),
        ),
    ]
