from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from .models import Bill
from .serializers import BillSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# @permission_classes((IsAuthenticated,))
class BillsList(generics.ListAPIView):
    serializer_class = BillSerializer
    pagination_class = StandardResultsSetPagination

    # the queryset should be based on each customer using filter
    # omitted for now.
    def get_queryset(self):
        return Bill.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
