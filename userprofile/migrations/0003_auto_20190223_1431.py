# Generated by Django 2.1.7 on 2019-02-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofileinfo_isheabitch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='nickname',
            field=models.CharField(max_length=200),
        ),
    ]
