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
    def test_degree_raw_newyork_low(self):
        r = business.grill("New York", 1)
        assert "raw" in r
        assert "not good" in r

    def test_degree_raw_newyork_high(self):
        r = business.grill("New York", 8)
        assert "raw" in r
        assert "not good" in r

    def test_degree_raw_ribeye_low(self):
        r = business.grill("Ribeye", 1)
        assert "raw" in r
        assert "not good" in r

    def test_degree_raw_ribeye_high(self):
        r = business.grill("Ribeye", 5)
        assert "raw" in r
        assert "not good" in r

    def test_degree_raw_tenderloin_low(self):
        r = business.grill("Tenderloin", 1)
        assert "raw" in r
        assert "not good" in r

    def test_degree_raw_tenderloin_high(self):
        r = business.grill("Tenderloin", 50)
        assert "raw" in r
        assert "not good" in r

    def test_degree_raw_porterhouse_low(self):
        r = business.grill("Porterhouse", 1)
        assert "raw" in r
        assert "not good" in r

    def test_degree_raw_porterhouse_high(self):
        r = business.grill("Porterhouse", 6) 
        assert "raw" in r
        assert "not good" in r
#Preparation degree: RARE
    def test_degree_rare_newyork_low(self):
        assert "rare" in business.grill("New York", 9)

    def test_degree_rare_newyork_high(self):
        assert "rare" in business.grill("New York", 10)    

    def test_degree_rare_ribeye_low(self):
        assert "rare" in business.grill("Ribeye", 6)

    def test_degree_rare_ribeye_high(self):
        assert "rare" in business.grill("Ribeye", 7)

    def test_degree_rare_tenderloin_low(self):
        assert "rare" in business.grill("Tenderloin", 51)

    def test_degree_rare_tenderloin_high(self):
        assert "rare" in business.grill("Tenderloin", 90)

    def test_degree_rare_porterhouse_low(self):
        assert "rare" in business.grill("Porterhouse", 7)

    def test_degree_rare_porterhouse_high(self):
        assert "rare" in business.grill("Porterhouse", 8) 
#Preparation degree: MEDIUM
    def test_degree_med_newyork_low(self):
        assert "medium" in business.grill("New York", 11)

    def test_degree_med_newyork_high(self):
        assert "medium" in business.grill("New York", 12)    

    def test_degree_med_ribeye_low(self):
        assert "medium" in business.grill("Ribeye", 8)

    def test_degree_med_ribeye_high(self):
        assert "medium" in business.grill("Ribeye", 9)    

    def test_degree_med_porterhouse_low(self):
        assert "medium" in business.grill("Porterhouse", 9)

    def test_degree_med_porterhouse_high(self):
        assert "medium" in business.grill("Porterhouse", 10)    

#Preparation degree: WELL DONE
    def test_degree_well_newyork_low(self):
        assert "well" in business.grill("New York", 13)

    def test_degree_well_newyork_high(self):
        assert "well" in business.grill("New York", 14)

    def test_degree_well_ribeye_low(self):
        assert "well" in business.grill("Ribeye", 10)

    def test_degree_well_ribeye_high(self):
        assert "well" in business.grill("Ribeye", 11)

    def test_degree_well_porterhouse_low(self):
        assert "well" in business.grill("Porterhouse", 11)

    def test_degree_well_porterhouse_high(self):
        assert "well" in business.grill("Porterhouse", 13)
#Preparation degree: BURNED
    def test_degree_burn_newyork_low(self):
        r = business.grill("New York", 15)
        assert "burned" in r
        assert "not good" in r

    def test_degree_burn_newyork_high(self):
        r = business.grill("New York", 120)
        assert "burned" in r
        assert "not good" in r

    def test_degree_burn_ribeye_low(self):
        r = business.grill("Ribeye", 12)
        assert "burned" in r
        assert "not good" in r
    
    def test_degree_burn_ribeye_high(self):
        r = business.grill("Ribeye", 120)
        assert "burned" in r
        assert "not good" in r

    def test_degree_burn_tenderloin_low(self):
        r = business.grill("Tenderloin", 119)
        assert "burned" in r
        assert "not good" in r

    def test_degree_burn_tenderloin_high(self):
        r = business.grill("Tenderloin", 91)
        assert "burned" in r
        assert "not good" in r  

    def test_degree_burn_porterhouse(self):
        r = business.grill("Porterhouse", 120)
        assert "burned" in r
        assert "not good" in r      
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