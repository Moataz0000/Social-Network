# Generated by Django 5.1.4 on 2024-12-21 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created']},
        ),
    ]