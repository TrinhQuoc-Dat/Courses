# Generated by Django 5.1.6 on 2025-03-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='tags',
            field=models.ManyToManyField(to='courses.tag'),
        ),
    ]
