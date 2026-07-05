from django.shortcuts import render

from .models import Product


def home(request):
    featured_products = Product.objects.filter(is_active=True)[:6]

    benefits = [
        {'title': 'Fast Shipping', 'text': 'Get orders delivered quickly with reliable service.'},
        {'title': 'Secure Checkout', 'text': 'Your payment and data stay protected at every step.'},
        {'title': '24/7 Support', 'text': 'We are here to help whenever you need assistance.'},
    ]

    return render(request, 'store/home.html', {
        'featured_products': featured_products,
        'benefits': benefits,
    })
