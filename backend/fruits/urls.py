from django.urls import path, include 
from fruits import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('orders', views.OrderList.as_view()),
    path('rounds', views.RoundList.as_view())
    # path('drinks/<int:id>', views.drink_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)