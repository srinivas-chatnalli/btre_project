from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import state_choices, bedroom_choices, price_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', {'listings':paged_listings})

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    return render(request, 'listings/listing.html', {'listing':listing})

def search(request):
    queryset = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset = queryset.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset = queryset.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset = queryset.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset = queryset.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset = queryset.filter(price__lte=price)
    return render(request, 'listings/search.html', {'listings': queryset,
                                                    'state_choices': state_choices,
                                                    'bedroom_choices': bedroom_choices,
                                                    'price_choices': price_choices,
                                                    'values': request.GET})
