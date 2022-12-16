from django.urls import path, include
from fruits import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("orders", views.OrderList.as_view()),
    path("rounds", views.RoundList.as_view()),
    path("fruits", views.FruitList.as_view()),
    path("orders/<int:id>", views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
