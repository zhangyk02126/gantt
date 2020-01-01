class Person:
    def __init__(self, chinese_name, english_name, alias, group_name):
        self.chinese_name = chinese_name
        self.english_name = english_name
        self.alias = alias
        self.group_name = group_name


zetgaar = Person('齐特佳', 'zetgaar', '齐特佳', 'Leader')
panpan = Person('桑奕盼', 'panpan', '盼盼', '产品')
zeta = Person('张云帆', 'zeta', 'zeta', '产品')
kui = Person('大魁', 'kui', '大魁', '算法')
xintong = Person('伊新铜', 'xintong', '新铜', '算法')

persons = [zetgaar, panpan, zeta, kui, xintong]


def get_name2person(persons):
    from collections import defaultdict
    t_name2ind = defaultdict(set)
    for ind, p in enumerate(persons):
        t_name2ind[p.chinese_name.lower()].add(ind)
        t_name2ind[p.english_name.lower()].add(ind)
        t_name2ind[p.alias.lower()].add(ind)
    name2ind = {}
    name2person = {}
    for k, v in t_name2ind.items():
        assert len(v) == 1, '出现重名：%s' % k
        name2ind[k] = list(v)[0]
        name2person[k] = persons[list(v)[0]]
    return name2ind, name2person


def check_english(persons):
    for p in persons:
        en = p.english_name.lower()
        for s in en:
            assert s >= 'a' and s <= 'z', '%s 的英文名字 %s 不合规' % (p.chinese_name, p.english_name)


print(get_name2person(persons))
print(check_english(persons))

# def get_person_id(name):
#     for
