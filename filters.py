import operator
from typing import List, Any

from utils import convert_value

functions = {
    '=': operator.eq,
    '>': operator.gt,
    '<': operator.lt,
}

def apply_filter(data: List[List[Any]], field: str,op_symbol: str, value: str):
    op_func = functions[op_symbol]
    value = convert_value(value)

    header = data[0]
    field_index = header.index(field)
    filtered_rows = [
        row for row in data[1:] if op_func(convert_value(row[field_index]), value)
    ]

    return [header] + filtered_rows