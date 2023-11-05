from main import example_one
import pytest

@pytest.mark.parametrize("x, y, result", [(1, 1, 0),
                                          (1, 0, 1),
                                          (0, 1, 1),
                                          (0, 0, 0)])
def test_example_one_good(x, y, result):
    assert example_one(x, y) == result


@pytest.mark.parametrize("expected_exception, x, y", [
                                                     (TypeError, "1", 0),
                                                     (TypeError, "1", "1"),
                                                     (TypeError, "0", 1),
                                                     (TypeError, 1, "0")])
def test_example_one_bad(expected_exception, x, y):
    # в этом контексте мы ожидаем получить ошибку
    with pytest.raises(expected_exception):
        test_example_one_good(x, y)