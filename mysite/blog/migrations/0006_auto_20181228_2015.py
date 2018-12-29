# Generated by Django 2.1.4 on 2018-12-28 20:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181220_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='blog_type',
            name='source_to',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Source_Type'),
            preserve_default=False,
        ),
    ]