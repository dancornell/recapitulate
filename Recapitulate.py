from enum import Enum
import logging
from ordered_enum import OrderedEnum
import pandas as pd

class ColumnDataType(OrderedEnum):
    UNKNOWN = 9999
    STRING = 1000
    FLOATINGPOINT = 2000
    INTEGER = 3000


class Recapitulate:

    def __init__(self, excel_file_name):
        logging.basicConfig(level=logging.DEBUG)
        self.excel_file_name = excel_file_name
        logging.debug('excel_file_name: ' + self.excel_file_name)

    def determineDataTypeFromList(my_list):
        '''Looks at a list and attempts to determine the type of data in the list - integers, floating point numbers, or strings
        
        Keyword arguments:
        my_list -- list of data items to evaluate
        '''
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

    def parse_excel_data(self):
        logging.debug('Starting parse_excel_data()')

        ret_val = { }

        xl = pd.ExcelFile(self.excel_file_name)
        sheet_names = xl.sheet_names
        for sheet in sheet_names:
            logging.debug('Working with sheet: ' + sheet)
            my_sheet = pd.read_excel(self.excel_file_name, sheet_name=sheet, header=0)
            
            ret_val[sheet] = 'PLACEHOLDER'

        logging.debug('Finished parse_excel_data()')

        return(ret_val)


Recapitulate.determineDataTypeFromList = staticmethod(Recapitulate.determineDataTypeFromList)



