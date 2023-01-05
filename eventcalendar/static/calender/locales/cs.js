// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var cs = {
    code: 'cs',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Dříve',
      next: 'Později',
      today: 'Nyní',
      month: 'Měsíc',
      week: 'Týden',
      day: 'Den',
      list: 'Agenda',
    },
    weekText: 'Týd',
    allDayText: 'Celý den',
    moreLinkText: function(n) {
      return '+další: ' + n
    },
    noEventsText: 'Žádné akce k zobrazení',
  };

  return cs;

}());
