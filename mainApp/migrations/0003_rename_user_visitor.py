# Generated by Django 4.0.5 on 2022-06-28 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_delete_university_course_available_seat_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Visitor',
        ),
    ]