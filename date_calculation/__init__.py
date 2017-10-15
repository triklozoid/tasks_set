#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

draw_schedule = (
        {
            'weekday': 2,
            'hour': 20,
            'minute': 0,
            'second': 0,
            'microsecond': 0,
        },
        {
            'weekday': 5,
            'hour': 20,
            'minute': 0,
            'second': 0,
            'microsecond': 0,
        },
)

def _next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)

def _nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

def get_next_draw_date(first_date=None):
    if first_date is None:
        first_date = datetime.now()
    dates = []
    for date in draw_schedule:
        d = _next_weekday(first_date, date['weekday'])
        d = d.replace(
            hour=date['hour'],
            minute=date['minute'],
            second=date['second'],
            microsecond=date['microsecond']
        )
        dates.append(d)

    return _nearest(dates, first_date)
