from django.shortcuts import render
from django.http import HttpResponse
from ticketsales.models import concertModel
from ticketsales.models import locationModel

# Create your views here.

#Response 1:
# def concertListView(request):
#     concerts = concertModel.objects.all()
#     return HttpResponse(concerts)

#Response 2:
# def concertListView(request):
#     concerts = concertModel.objects.all()
#     text = """
#     <!DOCTYPE html>
#     <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <title>Title</title>
#         </head>
#         <body>
#             <h1>لیست کنسرت ها</h1>
#             <ul>
#
#                 {}
#
#             </ul>
#
#         </body>
#     </html>
#     """.format('\n'.join('<li>{}</li>'.format(concert) for concert in concerts))
#     return HttpResponse(text)

#Response 3:
def concertListView(request):
    concerts = concertModel.objects.all()
    context = {

        "concertlist":concerts,
        "concertcount":concerts.count()
    }

    return render(request,"ticketsales/concertlist.html",context)

def locationListView(request):
    locations = locationModel.objects.all()
    context = {

        "locationlist":locations,
    }

    return render(request,"ticketsales/locationlist.html",context)

def concertDetailsView(request,concert_id):
    concert = locationModel.objects.get(pk=concert_id)
    context = {

        "concertdetails":concert
    }

    return render(request,"ticketsales/concertdetails.html",context)
