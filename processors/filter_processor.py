import operator
import re
from typing import List, Any
from argparse import Namespace

from filters import apply_filter
from parsers import parse_filter
from utils import convert_value
from exceptions import InvalidFilterSyntax
from protocols import Processor  # путь зависит от твоей структуры


class FilterProcessor:
    def process(self, data: List[List[Any]], args: Namespace) -> List[List[Any]]:
        field, op_symbol, value = parse_filter(args.where)
        return apply_filter(data, field, op_symbol, value)
