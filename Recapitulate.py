from enum import Enum
from ordered_enum import OrderedEnum

class ColumnDataType(OrderedEnum):
    UNKNOWN = 9999
    STRING = 1000
    FLOATINGPOINT = 2000
    INTEGER = 3000


class Recapitulate:
    def determineDataTypeFromList(my_list):
        ret_val = ColumnDataType.UNKNOWN

        if my_list is None:
            my_list = []

        for my_item in my_list:

            if ret_val == ColumnDataType.UNKNOWN or ret_val == ColumnDataType.INTEGER:
                try:
                    my_val = int(my_item)
                    ret_val = ColumnDataType.INTEGER
                except ValueError as v:
                    # Not an integer. Bump to float
                    ret_val = ColumnDataType.FLOATINGPOINT
            
            if ret_val == ColumnDataType.FLOATINGPOINT:
                try:
                    my_val = float(my_item)
                except ValueError as v:
                    # Not a float. Bump to string and get out
                    ret_val = ColumnDataType.STRING
                    break

        return(ret_val)

Recapitulate.determineDataTypeFromList = staticmethod(Recapitulate.determineDataTypeFromList)



