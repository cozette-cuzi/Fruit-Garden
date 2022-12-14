from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Fruit(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    DONE = "done"
    COLLECTING = "collecting"
    NEW = "new"
    CHOICES = [
        (DONE, DONE),
        (COLLECTING, COLLECTING),
        (NEW, NEW),
    ]
    status = models.CharField(max_length=16, choices=CHOICES, default=NEW)
    created = models.DateTimeField(auto_now_add=True)
    entries = models.ManyToManyField(
        Fruit, through="OrderEntry", related_name="order_entries", default=None
    )
    @property
    def rest(self):
        qs = self.entries.through.objects.filter(order_id=self).aggregate(rest=models.Sum('number'))
        return qs['rest']
    @property
    def collected(self):
        entries = self.entries.through.objects.filter(order_id=self)
        sum = 0
        for entry in entries:
            qs = entry.order_round_entries.aggregate(collected=models.Sum('number'))
            if(qs['collected']): sum += qs['collected']
        return sum


class Round(models.Model):
    done = models.BooleanField(default=False)
    entries = models.ManyToManyField(
        Fruit, related_name="round_entries", through="RoundEntry"
    )


class OrderEntry(models.Model):
    order_id = models.ForeignKey(
        Order,
        db_column="order_id",
        related_name="order_entries",
        on_delete=models.CASCADE,
    )
    fruit_id = models.ForeignKey(Fruit, db_column="fruit_id", on_delete=models.CASCADE)
    number = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], default=0
    )


class RoundEntry(models.Model):
    round_id = models.ForeignKey(
        Round,
        db_column="round_id",
        related_name="round_entries",
        on_delete=models.CASCADE,
    )
    fruit_id = models.ForeignKey(Fruit, db_column="fruit_id", on_delete=models.CASCADE)
    number = models.IntegerField(
        validators=[MaxValueValidator(50), MinValueValidator(0)], default=0
    )


class OrderRound(models.Model):
    order_entry_id = models.ForeignKey(
        OrderEntry,
        related_name="order_round_entries",
        db_column="order_entry_id",
        on_delete=models.CASCADE,
    )
    round_entry_id = models.ForeignKey(
        RoundEntry,
        related_name="order_round_entries",
        db_column="round_entry_id",
        on_delete=models.CASCADE,
    )
    number = models.IntegerField()
