from django.contrib import admin

from .models import Customer, Repair, Ticket

class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_number', 'cust_name','address','phone_number' )
    list_filter = ( 'cust_number','cust_name', 'address')
    search_fields = ('cust_name', )
    ordering = ['cust_name']

admin.site.register(Customer, CustomerList)


class RepairList(admin.ModelAdmin):
    list_display = ( 'repair_id', 'cust_name','repair_item','repair_model' )
    list_filter = ( 'repair_id','cust_name', 'repair_item')
    search_fields = ('repair_id', )
    ordering = ['cust_name']

admin.site.register(Repair, RepairList)


class TicketsList(admin.ModelAdmin):
    list_display = ( 'repair_id', 'cust_name','Issue','severity','setup_time' )
    list_filter = ( 'repair_id','cust_name', 'Issue')
    search_fields = ('repair_id', )
    ordering = ['cust_name']

admin.site.register(Ticket, TicketsList)
