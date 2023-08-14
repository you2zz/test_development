import pytest
from task_1 import unique_names_of_teaches, short_and_long, is_there_relationship
import data_task_1_1 as d1
import data_task_1_2 as d2
import data_task_1_3 as d3


@pytest.mark.parametrize(
    'mentors_name,expected',
    [
        (d1.mentors_1, d1.unique_names_1),
        (d1.mentors_2, d1.unique_names_2),
        (d1.mentors_3, d1.unique_names_3)
    ]
)
def test_unique_names_of_teaches(mentors_name, expected):
    res = unique_names_of_teaches(mentors_name)
    assert res == expected


@pytest.mark.parametrize(
    'duration,expected',
    [
        (d2.durations_1, d2.answer_1),
        (d2.durations_2, d2.answer_2),
        (d2.durations_3, d2.answer_3),
        (d2.durations_4, d2.answer_4),
        (d2.durations_5, d2.answer_5)
    ]
)
def test_short_and_long(duration, expected):
    res = short_and_long(d2.courses, d2.mentors, duration)
    assert res == expected


@pytest.mark.parametrize(
    'mentors,durations, expected',
    [
        (d3.mentors_1, d3.durations_1, d3.answer_1),
        (d3.mentors_1, d3.durations_2, d3.answer_2),
        (d3.mentors_2, d3.durations_2, d3.answer_3),
        (d3.mentors_2, d3.durations_1, d3.answer_4)
    ]
)
def test_is_there_relationship(mentors, durations, expected):
    res = is_there_relationship(d3.courses, mentors, durations)
    assert res == expected