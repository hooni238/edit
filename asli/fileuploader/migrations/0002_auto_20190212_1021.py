# Generated by Django 2.1.5 on 2019-02-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic',
            name='shar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pic',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]