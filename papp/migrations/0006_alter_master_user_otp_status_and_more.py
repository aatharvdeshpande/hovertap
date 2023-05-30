# Generated by Django 4.2.1 on 2023-05-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("papp", "0005_master_transactions_remove_master_img_accepted_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="master_user",
            name="otp_status",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="master_user",
            name="user_m_no",
            field=models.CharField(default=0, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="master_user",
            name="user_name",
            field=models.CharField(default="BAZINGA", max_length=25, null=True),
        ),
    ]