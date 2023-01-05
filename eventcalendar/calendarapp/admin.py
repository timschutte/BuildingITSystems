# /*************************************************************** 
# *Title: Event Calendar 
# *Author: sajib1066 
# *Date: 5 July 2020 
# *Code version: V79 
# *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
# ****************************************************************/

from django.contrib import admin
from calendarapp import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        "id",
        "title",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]


@admin.register(models.EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = models.EventMember
    list_display = ["id", "event", "user", "created_at", "updated_at"]
    list_filter = ["event"]
