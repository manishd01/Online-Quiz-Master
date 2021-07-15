# Generated by Django 3.1.1 on 2021-06-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details_answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_selected', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='details_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('num_of_ques', models.PositiveIntegerField()),
                ('candidate_name', models.CharField(max_length=20)),
            ],
        ),
    ]
