# Generated by Django 5.1.3 on 2024-12-31 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_image_items_itemimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=3000)),
                ('chefname', models.CharField(max_length=30)),
                ('postion', models.CharField(max_length=30)),
                ('chefimage', models.CharField(max_length=20)),
            ],
        ),
    ]
