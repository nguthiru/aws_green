# Generated by Django 3.2 on 2022-10-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20221021_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recyclecall',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]
