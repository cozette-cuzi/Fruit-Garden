from django.shortcuts import render
from .serializers import (
    OrderSerializer,
    OrderEntrySerializer,
    RoundSerializer,
    RoundEntrySerializer,
)
from .models import Order, Round, RoundEntry, OrderEntry, OrderRound, Fruit
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError, transaction
from django.core.exceptions import BadRequest
from .view_helpers import *

class OrderList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        order_entries_data = request.data.pop("order_entries")
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    saved = serializer.save()
                    order = Order.objects.get(pk=saved.id)
                    generate_relationships(order_entries_data, order, 100)
                    fulfill_order(order)
                    return Response(
                        serializer.data,
                        status=status.HTTP_201_CREATED,
                    )
            except BadRequest:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoundList(APIView):
    def get(self, request, format=None):
        rounds = Round.objects.all()
        serializer = OrderSerializer(rounds, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def post(self, request, format=None):
        round_entries_data = request.data.pop("round_entries")
        serializer = RoundSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    saved = serializer.save()
                    round = Order.objects.get(pk=saved.id)
                    generate_relationships(round_entries_data, round, 50)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except BadRequest:
                return Response(exception=BadRequest, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
