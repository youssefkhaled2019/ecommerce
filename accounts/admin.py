from django.contrib import admin
from .models import Account
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
#     list_display=[]
#     # search_fields=[]
