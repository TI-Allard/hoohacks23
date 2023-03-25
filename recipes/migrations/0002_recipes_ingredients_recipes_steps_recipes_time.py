# Generated by Django 4.1.7 on 2023-03-25 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipes',
            name='steps',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipes',
            name='time',
            field=models.CharField(default='', max_length=20),
        ),
    ]
