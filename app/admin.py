from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer,
    Branch,
    Home,
    Office,
    Loan,
    Excel,
)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'father_name', 'profile', 'loan_acc_no']

@admin.register(Branch)
class BranchModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'customer', 'zone_name', 'region_name', 'branch_name', 'branch_code']

@admin.register(Home)
class HomeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'customer', 'add_1', 'add_2', 'add_3', 'home_code', 'landmark']

@admin.register(Office)
class OfficeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'customer', 'add_1', 'add_2', 'add_3', 'off_code', 'landmark']

@admin.register(Loan)
class LoanModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'customer', 'agr_date', 'lrn', 'tenor', 'adv_emi', 'mob']

@admin.register(Excel)
class ExcelModelAdmin(admin.ModelAdmin):
 list_display = ['file']



# def customer_info(self, obj):
#   link = reverse("admin:app_customer_change", args=[obj.customer.pk])
#   return format_html('<a href="{}">{}</a>', link, obj.customer.name)
 
