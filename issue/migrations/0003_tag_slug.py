# Generated by Django 4.1.2 on 2022-10-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_tag_task_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.CharField(max_length=50, null=True, verbose_name='Слаг'),
        ),
    ]
