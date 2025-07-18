from typing import List, Any

from exceptions import NonNumericAggregationError

aggregations = {"min": min, "max": max, "avg": lambda x: sum(x) / len(x)}

def apply_aggregation(data: List[List[Any]], field: str, aggregation: str) -> List[List[Any]]:
    lookup_field = data[0].index(field)
    try:
        values = [float(row[lookup_field]) for row in data[1:]]
    except ValueError:
        raise NonNumericAggregationError("Аггрегация поддерживается только для числовых полей")
    result = aggregations[aggregation](values)
    return [[aggregation], [result]]