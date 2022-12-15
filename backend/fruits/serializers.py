from rest_framework import serializers
from .models import Order
from .models import OrderEntry
from .models import Round
from .models import RoundEntry
from .models import OrderRound
from .models import Fruit
from rest_framework.validators import *


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ["id", "name"]


class OrderEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderEntry
        fields = ["id", "fruit_id", "number"]


class OrderSerializer(serializers.ModelSerializer):
    order_entries = OrderEntrySerializer(many=True, read_only=True)
    created = serializers.DateTimeField(format="%Y.%m.%d %H:%M", read_only=True)
    class Meta:
        model = Order
        fields = ["id", "status", "created", "order_entries", "rest", "collected"]

    # def create(self, validated_data):
    #     order_entries_data = validated_data.pop('order_entries')
    #     order = Order.objects.create(**validated_data)
    #     for order_entry_data in order_entries_data:
    #         print(order_entry_data)
    #         OrderEntry.objects.create(order_id=order, **order_entry_data)
    #     return order


class RoundEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundEntry
        fields = ["id", "fruit_id", "number"]


class RoundSerializer(serializers.ModelSerializer):
    round_entries = RoundEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Round
        fields = ["id", "done", "round_entries"]


class OrderRoundSerializer(serializers.ModelSerializer):
    fruit = FruitSerializer(read_only=True, source="order_entry_id.fruit_id")
    class Meta:
        model = OrderRound
        fields =  ["id", "number", "fruit"]