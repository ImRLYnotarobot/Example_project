# Generated by Django 2.2.3 on 2019-07-21 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('middle_name', models.CharField(blank=True, max_length=128)),
                ('birth_d', models.DateTimeField()),
                ('is_head', models.BooleanField(default=False)),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Group')),
            ],
        ),
    ]
