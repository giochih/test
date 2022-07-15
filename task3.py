def intersection(a, b):
    ans = []
    k = 0
    j = 0
    while k < len(a) and j < len(b):
        first = a[k]
        second = b[j]
        if first[1] <= second[0]:
            k += 1
        elif first[0] >= second[1]:
            j += 1
        elif first[0] < second[0]:
            if first[1] < second[1]:
                ans.append([second[0], first[1]])
                k += 1
            else:
                ans.append(second)
                j += 1
        else:
            if first[1] < second[1]:
                ans.append(first)
                k += 1
            else:
                ans.append([first[0], second[1]])
                j += 1
    return ans


def count_time(a):

    answer = 0
    for el in a:
        answer += el[1] - el[0]
    return answer


def normal(a):
    flag = True
    ans = a[:]
    while flag:
        ans.sort(key=lambda x: x[0])
        new = []
        flag = False
        last = True
        j = 0
        while j < len(ans) - 1:
            if ans[j][1] >= ans[j + 1][0]:
                flag = True
                if j == len(ans) - 2:
                    last = False
                new.append([ans[j][0], max(ans[j + 1][1], ans[j][1])])
                j += 1
            else:
                new.append(ans[j])
            j += 1
        if last:
            new.append(ans[len(ans) - 1])
        ans = new[:]
    return ans


def appearance(intervals):
    lesson = intervals['lesson']
    les = normal([[lesson[2*j], lesson[2*j+1]] for j in range(len(lesson) // 2)])
    pup = intervals['pupil']
    p = normal([[pup[2*j], pup[2*j + 1]] for j in range(len(pup) // 2)])
    tut = intervals['tutor']
    t = normal([[tut[2*j], tut[2*j + 1]] for j in range(len(tut) // 2)])
    common_interval = intersection(les, p)
    common_interval = intersection(common_interval, t)
    return count_time(common_interval)


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117},
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577},
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565},
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
