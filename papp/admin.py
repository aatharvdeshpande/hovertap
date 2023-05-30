from django.contrib import admin
from .models import *
# Register your models here.


class master_user_admin(admin.ModelAdmin):
    list_display = ['user_m_no', 'otp_status','user_name']

class master_img_admin(admin.ModelAdmin):
    list_display = ['img', 'img_name']

class master_transactions_admin(admin.ModelAdmin):
    list_display = ['user_id', 'img_id', 'status']


admin.site.register(master_user, master_user_admin)
admin.site.register(master_img, master_img_admin)
admin.site.register(master_transactions, master_transactions_admin)