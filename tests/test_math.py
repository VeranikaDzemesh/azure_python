import allure
from pytest_assume.plugin import assume

@allure.description("Check math for two")
def test_two_and_two():
    num1 = 2
    num2 = 2
    with assume:
        assert num1 + num2 == 4
    with assume:
        assert num1 * num2 == 6

