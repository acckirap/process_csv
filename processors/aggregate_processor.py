import argparse
from typing import List, Any

from aggregators import apply_aggregation
from parsers import parse_aggregate


class AggregateProcessor():
    def process(self, data: List[List[Any]], args: argparse.Namespace) -> List[List[Any]]:
        field, aggregation = parse_aggregate(args.aggregate)
        return apply_aggregation(data, field, aggregation)
