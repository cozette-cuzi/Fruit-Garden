from .models import RoundEntry, OrderRound
from django.core.exceptions import BadRequest
from django.db import models
from .serializers import OrderRoundSerializer


def generate_relationships(entries, object, max):
    allEmpty = True
    for entry_data in entries:
        number = entry_data["number"]
        if number is None:
            continue
        elif number > max or number < 0:
            raise BadRequest()
        allEmpty = False
        object.entries.add(
            entry_data["fruit_id"],
            through_defaults={"number": number},
        )
    if allEmpty:
        raise BadRequest()


def fulfill_order(order):
    order_entries = order.order_entries.all()
    finished = True
    for order_entry in order_entries:
        round_entries = RoundEntry.objects.filter(
            fruit_id=order_entry.fruit_id, number__gt=0
        )
        for round_entry in round_entries:
            order.status = "collecting"
            order.save()
            fulfill = min(round_entry.number, order_entry.number)
            if fulfill == 0:
                break
            round_entry.number -= fulfill
            order_entry.number -= fulfill
            round_entry.save()
            order_entry.save()
            OrderRound.objects.create(
                order_entry_id=order_entry, round_entry_id=round_entry, number=fulfill
            )

        if order_entry.number > 0:
            finished = False

    if finished:
        order.status = "done"
        order.save()


def get_fruit_details(order):
    order_entries = order.order_entries.all()
    result = []
    for entry in order_entries:
        collected = entry.order_round_entries.aggregate(collected=models.Sum("number"))[
            "collected"
        ]
        result.append(
            {
                "name": entry.fruit_id.name,
                "collected": collected if collected != None else 0,
                "rest": entry.number,
            }
        )
    return result


def get_round_details(order):
    order_entries = order.order_entries.all()
    order_rounds = OrderRound.objects.filter(order_entry_id__in=order_entries)
    return OrderRoundSerializer(order_rounds, many=True).data
