from loguru import logger

#  https://t.me/pyway/270
"""
Когда вы определяете функцию внутри другой функции и используете локальные переменные внешней функции во вложенной, 
вы создаете замыкание. Время жизни этих переменных "продляется" в особой области видимости enclosing даже после 
завершения работы внешней функции. Пример: make_adder возвращает функцию-прибавлятор. Объект из переменной a будет жить
и работать даже после выхода из make_adder:
"""


def make_adders1(a):
    logger.info(f"")
    def adder(x):
        return a + x

    return adder


"""
Вместо функций прибавляющих разные числа от 0 до 2, мы получили 3 одинаковых функции, потому что внутри себя они
поддерживают ссылку на одну и ту же переменную a, значение которой останется равным 2 после выполнения
всего цикла целиком.

Есть простой прием, помогающий "зафиксировать" значения переменной в моменте: достаточно добавить во вложенную функцию
дополнительный аргумент со значением по умолчанию, равным нужной переменной a=a:
"""


def make_adders2():
    logger.info(f"")
    adders = []
    for a in range(3):
        def adder(x):
            return a + x

        adders.append(adder)
    return adders


def primer1():
    logger.info(f"")
    plus_5 = make_adders1(5)
    logger.info(plus_5(3))  # 8


def primer2():
    logger.info(f"")
    adders = make_adders2()
    for adder in adders:
        logger.info(f"{adder(2)}")  # 4 4 4


"""
Вместо функций прибавляющих разные числа от 0 до 2, мы получили 3 одинаковых функции, потому что внутри себя они 
поддерживают ссылку на одну и ту же переменную a, значение которой останется равным 2 после выполнения всего цикла целиком.

Есть простой прием, помогающий "зафиксировать" значения переменной в моменте: достаточно добавить во вложенную функцию 
дополнительный аргумент со значением по умолчанию, равным нужной переменной a=a:
"""


def make_adders3():
    logger.info(f"")
    adders = []
    for a in range(3):
        def adder(x, a=a):  # FIX!
            return a + x

        adders.append(adder)
    return adders


def primer3():
    logger.info(f"")
    adders = make_adders3()
    for adder in adders:
        logger.info(adder(2))  # 2 3 4
"""
Еще лучше переименовать аргумент, чтобы избежать конфликтов имен и замечаний IDE, например, так:

def adder(x, that_a=a):  # FIX!
    return that_a + x
"""
def make_adders4():
    logger.info(f"")
    adders = []
    for a in range(3):
        def adder(x, that_a=a):  # FIX!
            return that_a + x

        adders.append(adder)
    return adders


def primer4():
    logger.info(f"")
    adders = make_adders4()
    for adder in adders:
        logger.info(adder(2))  # 2 3 4

def primer():
    primer1()
    primer2()
    primer3()
