# Generated by Django 4.2.5 on 2023-10-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='firstname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='lastname',
            new_name='lname',
        ),
        migrations.AddField(
            model_name='member',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
