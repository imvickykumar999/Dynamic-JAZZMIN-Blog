# Generated by Django 5.0.4 on 2024-08-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_remove_calltoaction_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsbanner',
            name='name',
            field=models.CharField(default='Blogs Banner', max_length=255),
        ),
        migrations.AddField(
            model_name='contactbanner',
            name='name',
            field=models.CharField(default='Contact Banner', max_length=255),
        ),
    ]
