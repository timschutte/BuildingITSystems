// /*************************************************************** 
// *Title: Event Calendar 
// *Author: sajib1066 
// *Date: 5 July 2020 
// *Code version: V79 
// *Availability: https://github.com/sajib1066/event-calendar (Accessed 14 December 2022) 
// ****************************************************************/

FullCalendar.globalLocales.push(function () {
  'use strict';

  var ko = {
    code: 'ko',
    buttonText: {
      prev: '이전달',
      next: '다음달',
      today: '오늘',
      month: '월',
      week: '주',
      day: '일',
      list: '일정목록',
    },
    weekText: '주',
    allDayText: '종일',
    moreLinkText: '개',
    noEventsText: '일정이 없습니다',
  };

  return ko;

}());
