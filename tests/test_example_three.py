from main import example_three
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 10),
                                                   (2, 2, 2),
                                                   (5.0, 1.0, 5.0),
                                                   (2.2, 2.4, 2.4)])
def test_example_three(a, b, expected_result):
    assert example_three(a, b) == expected_result



@pytest.mark.parametrize("expected_exception, a, b", [
                                                     (TypeError, "2", 2),
                                                     (TypeError, "1.5", 1)])
def test_zero_division(expected_exception, a, b):
    # в этом контексте мы ожидаем получить ошибку
    with pytest.raises(expected_exception):
        test_example_three(a, b)