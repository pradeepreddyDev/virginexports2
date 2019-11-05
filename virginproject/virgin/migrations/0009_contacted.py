# Generated by Django 2.2.6 on 2019-11-01 03:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virgin', '0008_auto_20191020_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'contacted',
                'verbose_name_plural': 'contacted',
                'db_table': 'contacted',
            },
        ),
    ]