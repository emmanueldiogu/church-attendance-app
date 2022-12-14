# Generated by Django 4.0.6 on 2022-07-19 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('other_names', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('membership_date', models.DateField(blank=True, null=True)),
                ('tally_no', models.IntegerField()),
                ('photo', models.ImageField(upload_to='church/members/images/')),
                ('is_elder', models.BooleanField(default=False)),
                ('is_deacon', models.BooleanField(default=False)),
                ('is_preacher', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='leader', to='church.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='ministry',
            field=models.ManyToManyField(related_name='ministries', to='church.ministry'),
        ),
        migrations.AddField(
            model_name='member',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='church.zone'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='church.member')),
            ],
            options={
                'unique_together': {('date', 'member_id')},
            },
        ),
    ]
