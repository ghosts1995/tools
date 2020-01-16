# !/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import calendar
from datetime import timedelta


class Timer:

    def getNextMonthOneDay(self):
        time = datetime.date.today()
        # 求当前月第一天
        first_day = datetime.date(time.year, time.month, 1)
        # 求当前月的最后一天
        days_num = calendar.monthrange(first_day.year, first_day.month)[1]  # 获取当前月有多少天
        # 求下个月的第一天
        first_day_of_next_month = first_day + datetime.timedelta(days=days_num)
        startDate = str(first_day_of_next_month)
        time = ("%s 13:00:00" % startDate)
        return time

    def getNextWeekOneDay(self):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        m1 = calendar.MONDAY
        while today.weekday() != m1:
            today += oneday
        nextMonday = today.strftime('%Y-%m-%d')
        time = ("%s 13:00:00" % nextMonday)
        return time


    def getWeekSix(self):
        now = datetime.datetime.now()
        six = now + timedelta(days=now.weekday() + 5)
        return six
