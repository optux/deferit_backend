from rest_framework import serializers
from .models import Bill

# Use DRF ChoiceField to return human readable value


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)

# Bill model serializer
# status will be returned as a human readable value


class BillSerializer(serializers.ModelSerializer):
    status = ChoiceField(choices=Bill.STATUS_CHOICES)

    class Meta:
        model = Bill
        fields = ['id', 'description', 'thumbnail_url', 'original_url', 'amount',
                  'status', 'created_at', 'updated_at']
