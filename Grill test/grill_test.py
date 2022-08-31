from cgi import test
import business
import pytest

class TestGrill:
#Positive scenarios
#Functional tests
    def test_correct_meat_type(self):
        assert "New York" in business.grill("New York", 5)
