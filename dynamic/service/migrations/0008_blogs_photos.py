# Generated by Django 5.0.6 on 2024-07-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_blogs_slugdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='Photos',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='blogs/'),
        ),
    ]
