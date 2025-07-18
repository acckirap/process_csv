import csv
from io import StringIO
from types import SimpleNamespace

import pytest

from exceptions import InvalidFilterSyntax, InvalidAggregationSyntax, NonNumericAggregationError
from utils import convert_value
from main import process_csv



def prepare_file(csv_data):
    f = StringIO(csv_data)
    reader = csv.reader(f)
    return list(reader)

@pytest.mark.parametrize('where, expected_names, not_expected_names', [
    ('rating>4', ['Monitor'], ['Mouse', 'Notebook']),
    ('qty=10', ['Mouse'], ['Monitor', 'Notebook']),
    ('rating<4', ['Notebook'], ['Mouse', 'Monitor'])
])
def test_filter_rating_gt_4(sample_csv, where,expected_names, not_expected_names, capsys):
    data = prepare_file(sample_csv)
    args = SimpleNamespace(where=where, aggregate=None)
    process_csv(data, args)
    captured = capsys.readouterr()
    for name in expected_names:
        assert name in captured.out
    for name in not_expected_names:
        assert name not in captured.out


@pytest.mark.parametrize('aggregate, value', [
    ('rating=min', '3'),
    ('qty=avg', '11'),
])
def test_aggregate_min_rating(sample_csv, aggregate, value, capsys):
    data = prepare_file(sample_csv)
    args = SimpleNamespace(where=None, aggregate=aggregate)
    process_csv(data, args)
    captured = capsys.readouterr()
    assert value in captured.out


def test_invalid_filter(sample_csv):
    data = prepare_file(sample_csv)
    args = SimpleNamespace(where='rating>>4', aggregate=None)
    with pytest.raises(InvalidFilterSyntax):
        process_csv(data, args)


def test_invalid_aggregate(sample_csv):
    data = prepare_file(sample_csv)
    args = SimpleNamespace(where=None, aggregate='rating!=avg')
    with pytest.raises(InvalidAggregationSyntax):
        process_csv(data, args)


def test_non_numeric_aggregate_fails(sample_csv):
    data = prepare_file(sample_csv)
    args = SimpleNamespace(where=None, aggregate='name=avg')
    with pytest.raises(NonNumericAggregationError):
        process_csv(data, args)


def test_convert_value_float():
    f = '2.58'
    converted = convert_value(f)
    assert isinstance(converted, float)


def test_convert_value_string():
    f = 'apple'
    converted = convert_value(f)
    assert isinstance(converted, str)
