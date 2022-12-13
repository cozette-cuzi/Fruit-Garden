from django.contrib import admin
from .models import Order
from .models import OrderEntry
from .models import Round
from .models import RoundEntry
from .models import Fruit
from .models import OrderRound


admin.site.register(Order)
admin.site.register(Round)
admin.site.register(OrderEntry)
admin.site.register(RoundEntry)
admin.site.register(OrderRound)
admin.site.register(Fruit)


