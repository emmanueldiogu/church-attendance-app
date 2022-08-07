# Generated by Django 4.0.6 on 2022-07-19 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0004_remove_member_zone_zone_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='members',
        ),
        migrations.AddField(
            model_name='member',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='church.zone'),
        ),
    ]