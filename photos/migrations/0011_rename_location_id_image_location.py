# Generated by Django 4.0.4 on 2022-05-28 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_remove_image_location_image_location_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='location_id',
            new_name='location',
        ),
    ]
