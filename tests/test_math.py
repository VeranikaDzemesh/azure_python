import allure
from pytest_assume.plugin import assume

@allure.description("Check math for two")
def test_two_and_two():
    num1 = 2
    num2 = 2
    with assume:
        assert num1 + num2 == 4
    with assume:
        assert num1 * num2 == 4


@allure.description("Check math for three")
def test_three_and_three():
    num1 = 3
    num2 = 3
    with assume:
        assert num1 + num2 == 6
    with assume:
        assert num1 * num2 == 9


@allure.description("Check math for four")
def test_four_and_four():
    num1 = 4
    num2 = 4
    with assume:
        assert num1 + num2 == 8
    with assume:
        assert num1 * num2 == 16