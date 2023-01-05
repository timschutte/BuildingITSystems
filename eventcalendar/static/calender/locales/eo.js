// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var eo = {
    code: 'eo',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Antaŭa',
      next: 'Sekva',
      today: 'Hodiaŭ',
      month: 'Monato',
      week: 'Semajno',
      day: 'Tago',
      list: 'Tagordo',
    },
    weekText: 'Sm',
    allDayText: 'Tuta tago',
    moreLinkText: 'pli',
    noEventsText: 'Neniuj eventoj por montri',
  };

  return eo;

}());
