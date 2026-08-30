from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

from .models import (
    Category,
    Product,
    Order,
    OrderItem,
    Address
)

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer,
    AddressSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrderItem.objects.filter(
            order__user=self.request.user
        )


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


# ---------------------------------------------

from rest_framework.decorators import (
    api_view,
    permission_classes
)

from rest_framework.response import Response
from rest_framework import status

from .services import consultar_cep

from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def cep_view(request, cep):

    resultado = consultar_cep(cep)

    if resultado is None:
        return Response(
            {
                'detail': 'CEP inválido.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(
        resultado,
        status=status.HTTP_200_OK
    )


def home(request):
    return render(request, 'index.html')