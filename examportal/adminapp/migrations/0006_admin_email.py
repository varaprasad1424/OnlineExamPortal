# Generated by Django 4.2.5 on 2023-10-06 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_alter_faculty_email_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
