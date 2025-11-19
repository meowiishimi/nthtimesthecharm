from django.contrib import admin
from .models import Building, Agent, Venue

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'building')

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'floor_area', 'type', 'capacity', 'floor', 'building', 'agent')

