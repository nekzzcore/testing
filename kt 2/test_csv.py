import pytest
from csv_average import calculate_average

def test_calculate_average():
    result = calculate_average('grades.csv')
    assert result == 49.7875  # correct average
