Заключительное задание по погружение в Python:

Урок 15. Обзор стандартной библиотеки Python
Сдаем через гитхаб через репозиторий. Это очень важно.
Возьмите любые 3 задания (или рекурсивный калькулятор или обычный с ГУИ) из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.

Задача реализована на примере "Треугольник"
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка - стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равобедренным или равносторонним.

Решение:
Добавляем модуль sys для работы с командной строкой, 
logging для логирования ошибок и полезной информации и
datetime для фиксации времени

Определяем функцию, которая принимает 3 аргумента
Функция сравнивает длину каждого отрезка.
Функция проверяет тип треугольника
Также в основной программе добавляется система логирования для вывода полезной информации или об ошибке, если аргументы переданы некорректно
