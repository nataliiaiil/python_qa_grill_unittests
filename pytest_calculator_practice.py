import pytest

def math(num1, operator, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception("Use only integers for math!")
    
    if operator == "+":
        result = num1 + num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1 / num2 
    else:
        raise Exception(f"'{operator}' is not a math operator. Please use math operators")

    if result < 0:
        return "A negative numbers are not supported in this app"
    elif result < 10:
        return "A small number. It's OK"
    elif result < 20:
        return "A medium number"
    else: 
        return "A big number"

class TestMath:
        
    def test_non_int_input_for_num1(self):
        with pytest.raises(Exception) as exc_info:
            math('hi', '+', 3)
        assert "integers" in str(exc_info)

    def test_non_int_input_for_num2(self):
        with pytest.raises(Exception) as exc_info:
            math(2, '+', "in")
        assert "integers" in str(exc_info)
#addition
    def test_addition_with_negative_result(self):
        assert "negative numbers" in math(-10, '+', 2)

    def test_addition_with_small_result(self):
        assert "small number" in math(2, '+', 2)

    def test_addition_with_med_result(self):
        assert "medium" in math(9, '+', 9)

    def test_addition_with_big_result(self):
        assert "big" in math(21, '+', 10)
#multiplication
    def test_multi_with_negative_result(self):
        assert "negative numbers" in math(-10, '*', 2)

    def test_multi_with_small_result(self):
        assert "small number" in math(2, '*', 2)

    def test_multi_with_med_result(self):
        assert "medium" in math(2, '*', 9)

    def test_multi_with_big_result(self):
        assert "medium" in math(3, '*', 5)
#substraction
    def test_sub_with_negative_result(self):
        assert "negative numbers" in math(0, '-', 2)

    def test_sub_with_small_result(self):
        assert "small number" in math(5, '-', 2)

    def test_sub_with_med_result(self):
        assert "medium" in math(20, '-', 5)

    def test_sub_with_big_result(self):
        assert "big" in math(50, '-', 10)
#division
    def test_div_with_negative_result(self):
        assert "negative numbers" in math(-8, '/', 2)

    def test_div_with_small_result(self):
        assert "small number" in math(6, '/', 2)

    def test_div_with_med_result(self):
        assert "medium" in math(30, '/', 2)

    def test_div_with_big_result(self):
        assert "big" in math(100, '/', 2)

    def test_invalid_operator(self):
        with pytest.raises(Exception) as exc_info:
            math(4, 'j', 3)
        assert "is not a math operator" in str(exc_info)