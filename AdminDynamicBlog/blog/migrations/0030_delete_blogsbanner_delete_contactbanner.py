# Generated by Django 5.0.4 on 2024-08-08 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_blogsbanner_name_contactbanner_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogsBanner',
        ),
        migrations.DeleteModel(
            name='ContactBanner',
        ),
    ]
