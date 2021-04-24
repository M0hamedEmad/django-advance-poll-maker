# Generated by Django 3.2 on 2021-04-21 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=500)),
                ('number_of_vote', models.IntegerField()),
                ('poll_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='poll.poll')),
            ],
        ),
    ]