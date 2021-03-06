from django.db import models

# abstract class inherited by state & federal brackets
class Brackets(models.Model):
    greater_than = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    last_bkt = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    init_tax = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    new_rate = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    class Meta:
        abstract = True

class State(Brackets):
    state_id = models.CharField(primary_key=True, max_length=10)

class Federal(Brackets):
    federal_id = models.CharField(primary_key=True, max_length=10)
# Create your models here.

class UserInfo(models.Model):
    SINGLE_OR_MARRIED = (
        ('single', 'single'),
        ('married', 'married'),
    )

    salary = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    marital_status = models.CharField(max_length=7, choices=SINGLE_OR_MARRIED)
    zip_code = models.CharField(max_length=6, default='10016')
