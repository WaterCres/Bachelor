# Generated by Django 4.1.7 on 2023-02-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_alter_group_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='stds_pr_Team',
            new_name='cap_max',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='teams_max',
            new_name='cap_min',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='teams_min',
        ),
        migrations.AddField(
            model_name='topic',
            name='inst_short',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='topic',
            name='institute',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='topic',
            name='requirements',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]