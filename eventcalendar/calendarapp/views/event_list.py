# /*************************************************************** 
# *Title: Event Calendar 
# *Author: sajib1066 
# *Date: 5 July 2020 
# *Code version: V79 
# *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
# ****************************************************************/

from django.views.generic import ListView

from calendarapp.models import Event


class AllEventsListView(ListView):
    """ All event list views """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)


class RunningEventsListView(ListView):
    """ Running events list view """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)
