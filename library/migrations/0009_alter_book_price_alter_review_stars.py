# Generated by Django 5.1.4 on 2025-01-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_book_options_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.CharField(choices=[('🌟', '🌟'), ('🌟🌟', '🌟🌟'), ('🌟🌟🌟', '🌟🌟🌟'), ('🌟🌟🌟🌟', '🌟🌟🌟🌟'), ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟')], max_length=5, verbose_name='Оценка'),
        ),
    ]
