# Generated by Django 3.2 on 2021-05-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_taskf_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('len_of_words', models.CharField(max_length=200)),
                ('len_of_sentence', models.CharField(max_length=200)),
                ('num_of_prep', models.CharField(max_length=200)),
                ('part_of_speech', models.CharField(max_length=200)),
            ],
        ),
    ]