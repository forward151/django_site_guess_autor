# Generated by Django 3.2 on 2021-05-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210508_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskmodel2',
            options={},
        ),
        migrations.RenameField(
            model_name='taskmodel2',
            old_name='task',
            new_name='taskx',
        ),
        migrations.AlterField(
            model_name='taskf',
            name='task_1',
            field=models.FileField(upload_to=''),
        ),
    ]