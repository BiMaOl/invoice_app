from django.contrib import admin

# Register your models here.
from invoice_app.models import Contact, Vehicle, Invoice, InvoiceLine
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(InvoiceLine)
class InvoiceLineAdmin(admin.ModelAdmin):
    pass
