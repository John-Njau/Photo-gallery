# Generated by Django 4.0.4 on 2022-05-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='photos/static/uploads/'),
        ),
    ]
