import re  #импорт из библиотеки регулярных выражений


def clear_names(file_name: str) -> list:   #принимаем строки, возвращаем список имен
    """функция очистки имен от лишних символов"""
    new_names_list = list()   #задаем новую переменную
    with open('data/' + file_name) as names_file:   #с помощью контекстного менеджера открываем файл names.txt + прибавляем файл кот мы принимаем
        names_list = names_file.read().split()   #читаем файл целиком и разделяем на строки. получим массив из списка имен в 112 строк
        for name_item in names_list:   #проходим по всему списку полученных нами строк
            new_name = ''
            for symbol in name_item: # проходим по каждой строке (по имени)
                if symbol.isalpha():   #проверяем что строка состоит из букв
                    new_name += symbol  #после выхода из цикла будет либо пустая строка, либо строка из букв алфавита
            if new_name.isalpha():   #проверяем еще раз
                new_names_list.append(new_name)
    return new_names_list


def is_cyrillic(name_item: str) -> bool:
    """проверка на вхождение кириллицы в строку"""
    return bool(re.search('[а-яА-Я]', name_item))  #импортируем из библиотеки регулярных выражений. в [] задаем паттерн


def filter_russian_names(names_list: list) -> list:
    """Фильтрация имен написанных на русском"""
    new_names_list = list()
    for name_item in names_list:
        if is_cyrillic(name_item):
            new_names_list.append(name_item)

    return new_names_list

def save_to_file(file_name: str, data: str) -> None:
    """Сохраняет данные в файл"""
    with open('data/' + file_name, 'w') as names_file:   #'w'- на запись
        names_file.write(data)

if __name__ == '__main__':
    cleared_name = clear_names('names.txt')   #принимаем из файла
    #
    # for i in cleared_name:   #проходимся по списку
    #     print(i)
    #print(filter_russian_names(cleared_name)) #выводит только русские имена
    filtered_names = filter_russian_names(cleared_name)
    save_to_file(
        'russian_names.txt',       # есть файл
        '\n'.join(filtered_names)   #список сделали join через , и пробел
    )