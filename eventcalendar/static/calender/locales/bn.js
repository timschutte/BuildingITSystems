// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var bn = {
    code: 'bn',
    week: {
      dow: 0, // Sunday is the first day of the week.
      doy: 6, // The week that contains Jan 1st is the first week of the year.
    },
    buttonText: {
      prev: 'পেছনে',
      next: 'সামনে',
      today: 'আজ',
      month: 'মাস',
      week: 'সপ্তাহ',
      day: 'দিন',
      list: 'তালিকা',
    },
    weekText: 'সপ্তাহ',
    allDayText: 'সারাদিন',
    moreLinkText: function(n) {
      return '+অন্যান্য ' + n
    },
    noEventsText: 'কোনো ইভেন্ট নেই',
  };

  return bn;

}());
