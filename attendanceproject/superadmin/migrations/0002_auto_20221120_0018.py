# Generated by Django 3.2.9 on 2022-11-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('ClassRoom_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('course_year', models.CharField(max_length=50)),
                ('course_division', models.CharField(max_length=50)),
                ('course_subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='division',
            name='division_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='year',
            name='year_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]