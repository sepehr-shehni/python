from django.contrib import admin
from .models import ConcertModel, LocationModel, TimeModel, ProfileModel, TicketModel

# Register your models here.

# Register ConcertModel with the admin site
admin.site.register(ConcertModel)

# Register LocationModel with the admin site
admin.site.register(LocationModel)

# Register TimeModel with the admin site
admin.site.register(TimeModel)

# Register ProfileModel with the admin site
admin.site.register(ProfileModel)

# Register TicketModel with the admin site
admin.site.register(TicketModel)
