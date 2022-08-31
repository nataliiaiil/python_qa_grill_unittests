import enum
from enum import Enum
from tokenize import String

"""
__Requirements Documentation__

Absctract:
The function that needs to be developed is called "grill".
This function has to receive a type of meat that a user wants to grill 
and the amount of time (in minutes) that the user wants to grill it for.

Constraints:
- We only support the following types of meat: New York, Ribeye, Tenderloin, Porterhouse. 
If any other meat is provided by user - throw exception with text 'unknown meat type'.
- We only support cooking from 1 to 120 minutes. 
If cooking time is less than 1 minute - throw exception with text 'cooking for less than 1 minute is prohibited'.
If cooking time is more than 120 minutes - throw exception with text 'cooking for over 120 minutes is prohibited'.
- We only support 5 types of preparation degree of meat: raw, rare, medium, well done, burned. 
If any other degree is returned from the function - it is a bug and it should be reported to the manager.
- When executed successfully, the function should return the following string: 'Your MEAT_TYPE is cooked PREPARATION_DEGREE'
For example 'Your Tenderloin is cooked rare'
- If the meat is 'raw' or 'burned' - add the following text to the end '- not good' to let the user know that the meat is not fit for consumption.
For example 'Your Tenderloin is cooked burned - not good'
- Each meat type cooking time and preparation degree should be the same as in this table

+-------------+----------+-----------+-----------+-----------+------------+
|  Meat Type  |   Raw    |   Rare    |  Medium   | Well Done |   Burned   |
+-------------+----------+-----------+-----------+-----------+------------+
| New York    | 0-8 min  | 9-10 min  | 11-12 min | 13-14 min | 15-120 min |
| Ribeye      | 0-5 min  | 6-7 min   | 8-9 min   | 10-11 min | 12-120 min |
| Tenderloin  | 0-50 min | 51-90 min | --------- | --------- | 91-120 min |
| Porterhouse | 0-6 min  | 7-8 min   | 8-10 min  | 11-13 min | 14-120 min |
+-------------+----------+-----------+-----------+-----------+------------+

If the function returns preparation degree that is different from the table values - this is a bug and needs to be reported to the manager.

Technical constraints:
- The meat_type should only be of string type. If it is not - throw exception with text 'meat_type should be string'.
- The cooking time should be provided in minutes and only be of int type. If it is not - throw exception with text 'cook_time_mins should be int'.
- If an unexpected error happens - throw exception with text 'internal application error'. 
If this message gets returned this is a bug and should be reported to manager.

Happy path:
- User calls the 'grill' function with meat type: 'New York' and cooking time of 11 minutes.
- The 'grill' function returns the following message 'Your New York is cooked medium'

Technical documentation:
- Function signature
def grill(meat_type: string, cook_time_mins: int)
- To call the function type the following code
grill('New York', 11)
"""

class PreparationDegree(Enum):
    RAW = 1
    RARE = 2
    MEDIUM = 3
    WELL_DONE = 4
    BURNED = 5

preparation_degree_description = {
    PreparationDegree.RAW: "raw - not good",
    PreparationDegree.RARE: "rare",
    PreparationDegree.MEDIUM: "medium",
    PreparationDegree.WELL_DONE: "well done",
    PreparationDegree.BURNED: "burned - not good"
}

class CookingPeriod:
    def __init__(self, start_min, end_min, degree) -> None:
        self.start_min = start_min
        self.end_min = end_min
        self.degree = degree     

meat_types = {
    'New York': [
        CookingPeriod(0, 8, PreparationDegree.RAW),
        CookingPeriod(9, 10, PreparationDegree.RARE),
        CookingPeriod(11, 12, PreparationDegree.MEDIUM),
        CookingPeriod(13, 14, PreparationDegree.WELL_DONE),
        CookingPeriod(15, 120, PreparationDegree.BURNED),
    ],
    'Ribeye': [
        CookingPeriod(0, 5, PreparationDegree.RAW),
        CookingPeriod(6, 7, PreparationDegree.RARE),
        CookingPeriod(8, 9, PreparationDegree.MEDIUM),
        CookingPeriod(10, 11, PreparationDegree.WELL_DONE),
        CookingPeriod(12, 120, PreparationDegree.BURNED),
    ],
    'Tenderloin': [
        CookingPeriod(0, 50, PreparationDegree.RAW),
        CookingPeriod(51, 90, PreparationDegree.RARE),
        CookingPeriod(91, 120, PreparationDegree.BURNED),
    ],
    'Porterhouse': [
        CookingPeriod(0, 6, PreparationDegree.RAW),
        CookingPeriod(7, 8, PreparationDegree.RARE),
        CookingPeriod(8, 10, PreparationDegree.MEDIUM),
        CookingPeriod(11, 13, PreparationDegree.WELL_DONE),
        CookingPeriod(14, 120, PreparationDegree.BURNED),
    ],
}

def grill(meat_type, cook_time_mins):
    if not isinstance(meat_type, str):
        raise Exception('meat_type should be string')

    if not isinstance(cook_time_mins, int) or isinstance(cook_time_mins, bool):
         raise Exception('cook_time_mins should be int')

    if meat_type not in meat_types:
        raise Exception('unknown meat type')
    
    if cook_time_mins > 120:
        raise Exception('cooking for over 120 minutes is prohibited')

    if cook_time_mins < 1:
        raise Exception('cooking for less than 1 minute is prohibited')

    meat_cooking_periods = meat_types[meat_type]

    for cooking_period in meat_cooking_periods:
        if cook_time_mins >= cooking_period.start_min and cook_time_mins <= cooking_period.end_min:
            return "Your {} is cooked {}".format(meat_type, preparation_degree_description[cooking_period.degree])

    raise Exception('internal application error')
