def main():
    """
    Ввод значений с клавиатуры для формирования
    списка, по которому мы ищем искомое число и
    самого искомого числа

    Вызов функции guess_number, пытающуюся угадать число
    путем выбора подходящего алгоритма поиска

    args:
        number: загаданное искомое число
        lst: cписок целых чисел, в котором производится поиск
        type: способ поиска:
            - 'seq': последовательный (медленный) поиск
            - 'bin': бинарный поиск

    returns:
        кортеж, содержащий два элемента:
            - угаданное число (или -1, если число не найдено)
            - количество попыток
    """

    number = int(input('Введите загаданное число: '))
    low = int(input('Введите нижнюю границу диапазона: '))
    high = int(input('Введите верхнюю границу диапазона: '))

    # создаем список возмоных чисел
    data_list = list(range(low, high + 1))

    # выбираем тип поиска
    search_type = input('Выберите тип поиска (seq/bin): ')

    # вызываем функцию после определения
    result, tries = guess_number(number, data_list, search_type)
    # выводим результат
    if result == -1:
        print("Число не найдено в указанном диапазоне")
    else:
        print(f"Число {result} угадано за {tries} попыток")


def guess_number(number, lst, type='seq'):
    if type == 'seq':
        # ищем число последовательно
        attempts = 0  # счетчик количества попыток
        for guess in lst:  # цикл проходит по числам от low до high включительно
            attempts += 1
            if guess == number:
                return guess, attempts  # возвращаем результат и количество попыток
        return -1, attempts  # если число вне диапазона

    elif type == 'bin':
        # ищем число с помощью алгоритма бинарного поиска
        left, right = 0, len(lst) - 1  # задаем границы списка
        attempts = 0  # счетчик количества попыток
        while left <= right:
            middle = (left + right) // 2  # рассчитываем индекс среднего элемента
            attempts += 1
            if lst[middle] == number:
                return number, attempts
            elif lst[middle] > number:
                right = middle - 1  # иначе если средний элемент больше искомого — двигаемся влево
            else:
                left = middle + 1  # иначе - вправо
        return -1, attempts  # если число вне диапазона


# запуск основного сценария
if __name__ == "__main__":
    main()
