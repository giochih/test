def starting_el_dict():
    import requests
    import collections
    ur = "https://ru.wikipedia.org/w/api.php"
    param = {
        "action": "query",
        "cmtitle": "Категория:Животные по алфавиту",
        "list": "categorymembers",
        "format": "json",
        "cmlimit": 20000,
        "cmcontinue": "",
        "cmtype": "page"
    }
    d = collections.defaultdict(int)
    while 1:
        js = requests.get(url=ur, params=param)
        data = js.json()
        pages = data['query']['categorymembers']
        for page in pages:
            t = page['title']
            d[t[0]] += 1
        if "continue" in data:
            param["cmcontinue"] = data["continue"]["cmcontinue"]
        else:
            break
    return d


def print_res():
    a = ord('А')
    alp = [chr(i) for i in range(a, a+6)] + ['Ё'] + [chr(i) for i in range(a+6, a+32)]
    d = starting_el_dict()
    for el in alp:
        print(f"{el}: {d[el]}")


if __name__ == '__main__':
    print_res()

"""
А: 1148
Б: 1600
В: 515
Г: 984
Д: 739
Е: 99
Ё: 2
Ж: 393
З: 621
И: 337
Й: 3
К: 2186
Л: 679
М: 1242
Н: 451
О: 766
П: 1730
Р: 556
С: 1738
Т: 968
У: 242
Ф: 189
Х: 270
Ц: 218
Ч: 658
Ш: 268
Щ: 146
Ъ: 0
Ы: 0
Ь: 0
Э: 213
Ю: 133
Я: 209
"""