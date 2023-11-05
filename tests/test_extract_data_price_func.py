import requests
import pandas as pd
import pytest
from main import extract_data_price


@pytest.mark.parametrize("expected_result", [(pd.DataFrame)])
def test_extract_data_price(expected_result):
    assert extract_data_price() == expected_result