from operator import itemgetter


class MusicalWork:
    def __init__(self, id, title, duration, orchestra_id):
        self.id = id
        self.title = title
        self.duration = duration
        self.orchestra_id = orchestra_id


class Orchestra:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class WorkOrchestra:
    def __init__(self, orchestra_id, work_id):
        self.orchestra_id = orchestra_id
        self.work_id = work_id


# Тестовые данные
orchestras = [
    Orchestra(1, "Академический оркестр"),
    Orchestra(2, "Симфонический оркестр"),
    Orchestra(3, "Камерный ансамбль"),
    Orchestra(4, "Альтернативный оркестр"),
]

works = [
    MusicalWork(1, "Вальсов", 7.5, 1),
    MusicalWork(2, "Маршов", 5.0, 2),
    MusicalWork(3, "Реквием", 12.0, 3),
    MusicalWork(4, "Концертов", 10.0, 1),
    MusicalWork(5, "Сюита", 8.0, 2),
]

works_orchestras = [
    WorkOrchestra(1, 1),
    WorkOrchestra(1, 4),
    WorkOrchestra(2, 2),
    WorkOrchestra(2, 5),
    WorkOrchestra(3, 3),
    WorkOrchestra(4, 1),
    WorkOrchestra(4, 2),
]


def get_one_to_many(orchestras, works):
    return [
        (w.title, w.duration, o.name)
        for o in orchestras
        for w in works
        if w.orchestra_id == o.id
    ]


def get_many_to_many(orchestras, works, works_orchestras):
    temp = [
        (o.name, wo.orchestra_id, wo.work_id)
        for o in orchestras
        for wo in works_orchestras
        if o.id == wo.orchestra_id
    ]

    return [
        (w.title, w.duration, orchestra_name)
        for orchestra_name, _, work_id in temp
        for w in works
        if w.id == work_id
    ]


# Задание Д1
def query_d1(one_to_many):
    return [
        (title, orchestra)
        for title, _, orchestra in one_to_many
        if title.endswith("ов")
    ]


# Задание Д2
def query_d2(one_to_many, orchestras):
    result = []
    for o in orchestras:
        o_works = list(filter(lambda x: x[2] == o.name, one_to_many))
        if o_works:
            durations = [dur for _, dur, _ in o_works]
            avg = sum(durations) / len(durations)
            result.append((o.name, avg))
    return sorted(result, key=itemgetter(1))


# Задание Д3
def query_d3(many_to_many, orchestras):
    result = {}
    for o in orchestras:
        if o.name.startswith("А"):
            o_works = list(filter(lambda x: x[2] == o.name, many_to_many))
            result[o.name] = [title for title, _, _ in o_works]
    return result
