# Generated by Django 2.1.2 on 2018-10-22 22:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='date_added',
        ),
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]