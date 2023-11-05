from main import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (16, 8, 2),
                                                   (30, 15, 2),
                                                   (100, 25, 4),
                                                   (5.0, 2.5, 2.0)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, divider, divison_np", [(ZeroDivisionError, 0, 10),
                                                         (TypeError, "2", 20)])
def test_zero_division(expected_exception, divider, divison_np):
    # в этом контексте мы ожидаем получить ошибку
    with pytest.raises(expected_exception):
        division(divison_np, divider)