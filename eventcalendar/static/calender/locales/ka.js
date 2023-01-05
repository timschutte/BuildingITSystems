// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var ka = {
    code: 'ka',
    week: {
      dow: 1,
      doy: 7,
    },
    buttonText: {
      prev: 'წინა',
      next: 'შემდეგი',
      today: 'დღეს',
      month: 'თვე',
      week: 'კვირა',
      day: 'დღე',
      list: 'დღის წესრიგი',
    },
    weekText: 'კვ',
    allDayText: 'მთელი დღე',
    moreLinkText: function(n) {
      return '+ კიდევ ' + n
    },
    noEventsText: 'ღონისძიებები არ არის',
  };

  return ka;

}());
