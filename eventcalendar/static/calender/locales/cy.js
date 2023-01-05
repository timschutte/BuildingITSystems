// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var cy = {
    code: 'cy',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Blaenorol',
      next: 'Nesaf',
      today: 'Heddiw',
      year: 'Blwyddyn',
      month: 'Mis',
      week: 'Wythnos',
      day: 'Dydd',
      list: 'Rhestr',
    },
    weekText: 'Wythnos',
    allDayText: 'Trwy\'r dydd',
    moreLinkText: 'Mwy',
    noEventsText: 'Dim digwyddiadau',
  };

  return cy;

}());
