# Generated by Django 3.0.7 on 2020-07-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='platform',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
