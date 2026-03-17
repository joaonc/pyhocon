from datetime import timedelta

import pytest

from pyhocon.period_parser import parse_period
from pyhocon.period_serializer import timedelta_to_hocon

try:
    from dateutil.relativedelta import relativedelta as period
except ImportError:
    period = timedelta


@pytest.mark.parametrize('data_set', [
    ('1 minutes', period(minutes=1)),
    ('1minutes', period(minutes=1)),
    ('2 minute', period(minutes=2)),
    ('3 m', period(minutes=3)),
    ('3m', period(minutes=3)),

    ('4 seconds', period(seconds=4)),
    ('5 second', period(seconds=5)),
    ('6 s', period(seconds=6)),

    ('7 hours', period(hours=7)),
    ('8 hour', period(hours=8)),
    ('9 h', period(hours=9)),

    ('10 weeks', period(weeks=10)),
    ('11 week', period(weeks=11)),
    ('12 w', period(weeks=12)),

    ('10 days', period(days=10)),
    ('11 day', period(days=11)),
    ('12 d', period(days=12)),

    ('110 microseconds', period(microseconds=110)),
    ('111 microsecond', period(microseconds=111)),
    ('112 micros', period(microseconds=112)),
    ('113 micro', period(microseconds=113)),
    ('114 us', period(microseconds=114)),

    ('110 milliseconds', timedelta(milliseconds=110)),
    ('111 millisecond', timedelta(milliseconds=111)),
    ('112 millis', timedelta(milliseconds=112)),
    ('113 milli', timedelta(milliseconds=113)),
    ('114 ms', timedelta(milliseconds=114)),

    ('110 nanoseconds', period(microseconds=0)),
    ('11000 nanoseconds', period(microseconds=11)),
    ('1110000 nanosecond', period(microseconds=1110)),
    ('1120000 nanos', period(microseconds=1120)),
    ('1130000 nano', period(microseconds=1130)),
    ('1140000 ns', period(microseconds=1140)),
])
def test_parse_string_with_duration(data_set):
    config = parse_period(data_set[0])

    assert config == data_set[1]


@pytest.mark.parametrize('hocon_str,rd_kwargs', [
    ('1 months', {'months': 1}),
    ('1months', {'months': 1}),
    ('2 month', {'months': 2}),
    ('3 mo', {'months': 3}),
    ('3mo', {'months': 3}),

    ('1 years', {'years': 1}),
    ('1years', {'years': 1}),
    ('2 year', {'years': 2}),
    ('3 y', {'years': 3}),
    ('3y', {'years': 3}),
])
def test_parse_string_with_duration_optional_units(hocon_str, rd_kwargs):
    rd = pytest.importorskip('dateutil.relativedelta')
    parsed = parse_period(hocon_str)
    assert parsed == rd.relativedelta(**rd_kwargs)


def test_format_relativedelta():
    rd = pytest.importorskip('dateutil.relativedelta')
    for time_delta, expected_result in (
        (rd.relativedelta(seconds=0), '0 seconds'),
        (rd.relativedelta(hours=0), '0 seconds'),
        (rd.relativedelta(days=5), '5 days'),
        (rd.relativedelta(weeks=3), '21 days'),
        (rd.relativedelta(hours=2), '2 hours'),
        (rd.relativedelta(minutes=43), '43 minutes'),
    ):
        assert expected_result == timedelta_to_hocon(time_delta)


def test_format_time_delta():
    for time_delta, expected_result in ((timedelta(days=0), '0 seconds'),
                                        (timedelta(days=5), '5 days'),
                                        (timedelta(seconds=51), '51 seconds'),
                                        (timedelta(microseconds=786), '786 microseconds')):
        assert expected_result == timedelta_to_hocon(time_delta)
