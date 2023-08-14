import requests


def unique_names_of_teaches(mentors) -> str:
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    # all_names_sorted = unique_names

    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


def short_and_long(courses, mentors, durations) -> tuple:
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "durations": duration}
        courses_list.append(course_dict)

    min_ = min(durations)
    max_ = max(durations)

    maxes = []
    minis = []
    for index, duration in enumerate(durations):
        if duration == max_:
            maxes.append(index)
        elif duration == min_:
            minis.append(index)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]['title'])

    for id in maxes:
        courses_max.append(courses_list[id]['title'])

    short = f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_} месяца(ев)'
    long = f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_} месяца(ев)'

    return short, long


def is_there_relationship(courses, mentors, durations) -> tuple:
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    duration_index = []
    mcount_index = []
    for index, course in enumerate(courses_list):
        duration_index.append([course['duration'], index])
        mcount_index.append([len(course[('mentors')]), index])

    duration_index.sort()
    mcount_index.sort()

    indexes_d = []
    indexes_m = []

    for d in duration_index:
        indexes_d.append(d[1])

    for m in mcount_index:
        indexes_m.append(m[1])

    relationship = "Связь есть" if indexes_d == indexes_m else "Связи нет"
    sorting_by_duration = f"Порядок курсов по длительности: {indexes_d}"
    sorting_by_quantity = f"Порядок курсов по количеству преподавателей: {indexes_m}"

    return relationship, sorting_by_duration, sorting_by_quantity


def create_folder(url, path, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    response = requests.put(url, headers=headers, params={'path': path})
    return response


def check_folder(url, path, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    response = requests.get(url, headers=headers, params={'path': path})
    return response
