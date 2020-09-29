# from django.contrib.auth.models import User
from django.db import models

# For simplicity, no user model is linked to this Bill model
# Suppose this table is only for one customer for now.


class Bill(models.Model):
    # status choices are defined as follows
    PROCESSING = 'PR'
    SCHEDULED = 'SC'
    UNABLE_TO_PAY = 'UN'
    PAID = 'PA'
    STATUS_CHOICES = [
        (PROCESSING, 'Processing'),
        (SCHEDULED, 'Scheduled'),
        (UNABLE_TO_PAY, 'Unable to Pay'),
        (PAID, 'Paid'),
    ]

    # customer = models.ForeignKey(
    #     User, related_name='customer', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/% Y/% m/% d/')
    amount = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PROCESSING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
