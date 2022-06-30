from datetime import datetime


def suma():
    print(f"1 + 1 = {1+1}")


def suma_2(suma: int):
    if suma == 2:
        print(f"1⚽ + 1⚽ = {1+1}⚽")
    else:
        print("OTRA SUMA")


def function_date():
    date = datetime.now()
    if date.month == 5 and date.date == 4 and date.year == 2022:
        print("May the Forth Be with You!")
    else:
        print(f"The current date is: {date.month}-{date.date}-{date.year}")


def function_date_2():
    date = datetime.now()
    output = f"The current month is {date.month}"
    if date.month == 5:
        if date.date == 5:
            if date.year == 2022:
                print("May the Forth Be with You!")
    print(output)


def function_4():
    date = datetime.now()

    if date.month == 11:
        print('Es Noviembre')
    elif date.month == 12:
        print('Es Noviembre')
    elif date.month == 1:
        print('Es Enero')
    else:
        print('No hay coincidencias')

    # match date.month: Python 3.10 Feature
    #     case 11:
    #         print('Es Noviembre')
    #     case 12:
    #         print('Es Diciembre')
    #     case 1:
    #         print('Es Enero')
    #     case other:
    #         print('No hay coincidencias')


if __name__ == '__main__':
    function_date()
