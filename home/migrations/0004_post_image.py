# Generated by Django 3.1.1 on 2020-10-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='static/default.jpg', upload_to=''),
        ),
    ]
