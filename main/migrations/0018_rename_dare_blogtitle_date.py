# Generated by Django 4.1.3 on 2022-12-28 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_blogtitle_dare'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogtitle',
            old_name='dare',
            new_name='date',
        ),
    ]
