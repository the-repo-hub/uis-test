def calculate(num, k):
    result = int(num)
    indexes = [i for i in range(k, len(num))]
    c = 0
    rest = ''
    for i in range(len(num) * 2):
        s = rest
        for j in indexes:
            s += num[j]
        if result > int(s):
            result = int(s)
        if c == len(indexes):
            c = 0
            indexes = indexes[1:]
            rest += num[:1]
            num = num[1:]
        else:
            indexes[c] -= 1
            c += 1
    return result


def main():
    """
    assert calculate("1432219", 3) == 1219
    assert calculate("10200", 1) == 200
    assert calculate('2121313', 1) == 121313
    assert calculate('00100010', 1) == 10
    assert calculate('12345', 3) == 12
    assert calculate('1001001', 2) == 1
    """

    print(calculate(input('num = '), int(input('k = '))))


if __name__ == '__main__':
    main()
