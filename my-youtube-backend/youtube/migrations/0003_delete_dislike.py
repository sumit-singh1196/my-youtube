# Generated by Django 3.2.8 on 2021-11-09 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_comment_dislike_like_video_view'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DisLike',
        ),
    ]