# Generated by Django 5.0.3 on 2024-03-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_blog',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
