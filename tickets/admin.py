from django.contrib import admin
from .models import Reservation, Ticket

# Register your models here.
class TicketInline(admin.StackedInline):
    model = Ticket # Specify which model to use
    extra = 2 # How many to start with

class ReservationAdmin(admin.ModelAdmin):
    fields = [
        'flight', 'num_people', 'total_cost'
    ]
    inlines = [TicketInline] # Load the RunwayInline Class

admin.site.register(Reservation, ReservationAdmin)