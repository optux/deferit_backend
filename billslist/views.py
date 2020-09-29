from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from .models import Bill
from .serializers import BillSerializer


# @permission_classes((IsAuthenticated,))
class BillsList(generics.ListAPIView):
    serializer_class = BillSerializer

    # the queryset should be based on each customer
    # omitted for now.
    def get_queryset(self):
        return Bill.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
