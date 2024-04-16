from django.contrib import admin
from ticketsales.models import concertModel
from ticketsales.models import locationModel
from ticketsales.models import timeModel
from ticketsales.models import ProfileModel
from ticketsales.models import ticketModel


# Register your models here.
admin.site.register(concertModel)
admin.site.register(locationModel)
admin.site.register(timeModel)
admin.site.register(ProfileModel)
admin.site.register(ticketModel)
