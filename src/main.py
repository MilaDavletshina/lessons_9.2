def clear_names(file_name: str) -> list:   #принимаем строки, возвращаем список имен
    """функция очистки имен от лишних символов"""
    new_names_list = list()   #задаем новую переменную
    with open('data/' + file_name) as names_file:   #с помощью контекстного менеджера открываем файл names.txt + прибавляем файл кот мы принимаем
        names_list = names_file.read().split()   #читаем файл разом и разделяем на строки. получим массив из списка имен в 112 строк
        for name_item in names_list:   #чистим каждое имя
            new_name = ''
            for symbol in name_item: # проходим по каждой строке (по имени)
                if symbol.isalpha():
                    new_name += symbol  #после выхода из цикла будет либо пустая строка, либо строка из букв алфавита
            if new_name.isalpha():   #проверяем еще раз
                new_names_list.append(new_name)
    return new_names_list


if __name__ == '__main__':
    cleared_name = clear_names('names.txt')   #принимаем из файла

    for i in cleared_name:   #проходимся по списку
        print(i)