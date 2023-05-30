from django.db import models

# Create your models here.

class master_user(models.Model):
    user_m_no = models.CharField(unique = True, null = True, default = 00000)
    otp_status = models.BooleanField(default = False, null = True)
    user_name = models.CharField(max_length=25, default = "BAZINGA", null = True)

class master_img(models.Model):
    img = models.ImageField(upload_to = 'papp/images')
    img_name = models.CharField(max_length=25, default = "Error")

class master_transactions(models.Model):
    user_id = models.CharField()
    img_id = models.CharField()
    status = models.BooleanField(default = False)