import sqlite3
import random
import datetime

conn = sqlite3.connect("base.db")
cur = conn.cursor()


def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS "accrual" (
            	"id"	INTEGER,
            	"date"	DATE,
	            "month"	STRING,
            	PRIMARY KEY("id" AUTOINCREMENT)
                );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS "payment" (
                	"id"	INTEGER,
                	"date"	DATE,
    	            "month"	STRING,
                	PRIMARY KEY("id" AUTOINCREMENT)
                    );""")
    conn.commit()


def date_generator(num):
    for i in range(num):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        year = random.randint(2019, 2022)
        yield f'{year}-{month}-{day}', month


def create_some_data(accruals=10, payments=15):
    gen = date_generator(accruals)
    for date in gen:
        cur.execute(f'insert into accrual values (NULL, "{date[0]}", "{date[1]}")')
    gen = date_generator(payments)
    for date in gen:
        cur.execute(f'insert into payment values (NULL, "{date[0]}", "{date[1]}")')
    conn.commit()


def make_datetime(s):
    s = list(map(int, s.split('-')))
    return datetime.date(s[0], s[1], s[2])


def query_fn():
    accruals = list(cur.execute('select * from accrual order by date, month').fetchall())
    payments = list(cur.execute('select * from payment order by date, month').fetchall())

    table = {}
    out = []

    for pay in payments:
        for acc in accruals:
            if acc[2] == pay[2] and make_datetime(pay[1]) >= make_datetime(acc[1]):
                table[pay] = acc
                accruals.remove(acc)
                payments.remove(pay)
                break
    reboot = True
    while reboot:
        reboot = False
        for pay in payments:
            for acc in accruals:
                if make_datetime(pay[1]) < make_datetime(acc[1]):
                    out.append(pay)
                    payments.remove(pay)
                    reboot = True
                    break
                else:
                    table[pay] = acc
                    accruals.remove(acc)
                    payments.remove(pay)
                    reboot = True
                    break
            if reboot:
                break
    return table, out


if __name__ == '__main__':
    flag = False # перевести в True, чтобы создать бд (необходимо удалить существующую)
    if flag:
        create_tables()
        create_some_data(100, 150)
    result = query_fn()

    print('Таблица соответствий:\n')
    print('Платежи\t\t\t\t\t\t\tДолги\n')
    for payment, accrual in result[0].items():
        print(f'{payment}\t\t\t{accrual}')
    print('\nПлатежи, не нашедшие себе долга:\n')
    for line in result[1]:
        print(line)
