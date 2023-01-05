// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var el = {
    code: 'el',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4st is the first week of the year.
    },
    buttonText: {
      prev: 'Προηγούμενος',
      next: 'Επόμενος',
      today: 'Σήμερα',
      month: 'Μήνας',
      week: 'Εβδομάδα',
      day: 'Ημέρα',
      list: 'Ατζέντα',
    },
    weekText: 'Εβδ',
    allDayText: 'Ολοήμερο',
    moreLinkText: 'περισσότερα',
    noEventsText: 'Δεν υπάρχουν γεγονότα προς εμφάνιση',
  };

  return el;

}());
