from django.shortcuts import render
from ticketsales.models import ConcertModel, LocationModel

def concertListView(request):
    """
    View function to display a list of concerts.
    """
    concerts = ConcertModel.objects.all()
    context = {
        "concerts": concerts,
        "concert_count": concerts.count()
    }
    return render(request, "ticketsales/concertlist.html", context)

def locationListView(request):
    """
    View function to display a list of locations.
    """
    locations = LocationModel.objects.all()
    context = {
        "locations": locations,
    }
    return render(request, "ticketsales/locationlist.html", context)

def concertDetailsView(request, concert_id):
    """
    View function to display details of a specific concert.
    """
    concert = ConcertModel.objects.get(pk=concert_id)
    context = {
        "concert": concert
    }
    return render(request, "ticketsales/concertdetails.html", context)
