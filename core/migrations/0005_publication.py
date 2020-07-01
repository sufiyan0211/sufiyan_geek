# Generated by Django 3.0.7 on 2020-07-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200701_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]