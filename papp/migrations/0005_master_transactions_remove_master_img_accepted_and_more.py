# Generated by Django 4.2.1 on 2023-05-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("papp", "0004_alter_master_user_user_m_no"),
    ]

    operations = [
        migrations.CreateModel(
            name="master_transactions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.CharField()),
                ("img_id", models.CharField()),
                ("status", models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name="master_img",
            name="accepted",
        ),
        migrations.RemoveField(
            model_name="master_img",
            name="rejected",
        ),
        migrations.AddField(
            model_name="master_img",
            name="img_name",
            field=models.CharField(default="Error", max_length=25),
        ),
    ]
