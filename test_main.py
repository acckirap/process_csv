import pytest
from io import StringIO
from types import SimpleNamespace
from main import process_csv, convert_value

csv_data = """name,rating,qty
Mouse,4,10
Monitor,5,7
Notebook,3,15
"""

def test_filter_rating_gt_4(capsys):
    f = StringIO(csv_data)
    args = SimpleNamespace(where="rating>4", aggregate=None)
    process_csv(f, args)
    captured = capsys.readouterr()
    assert "Monitor" in captured.out
    assert "Mouse" not in captured.out

def test_filter_qty_eq_7(capsys):
    f = StringIO(csv_data)
    args = SimpleNamespace(where="rating>4", aggregate=None)
    process_csv(f, args)
    captured = capsys.readouterr()
    assert "Monitor" in captured.out
    assert "Mouse" not in captured.out
    assert "Notebook" not in captured.out

def test_aggregate_min_rating(capsys):
    f = StringIO(csv_data)
    args = SimpleNamespace(where=None, aggregate="rating=min")
    process_csv(f, args)
    captured = capsys.readouterr()
    assert "3" in captured.out

def test_invalid_filter():
    f = StringIO(csv_data)
    args = SimpleNamespace(where="rating>>4", aggregate=None)
    with pytest.raises(SyntaxError):
        process_csv(f, args)

def test_invalid_aggregate():
    f = StringIO(csv_data)
    args = SimpleNamespace(where=None, aggregate='rating!=avg')
    with pytest.raises(SyntaxError):
        process_csv(f, args)


def test_non_numeric_aggregate_fails():
    f = StringIO(csv_data)
    args = SimpleNamespace(where=None, aggregate='name=avg')
    with pytest.raises(ValueError):
        process_csv(f, args)

def test_convert_value_float():
    f = '2.58'
    converted = convert_value(f)
    assert isinstance(converted, float)

def test_convert_value_string():
    f = 'apple'
    converted = convert_value(f)
    assert isinstance(converted, str)

