from main import example_two
import pytest

@pytest.mark.parametrize("a, b, x, y, expected_result", [(2, 3, 4, 5, 2),
                                                         (1, 2, 3, 4, 1),
                                                         (10, 100, 5, 5, 5),
                                                         (1.0, 1.0, 0.5, 100, 0.5),
                                                         (10, 5, 1, 5, 1)])
def test_example_two(a, b, x, y, expected_result):
    assert example_two(a, b, x, y) == expected_result


@pytest.mark.parametrize("expected_exception, a, b, x, y", [
                                                            (TypeError, "2", 3, 5, 7),
                                                            (TypeError, 2, 2, 5, "7")])
def test_zero_division(expected_exception, a, b, x, y):
    # в этом контексте мы ожидаем получить ошибку
    with pytest.raises(expected_exception):
        example_two(a, b, x, y)