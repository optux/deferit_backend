from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['customer', 'image', 'amount',
                  'status', 'created_at', 'updated_at']
