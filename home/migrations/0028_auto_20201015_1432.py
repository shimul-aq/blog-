# Generated by Django 3.1.1 on 2020-10-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_post_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
