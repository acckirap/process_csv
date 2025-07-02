Инструкция

В репозитории находится тестовый файл test.csv, который можно использовать для тестирования.
Параметры запроса:
--file - адрес файла для обработки
--where - условие для выборки:
    "field>1"
    "field=name"
    "field<100"
--aggregate - выбор поля и метода аггрегации:
    "field=min"
    "field=max"
    "field=avg"

Пример запуска скрипта:
python main.py --file test.csv --where "rating>2" --aggregate "price=min"