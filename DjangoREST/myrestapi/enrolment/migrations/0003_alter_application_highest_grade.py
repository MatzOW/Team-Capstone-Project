# Generated by Django 4.0 on 2022-01-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolment', '0002_rename_cet_scorecard_application_matric_certificate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='highest_grade',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
