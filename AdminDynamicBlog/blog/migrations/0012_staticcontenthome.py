# Generated by Django 5.0.4 on 2024-08-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_seometa_description_alter_seometa_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticContentHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('content_p1', models.TextField()),
                ('content_p2', models.TextField()),
                ('youtube_url', models.CharField(max_length=255)),
                ('slider1', models.CharField(max_length=255)),
                ('slider1_p1', models.TextField()),
                ('slider1_p2', models.TextField()),
                ('slider2', models.CharField(max_length=255)),
                ('slider2_p1', models.TextField()),
                ('slider2_p2', models.TextField()),
                ('slider3', models.CharField(max_length=255)),
                ('slider3_p1', models.TextField()),
                ('slider3_p2', models.TextField()),
                ('slider4', models.CharField(max_length=255)),
                ('slider4_p1', models.TextField()),
                ('slider4_p2', models.TextField()),
                ('calltoaction', models.CharField(max_length=255)),
                ('calltoaction_p', models.TextField()),
            ],
        ),
    ]
