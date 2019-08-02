# Generated by Django 2.2.3 on 2019-08-02 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20190722_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('CR', 'created'), ('CD', 'changed'), ('DL', 'deleted')], max_length=2)),
                ('model_name', models.CharField(max_length=127)),
                ('object_id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='headman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_d',
            field=models.DateField(verbose_name='Birth date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Group', verbose_name='Group'),
        ),
    ]