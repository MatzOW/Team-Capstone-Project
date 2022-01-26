# Generated by Django 4.0 on 2022-01-26 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=200)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrolment.notice')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('Computer Science Engineering', 'Computer Science Engineering'), ('Information Technology Engineering', 'Information Technology Engineering'), ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'), ('Electronics Engineering', 'Electronics Engineering')], max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('student_profile', models.ImageField(upload_to='images')),
                ('ssc_percentage', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('ssc_marksheet', models.ImageField(null=True, upload_to='images')),
                ('ssc_passing_certificate', models.ImageField(null=True, upload_to='images')),
                ('ssc_leaving_certificate', models.ImageField(null=True, upload_to='images')),
                ('hsc_percentage', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('hsc_marksheet', models.ImageField(null=True, upload_to='images')),
                ('hsc_passing_certificate', models.ImageField(null=True, upload_to='images')),
                ('hsc_leaving_certificate', models.ImageField(null=True, upload_to='images')),
                ('cet_percentile', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('cet_scorecard', models.ImageField(null=True, upload_to='images')),
                ('jee_percentile', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('jee_scorecard', models.ImageField(null=True, upload_to='images')),
                ('Application_Status', models.TextField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('message', models.TextField(default='', max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
