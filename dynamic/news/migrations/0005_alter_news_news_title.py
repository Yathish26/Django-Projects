# Generated by Django 5.0.6 on 2024-07-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=100),
        ),
    ]
