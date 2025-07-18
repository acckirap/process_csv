from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    parser = ArgumentParser(description="Обработка CSV")
    parser.add_argument("--file", required=True, type=str, help="file destination")
    parser.add_argument("--where", type=str, help="condition for select")
    parser.add_argument("--aggregate", type=str, help="aggregation")
    return parser.parse_args()
