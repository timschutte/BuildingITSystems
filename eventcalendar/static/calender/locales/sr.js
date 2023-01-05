// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var sr = {
    code: 'sr',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 7, // The week that contains Jan 1st is the first week of the year.
    },
    buttonText: {
      prev: 'Prethodna',
      next: 'Sledeći',
      today: 'Danas',
      month: 'Mеsеc',
      week: 'Nеdеlja',
      day: 'Dan',
      list: 'Planеr',
    },
    weekText: 'Sed',
    allDayText: 'Cеo dan',
    moreLinkText: function(n) {
      return '+ još ' + n
    },
    noEventsText: 'Nеma događaja za prikaz',
  };

  return sr;

}());
