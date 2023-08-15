import pytest
from tasks_foo import unique_names_of_teaches, short_and_long, is_there_relationship, create_folder, check_folder
import data_task_1_1 as d1
import data_task_1_2 as d2
import data_task_1_3 as d3


# TASK_1
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


# TASK_2 тесты с API яндекс диск

url_1 = "https://cloud-api.yandex.net/v1/disk/resources" # корректный url
url_2 = "https://cloud-api.yandex.net/disk/resources" # не корректный url (404)

token_1 = 'укажите корректный токен' # корректный токен
token_2 = 'y0_AgAAAAABSEDuAADLWwAAAADi8j6CmHzAb6WNSFuHd3Vip8Dfr0' # не корректный токен (401)

path_1 = 'test_folder_1' # корректное название папки
path_2 = '' # некорректное название папки (400)

@pytest.mark.parametrize(
    'url,token, path, expected',
    [
        (url_1, token_1, path_1, 201), # OK - папка создана
        (url_1, token_1, path_1, 409), # Ресурс "{path}" уже существует.
        (url_1, token_2, path_1, 401), # Некорректный токен. Не авторизован
        (url_2, token_1, path_1, 404), # Некорректный URL.Не удалось найти запрошенный ресурс.
        (url_1, token_1, path_2, 400)  # Некорректное название папки. Некорректные данные.
    ]
)
def test_create_folder(url, token, path, expected):
    res = create_folder(url, path, token).status_code
    assert res == expected

@pytest.mark.parametrize(
    'path, expected',
    [
        ('test_folder_1', 200), # проверка созданной папки
        ('test_folder_2', 404)  # запрос к несуществующей папке
    ]
)
def test_check_folder (path, expected):
    res = check_folder(url_1, path, token_1).status_code
    assert res == expected