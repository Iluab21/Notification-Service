# Generated by Django 4.1.1 on 2022-09-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0013_alter_distribution_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sended_status',
            field=models.CharField(default=False, max_length=255),
        ),
    ]
