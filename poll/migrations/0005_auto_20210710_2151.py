# Generated by Django 3.2.4 on 2021-07-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20210705_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='hide_results',
            field=models.BooleanField(choices=[(True, 'Hide Results'), (False, 'Publish Results')], default=False),
        ),
        migrations.AlterField(
            model_name='poll',
            name='multiple_answers',
            field=models.BooleanField(choices=[(True, 'Select Multiple Answers'), (False, 'Select One Answer')], default=False),
        ),
        migrations.AlterField(
            model_name='poll',
            name='status',
            field=models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=True),
        ),
    ]
