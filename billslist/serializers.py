from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'description', 'thumbnail_url', 'original_url', 'amount',
                  'status', 'created_at', 'updated_at']
