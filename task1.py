def task(array):
    if array[0] == '0':
        return 0
    if array[-1] == '1':
        return "no answer"
    i = 0
    j = len(array)-1
    while j - i > 1:
        k = (i + j) // 2
        if array[k] == '1':
            i = k
        else:
            j = k
    return j


if __name__ == '__main__':
    print(task("111111111110000000000000000"))  # 11
    print(task("1"))  # no
    print(task("0"))  # 0
    print(task("10"))  # 1
    print(task("110"))  # 2
    print(task("100"))  # 1
    print(task("1100"))  # 2
    print(task("11111111111111111111111111111"))  # no
    print(task("000000000000000000000000"))  # 0
