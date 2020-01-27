from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    cust_number = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)

class Repair(models.Model):
    repair_id = models.IntegerField(blank=True)
    cust_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='repairs')
    repair_item = models.CharField(max_length=100)
    repair_model = models.CharField(max_length=100)
    description = models.TextField()
    repair_charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.repair_id )

class Ticket(models.Model):
    cust_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='tickets')
    repair_id = models.ForeignKey(Repair, on_delete=models.CASCADE, related_name='item', default='repair_id', blank=True)
    setup_time = models.DateTimeField(
        default=timezone.now)
    Issue = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.repair_id )
