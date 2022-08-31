from cgi import test
import business
import pytest

class TestGrill:
#Positive scenarios
#Functional tests: meat type
    def test_correct_meat_type_newyork(self):
        assert "New York" in business.grill("New York", 5)
    def test_correct_meat_type_ribeye(self):
        assert "Ribeye" in business.grill("Ribeye", 10)
    def test_correct_meat_type_tenderloin(self):
        assert "Tenderloin" in business.grill("Tenderloin", 20)
    def test_correct_meat_type_porterhous(self):
        assert "Porterhouse" in business.grill("Porterhouse", 20)

    