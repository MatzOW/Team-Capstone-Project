# Generated by Django 4.0 on 2022-01-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnrolmentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(verbose_name=6),
        ),
    ]