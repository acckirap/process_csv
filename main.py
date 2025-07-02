import argparse
import ast
import operator
from typing import Any, IO
from tabulate import tabulate
import csv
import re

functions = {
    '=': operator.eq,
    '>': operator.gt,
    '<': operator.lt,
}

aggregations = {
    'min': min,
    'max': max,
    'avg': lambda x: sum(x)/ len(x)
}

def convert_value(value: str)-> Any:
    try:
        value = ast.literal_eval(value)
    except ValueError:
        pass
    return value

def process_csv(file: IO[str], args: argparse.Namespace) -> None:
    reader = csv.reader(file)
    data = list(reader)
    if args.where:
        pattern = r'^(\w+)\s*(=|<|>)\s*([\w\.\'-]+)$'
        match = re.match(pattern, args.where)
        if not match:
            raise SyntaxError('Некорректный запрос')
        field, function, value = match.groups()
        function = functions[function]
        value = convert_value(value)
        lookup_field = data[0].index(field)
        filtered = [row for row in data[1:] if function(convert_value(row[lookup_field]), value)]
        data = [data[0]] + filtered

    if args.aggregate:
        pattern = r'^(\w+)\s*=\s*(min|max|avg)$'
        match = re.match(pattern, args.aggregate)
        if not match:
            raise SyntaxError('Некорректный запрос')
        field, aggregation = match.groups()
        lookup_field = data[0].index(field)
        try:
            data_to_aggregate = list(map(lambda x: float(x[lookup_field]), data[1:]))
        except ValueError:
            raise ValueError('Аггрегация поддерживается только для числовых полей')
        func = aggregations[aggregation]
        data = [[aggregation], [func(data_to_aggregate)]]

    print(tabulate(data[1:], headers=data[0], tablefmt="grid"))



def main() -> None:
    parser = argparse.ArgumentParser(description='Обработка CSV')
    parser.add_argument('--file', type=str, help='file destination')
    parser.add_argument('--where', type=str, help='condition for select')
    parser.add_argument('--aggregate', type=str, help='aggregation')
    args = parser.parse_args()
    file_path = args.file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            process_csv(f, args)
    except FileNotFoundError:
        raise FileNotFoundError('Файл не найден')


if __name__ == "__main__":
    main()