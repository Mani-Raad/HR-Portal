# Generated by Django 5.0.7 on 2024-08-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_document_leave_payroll_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('preferred_contact', models.CharField(max_length=50)),
                ('contact_details', models.CharField(max_length=255)),
                ('incident_date', models.DateField()),
                ('incident_time', models.TimeField(blank=True, null=True)),
                ('incident_description', models.TextField()),
                ('harasser_name', models.CharField(max_length=255)),
                ('harasser_role', models.CharField(blank=True, max_length=255)),
                ('harasser_department', models.CharField(blank=True, max_length=255)),
                ('witness_name', models.CharField(blank=True, max_length=255)),
                ('evidence', models.FileField(blank=True, upload_to='evidence/')),
            ],
        ),
    ]
