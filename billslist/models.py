# from django.contrib.auth.models import User
from django.db import models

# For simplicity, no user model is linked to this Bill model
# Suppose this table is only for one customer just for now.


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
    # image = models.ImageField(upload_to='images/% Y/% m/% d/')
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True)
    # For simplicity, instead of using ImageField, TextField is used
    # placeholder.com is used for image url for now
    thumbnail_url = models.TextField(
        default='https://via.placeholder.com/80x120')
    original_url = models.TextField(
        default='https://via.placeholder.com/480x720')
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PROCESSING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=False)
    processed_at = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['created_at']

    def short_description(self):
        return str(self.description)[:50]
