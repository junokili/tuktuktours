from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tours.models import Tour


def basket_contains(request):

    basket_not_empty = []
    total = 0
    tour_count = 0

    if tour_count >= settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE/100)
        discount_delta = 0
    else:
        discount = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - tour_count

    grand_total = total - discount

    context = {
        'basket_not_empty': basket_not_empty,
        'total': total,
        'tour_count': tour_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
        }

    return context
