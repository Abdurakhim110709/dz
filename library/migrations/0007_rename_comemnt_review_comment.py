# Generated by Django 5.1.4 on 2025-01-24 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_book_video_id_alter_book_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comemnt',
            new_name='comment',
        ),
    ]
