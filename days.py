def get_days(date: str) -> int:
    date = list(map(int, date.split('-')))
    current_year = date[0] # записываем текущий год

    # считаем все дни с 0 года
    date[0] -= 1 # не следует считать год, который еще не завершился
    result = date[2]
    leap = date[0] // 4 - date[0] // 100 + date[0] // 400 + 1
    result += leap * 366
    result += (date[0] - leap) * 365

    # считаем дни в месяцах текущего года
    a, b = 31, 30
    for m in range(1, date[1]):
        if m == 8:
            a, b = b, a
        if m == 2:
            result += 28
            if current_year % 400 == 0 or (current_year % 100 != 0 and current_year % 4 == 0):
                result += 1
        else:
            if m % 2 != 0:
                result += a
            else:
                result += b
    return result


def main():
    date1 = input('date1 = ')
    date2 = input('date2 = ')
    res = get_days(date1) - get_days(date2)
    if res < 0:
        res *= -1
    print(res)


if __name__ == '__main__':
    main()
