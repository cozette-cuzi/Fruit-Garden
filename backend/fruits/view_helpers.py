from .models import  Order, RoundEntry, OrderEntry, OrderRound
from django.core.exceptions import BadRequest


def generate_relationships(entries, object, max):
    for entry_data in entries:
        number = entry_data["number"]
        if(number == None):
            continue
        elif number > max:
            raise BadRequest()
        object.entries.add(
            entry_data["fruit_id"],
            through_defaults={"number": number},
        )

def fulfill_order(order):
    order_entries = OrderEntry.objects.filter(order_id=order)
    finished = True
    for order_entry in order_entries:
        round_entries = RoundEntry.objects.filter(fruit_id=order_entry.fruit_id, number__gt=0)
        for round_entry in round_entries:
            order.status = "collecting"
            order.save()
            fulfill = min(round_entry.number, order_entry.number)
            if(fulfill == 0): break
            round_entry.number -= fulfill
            order_entry.number -= fulfill
            round_entry.save()
            order_entry.save()
            OrderRound.objects.create(order_entry_id=order_entry, round_entry_id=round_entry, number=fulfill)

        if order_entry.number > 0: 
            finished = False
        
    if finished:
        order.status = "done"
        order.save()

