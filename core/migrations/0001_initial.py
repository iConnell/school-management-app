# Generated by Django 4.0.6 on 2022-07-11 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
