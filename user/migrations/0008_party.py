# Generated by Django 5.1.3 on 2025-01-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_gimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pryimg', models.CharField(max_length=10)),
                ('pryname', models.CharField(max_length=30)),
                ('pryamount', models.CharField(max_length=30)),
                ('pryabout', models.CharField(max_length=2000)),
            ],
        ),
    ]
