# Generated by Django 3.2.9 on 2022-11-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AP_ID', models.IntegerField(unique=True)),
                ('adminName', models.CharField(max_length=50)),
                ('adminEmail', models.EmailField(max_length=254)),
                ('adminPassword', models.CharField(max_length=50)),
                ('loginStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('ClassRoom_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('course_year', models.CharField(max_length=50)),
                ('course_division', models.CharField(max_length=50)),
                ('course_subject', models.CharField(max_length=50)),
                ('file_csv_student', models.FileField(null=True, upload_to='')),
                ('file_csv_teacher', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=50)),
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CreateAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentPrn', models.IntegerField(unique=True)),
                ('studentName', models.CharField(max_length=50)),
                ('studentEmail', models.EmailField(max_length=254)),
                ('studentNumber', models.IntegerField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('division_id', models.IntegerField(primary_key=True, serialize=False)),
                ('division_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coures', models.CharField(max_length=50, null=True)),
                ('branch', models.CharField(max_length=50, null=True)),
                ('year', models.IntegerField(default=1, null=True)),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_account_file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherAccounts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('teacher_account_file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year_id', models.IntegerField(primary_key=True, serialize=False)),
                ('year_number', models.IntegerField(unique=True)),
            ],
        ),
    ]
