# Generated by Django 4.0 on 2021-12-13 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='dni',
            field=models.CharField(default=0, max_length=8, unique=True),
            preserve_default=False,
        ),
    ]
