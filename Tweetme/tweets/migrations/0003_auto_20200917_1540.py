# Generated by Django 3.1.1 on 2020-09-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20200917_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140),
        ),
    ]
