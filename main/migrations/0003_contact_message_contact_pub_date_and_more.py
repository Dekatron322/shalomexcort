# Generated by Django 4.2.6 on 2023-10-07 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_topic_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default='', max_length=1130, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.TextField(default='', max_length=1000000),
        ),
    ]