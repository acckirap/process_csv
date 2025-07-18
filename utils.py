import ast
from typing import Any


def convert_value(value: str) -> Any:
    try:
        value = ast.literal_eval(value)
    except ValueError:
        pass
    return value
