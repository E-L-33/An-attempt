# Generated by Django 2.1.4 on 2018-12-18 07:41

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180827_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]