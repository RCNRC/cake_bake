# cake_bake

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
