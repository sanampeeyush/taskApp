from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner_info = models.TextField()
    employee_size = models.PositiveIntegerField()
    summary = models.TextField()
    headquarters_location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    founded_date = models.DateField()
    founders = models.CharField(max_length=255)
    operating_status = models.BooleanField(default=True)
    last_funding_type = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    stock_symbol = models.CharField(max_length=255)
    company_type = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name