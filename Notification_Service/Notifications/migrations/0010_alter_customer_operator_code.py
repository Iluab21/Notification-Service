# Generated by Django 4.1.1 on 2022-09-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0009_alter_customer_operator_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='operator_code',
            field=models.CharField(editable=False, max_length=3),
        ),
    ]
