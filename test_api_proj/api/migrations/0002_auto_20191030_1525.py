# Generated by Django 2.2.6 on 2019-10-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patexdata',
            name='security_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patexdata',
            name='tech_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]