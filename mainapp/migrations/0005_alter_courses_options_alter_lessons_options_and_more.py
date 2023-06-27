# Generated by Django 4.1.1 on 2022-10-07 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_courses_lessons_teachers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
    ]
