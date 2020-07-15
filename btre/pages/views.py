from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    return render(request, 'pages/index.html', {'listings': listings,
                                                'state_choices': state_choices,
                                                'bedroom_choices': bedroom_choices,
                                                'price_choices': price_choices})

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    return render(request, 'pages/about.html', {'realtors': realtors,
                                                'mvp_realtors': mvp_realtors})
