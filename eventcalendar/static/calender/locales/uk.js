// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var uk = {
    code: 'uk',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 7, // The week that contains Jan 1st is the first week of the year.
    },
    buttonText: {
      prev: 'Попередній',
      next: 'далі',
      today: 'Сьогодні',
      month: 'Місяць',
      week: 'Тиждень',
      day: 'День',
      list: 'Порядок денний',
    },
    weekText: 'Тиж',
    allDayText: 'Увесь день',
    moreLinkText: function(n) {
      return '+ще ' + n + '...'
    },
    noEventsText: 'Немає подій для відображення',
  };

  return uk;

}());
