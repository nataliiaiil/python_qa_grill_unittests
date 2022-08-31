from cgi import test
import business
import pytest

class TestGrill:
#Positive scenarios
#Functional tests: meat type
    def test_meat_type_newyork(self):
        assert "New York" in business.grill("New York", 5)

    def test_meat_type_ribeye(self):
        assert "Ribeye" in business.grill("Ribeye", 10)

    def test_meat_type_tenderloin(self):
        assert "Tenderloin" in business.grill("Tenderloin", 20)

    def test_meat_type_porterhouse(self):
        assert "Porterhouse" in business.grill("Porterhouse", 20)

#Cooking time test
    def test_1_minute_cooking(self):
        assert "New York" in business.grill("New York", 1)

    def test_50_minute_cooking(self):
        assert "Ribeye" in business.grill("Ribeye", 50)

    def test_120_minute_cooking(self):
        assert "Tenderloin" in business.grill("Tenderloin", 120)
#Preparation degree: RAW
    def test_degree_raw_newyork(self):
        assert "raw" in business.grill("New York", 5)

    def test_degree_raw_ribeye(self):
        assert "raw" in business.grill("Ribeye", 4)

    def test_degree_raw_tenderloin(self):
        assert "raw" in business.grill("Tenderloin", 49)

    def test_degree_raw_porterhouse(self):
        assert "raw" in business.grill("Porterhouse", 5)
#Preparation degree: RARE
    def test_degree_rare_newyork(self):
        assert "rare" in business.grill("New York", 9)

    def test_degree_rare_ribeye(self):
        assert "rare" in business.grill("Ribeye", 6)

    def test_degree_rare_tenderloin(self):
        assert "rare" in business.grill("Tenderloin", 89)

    def test_degree_rare_porterhouse(self):
        assert "rare" in business.grill("Porterhouse", 8)
#Preparation degree: MEDIUM
    def test_degree_med_newyork(self):
        assert "medium" in business.grill("New York", 12)

    def test_degree_med_ribeye(self):
        assert "medium" in business.grill("Ribeye", 9)
#    def test_degree_med_tenderloin(self):
#        with pytest.raises(Exception) as exc_info:
#            business.grill("Tenderloin", )
#        assert "integers" in str(exc_info)
    def test_degree_med_porterhouse(self):
        assert "medium" in business.grill("Porterhouse", 9)

#Preparation degree: WELL DONE
    def test_degree_well_newyork(self):
        assert "well" in business.grill("New York", 14)

    def test_degree_well_ribeye(self):
        assert "well" in business.grill("Ribeye", 11)
#    def test_degree_well_tenderloin(self):
#        assert "well" in business.grill("Tenderloin", 89)
    def test_degree_well_porterhouse(self):
        assert "well" in business.grill("Porterhouse", 12)
#Preparation degree: BURNED
    def test_degree_burn_newyork(self):
        assert "burned" in business.grill("New York", 119)

    def test_degree_burn_ribeye(self):
        assert "burned" in business.grill("Ribeye", 119)

    def test_degree_burn_tenderloin(self):
        assert "burned" in business.grill("Tenderloin", 119)

    def test_degree_burn_porterhouse(self):
        assert "burned" in business.grill("Porterhouse", 119)

#Negative testing
#Meat_type field
    def test_field_meat_type_int(self):
        with pytest.raises(Exception) as exc_info:
            business.grill(20, 20)
        assert "meat_type should be string" in str(exc_info)

    def test_field_meat_type_bool(self):
        with pytest.raises(Exception) as exc_info:
            business.grill(True, 20)
        assert "meat_type should be string" in str(exc_info)

    def test_field_meat_type_float(self):
        with pytest.raises(Exception) as exc_info:
            business.grill(20.50, 20)
        assert "meat_type should be string" in str(exc_info)
#Cook_time_mins field
    def test_field_cook_time_float(self):
        with pytest.raises(Exception) as exc_info:
            business.grill("Ribeye", 40.50)
        assert "cook_time_mins should be int" in str(exc_info)

    def test_field_cook_time_str(self):
        with pytest.raises(Exception) as exc_info:
            business.grill("Ribeye", "String")
        assert "cook_time_mins should be int" in str(exc_info)

    def test_field_cook_time_bool(self):
        with pytest.raises(Exception) as exc_info:
            business.grill("Ribeye", False)
        assert "cook_time_mins should be int" in str(exc_info)
    
    def test_field_unknown_meat_type(self):
        with pytest.raises(Exception) as exc_info:
            business.grill("Fish", 10)
        assert "unknown meat type" in str(exc_info)
#Cook_time_mins incorrect 
    def test_0_minute_cooking(self):
        with pytest.raises(Exception) as exc_info:
            business.grill("Tenderloin", 0)
        assert "less than 1 minute" in str(exc_info)
    
    def test_121_minute_cooking(self):
        with pytest.raises(Exception) as exc_info:
            business.grill("Porterhouse", 121)
        assert "over 120 minutes" in str(exc_info)

    def test_internal_app_error(self):
        with pytest.raises(Exception) as exc_info:
            business.grill("")
        assert "internal application error" in str(exc_info)