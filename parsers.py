import re
from exceptions import InvalidAggregationSyntax, InvalidFilterSyntax


def parse_aggregate(aggregate_str: str) -> tuple[str, str]:
    pattern = r"^(\w+)\s*=\s*(min|max|avg)$"
    match = re.match(pattern, aggregate_str)
    if not match:
        raise InvalidAggregationSyntax("Некорректный запрос")
    return match.groups()

def parse_filter(where_str: str) -> tuple[str, str, str]:
    pattern = r'^(\w+)\s*(=|<|>)\s*([\w\.\'-]+)$'
    match = re.match(pattern, where_str)
    if not match:
        raise InvalidFilterSyntax("Некорректный запрос")
    field, op_symbol, value = match.groups()
    return field, op_symbol, value