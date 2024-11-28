class MyDict:                   #тестовая версия
    def __init__(self):
        """Инициализация пустого словаря."""
        self._data = []  # Храним данные как список кортежей (ключ, значение)

    def __getitem__(self, key):
        """Получение значения по ключу. Если ключ не существует, вернуть None."""
        for k, v in self._data:
            if k == key:
                return v
        return None

    def __setitem__(self, key, value):
        """Установка значения по ключу."""
        for i, (k, v) in enumerate(self._data):
            if k == key:
                self._data[i] = (key, value)  # Обновляем значение
                return
        self._data.append((key, value))  # Если ключ не найден, добавляем новую пару

    def __delitem__(self, key):
        """Удаление элемента по ключу. Если ключ не существует, ничего не делать."""
        for i, (k, v) in enumerate(self._data):
            if k == key:
                del self._data[i]
                return

    def keys(self):
        """Возврат списка всех ключей в словаре."""
        return [k for k, v in self._data]

    def values(self):
        """Возврат списка всех значений в словаре."""
        return [v for k, v in self._data]

    def items(self):
        """Возврат списка пар (ключ, значение) в словаре."""
        return self._data

    def __contains__(self, key):
        """Проверка наличия ключа в словаре (аналог оператора `in`)."""
        return any(k == key for k, v in self._data)

    def __str__(self):
        """Возврат строкового представления словаря для удобства отладки."""
        return "{" + ", ".join(f"{k}: {v}" for k, v in self._data) + "}"
my_dict = MyDict()

# Добавляем элементы
my_dict['name'] = 'Alice'
my_dict['age'] = 30

# Получаем элементы
print(my_dict['name'])  # 'Alice'
print(my_dict['age'])   # 30

# Проверка на наличие ключа
print('city' in my_dict)  # False

# Удаление элемента
del my_dict['age']

# Получаем ключи и значения
print(my_dict.keys())  # ['name']
print(my_dict.values())  # ['Alice']

# Печать словаря
print(my_dict)  # {name: Alice}