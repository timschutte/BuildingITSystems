// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var ca = {
    code: 'ca',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Anterior',
      next: 'Següent',
      today: 'Avui',
      month: 'Mes',
      week: 'Setmana',
      day: 'Dia',
      list: 'Agenda',
    },
    weekText: 'Set',
    allDayText: 'Tot el dia',
    moreLinkText: 'més',
    noEventsText: 'No hi ha esdeveniments per mostrar',
  };

  return ca;

}());
