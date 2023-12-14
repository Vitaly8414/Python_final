""" Урок 15. Обзор стандартной библиотеки Python
# Сдаем через гитхаб через репозиторий. Это очень важно.
# Возьмите любые 3 задания (или рекурсивный калькулятор или обычный с ГУИ) из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.

# Треугольник
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка - стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равобедренным или 
# равносторонним.
"""
import sys
import logging
from datetime import datetime

# добавляем модуль sys для работы с командной строкой, logging для логирования 
#  ошибок и полезной информации и datetime для фиксации времени

# Определяем функцию, которая принимает 3 аргумента
# Функция сравнивает длину каждого отрезка.
# Функция проверяет тип треугольника
# Также в основной программе добавляется система логирования
# для вывода полезной информации или об ошибке, если аргументы переданы некорректно

# def calc(s):
#     logger.info(f"Пользователь {name} ввел строку {s}")
#     try:
#         print(f"Результат равен {eval(s)}")
#         logger.info(f"результат вычисления равен {eval(s)}")
#     except ZeroDivisionError as e:
#         print(e)
#         logger.critical(f"{datetime.now().strftime('%H:%M:%S')} произошла ошибка {e}")

def check_triangle(a, b, c):
    logging.info(f"Пользователь {name} ввел значения треугольника со сторонами {a},{b},{c}")
    if a <= 0 or b <= 0 or c <= 0:
        logging.error("Длина стороны должна быть положительным числом")
        return False
    
    if a + b <= c or a + c <= b or b + c <= a:
        logging.info("Треугольник с такими сторонами не существует")
        return False
    
    if a != b and a != c and b != c:
        logging.info("Треугольник разносторонний")
    elif a == b and b == c:
        logging.info("Треугольник равносторонний")
    else:
        logging.info("Треугольник равнобедренный")
    return True

if __name__ == '__main__':
    logging.basicConfig(filename='project.log.',
                    encoding='utf-8',
                    level=logging.NOTSET)
logger = logging.getLogger('Треугольник')

if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])

        check_triangle(a, b, c)
        name = input("Введите свое имя ")
else:
        logging.error(f"{datetime.now().strftime('%H:%M:%S')} Некорректное число аргументов, введите значения a, b, c через пробел")