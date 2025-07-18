import csv
from typing import Any, List

from tabulate import tabulate
from cli import parse_args
from exceptions import FileOpenError, CSVProcessingError
from processors.filter_processor import FilterProcessor
from processors.aggregate_processor import AggregateProcessor
from protocols import Processor

def load_data(file_path: str) -> List[List[Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        raise FileOpenError(f"Файл не найден: {file_path}")

def process_csv(data, args):
    processors: List[Processor] = []
    if args.where:
        processors.append(FilterProcessor())
    if args.aggregate:
        processors.append(AggregateProcessor())

    for processor in processors:
        data = processor.process(data, args)

    print(tabulate(data[1:], headers=data[0], tablefmt="grid"))

def main() -> None:
    args = parse_args()

    try:
        data = load_data(args.file)
        process_csv(data, args)

    except CSVProcessingError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()