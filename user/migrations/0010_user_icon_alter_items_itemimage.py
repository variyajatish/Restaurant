# Generated by Django 5.1.3 on 2025-01-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_items_itemimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='itemimage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
