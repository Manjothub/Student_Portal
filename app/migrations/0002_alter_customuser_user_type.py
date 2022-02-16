# Generated by Django 4.0.2 on 2022-02-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'STAFF'), (1, 'HOD'), (3, 'STUDENT')], default=1, max_length=50),
        ),
    ]
