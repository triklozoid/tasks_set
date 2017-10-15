#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from datetime import datetime, timedelta

import date_calculation


def test_date_calculation():
    tests_count = 100000
    timedelta_range = 10 ** 8
    for i in xrange(0, tests_count):
        test_date = datetime.now() + timedelta(seconds=random.randint(0, timedelta_range) - timedelta_range / 2)
        result = date_calculation.get_next_draw_date(first_date=test_date)
        td = result - test_date
        assert td.total_seconds() > 0

        scheduled_weekdays = [d['weekday'] for d in date_calculation.draw_schedule]
        assert result.weekday() in scheduled_weekdays
        scheduled_hours = [d['hour'] for d in date_calculation.draw_schedule]
        assert result.hour in scheduled_hours
test_date_calculation()
