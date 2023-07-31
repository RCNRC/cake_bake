# cake_bake

Проект представляет собой сайт по закзу тортов, [пример работающего сайта](https://testserverdvmn.pythonanywhere.com/).

## Установка

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:  
1. Для Unix/macOs:
```commandline
python -m pip install -r requirements.txt
```
2. Для Windows:
```commandline
py -m pip install --destination-directory DIR -r requirements.txt
```

Далее:
1. Сгенерируйте секретный ключ `secret_key`, в котором будет не меньше 50 символов и не меньше 5 уникальных символов.
2. Создайте в корневой директории файл `.env`
3. Поместите в файл `.env` строку `SECRET_KEY=secret_key`, где `secret_key` - секретный ключ, полученный на шаге 1.

## Получение числа посещений сайта из других адресов

- Для получения числа посещений из конкретного адреса `url_address` введите в терминале команду `python3 manage.py get_visits --url=url_address`
- Для получения числа посещений из 10 наиболее посещяемых адресов введите в терминале команду `python3 manage.py get_visits`
