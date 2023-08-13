import pytest
from task_1 import unique_names_of_teaches
from data import mentors_1, mentors_2, mentors_3, unique_names_1, unique_names_2, unique_names_3


@pytest.mark.parametrize(
    'mentors,expected',
    [
        (mentors_1, unique_names_1),
        (mentors_2, unique_names_2),
        (mentors_3, unique_names_3)
    ]
)
def test_unique_names_of_teaches(mentors, expected):
    res = unique_names_of_teaches(mentors)
    assert res == expected
