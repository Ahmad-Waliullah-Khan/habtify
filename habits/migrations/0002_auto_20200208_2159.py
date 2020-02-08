# Generated by Django 3.0.3 on 2020-02-08 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='created_at',
            new_name='started_at',
        ),
        migrations.RenameField(
            model_name='tracker',
            old_name='created_at',
            new_name='started_at',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='title',
        ),
        migrations.AddField(
            model_name='habit',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tracker',
            name='description',
            field=models.TextField(),
        ),
    ]
