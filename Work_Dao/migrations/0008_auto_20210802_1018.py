# Generated by Django 3.2.2 on 2021-08-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Dao', '0007_note_modify_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-create_time'], 'verbose_name': ('便签',), 'verbose_name_plural': '便签'},
        ),
        migrations.AlterField(
            model_name='task_list',
            name='status',
            field=models.CharField(choices=[('已完成', '已完成'), ('未处理', '未处理'), ('转接', '转接')], default='未处理', max_length=20, verbose_name='完成状态'),
        ),
    ]
