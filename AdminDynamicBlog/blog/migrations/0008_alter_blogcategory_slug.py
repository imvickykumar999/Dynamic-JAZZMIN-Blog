# Generated by Django 5.0.4 on 2024-08-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]