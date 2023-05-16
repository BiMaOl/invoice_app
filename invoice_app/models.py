from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.EmailField()
    billing_address = models.TextField()
        
class Contact(models.Model):
    CUST = "customer"
    EMPL = "employee"
    TYPES = [(CUST, "customer"), (EMPL, "employee")]
    account_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    home_address = models.TextField
    type = models.CharField(max_length=32, choices=TYPES, default=CUST)

class Vehicle(models.Model):
    name = models.TextField
    vin = models.CharField
    account_name = models.ForeignKey(Account, on_delete=models.RESTRICT)

class Invoice(models.Model):
    billing_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField

class InvoiceLine(models.Model):
    invoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    line_amount = models.PositiveBigIntegerField
    discount  = models.IntegerField
    tax = models.IntegerField
    operation= models.TextField