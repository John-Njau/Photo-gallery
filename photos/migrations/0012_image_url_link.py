# Generated by Django 4.0.4 on 2022-05-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_rename_location_id_image_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='url_link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]