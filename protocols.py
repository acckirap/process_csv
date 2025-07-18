from typing import Protocol, List, Any
from argparse import Namespace

class Processor(Protocol):
    def process(self, data: List[List[Any]], args: Namespace) -> List[List[Any]]:
        ...