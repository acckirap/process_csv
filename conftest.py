import pytest

@pytest.fixture
def sample_csv():
    return """name,rating,qty
Mouse,4,10
Monitor,5,8
Notebook,3,15
"""