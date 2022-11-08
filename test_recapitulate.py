import unittest

import Recapitulate as RecapitulateClass

class Test(unittest.TestCase):

    recapitulate = RecapitulateClass.Recapitulate('./data/TestCasesSpreadsheet1.xlsx')

    def test_0_basic_lists(self):
        print('Start test test_0_basic_lists()')

        empty_list = []
        all_string_list = ['String1', 'String2', 'String3']
        all_int_list = ['1', '2', '3']
        all_float_list = ['1.1', '2.2', '3.3']
        float_with_string_list = ['1.1', 'String1', '2.2']
        int_with_string_list = ['1', 'String1', '2']
        int_with_float_list = ['1', '2.2', '3']
        int_with_blank_list = ['1', '', '3']

        ret_val = self.recapitulate.determineDataTypeFromList(None)
        print('None: ' + str(None) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.UNKNOWN)

        ret_val = self.recapitulate.determineDataTypeFromList(empty_list)
        print('empty_list: ' + str(empty_list) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.UNKNOWN)

        ret_val = self.recapitulate.determineDataTypeFromList(all_string_list)
        print('all_string_list: ' + str(all_string_list) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.STRING)

        ret_val = self.recapitulate.determineDataTypeFromList(all_int_list)
        print('all_int_list: ' + str(all_int_list) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.INTEGER)

        ret_val = self.recapitulate.determineDataTypeFromList(all_float_list)
        print('all_float_list: ' + str(all_float_list) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.FLOATINGPOINT)

        ret_val = self.recapitulate.determineDataTypeFromList(float_with_string_list)
        print('float_with_string_list: ' + str(float_with_string_list) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.STRING)

        ret_val = self.recapitulate.determineDataTypeFromList(int_with_string_list)
        print('int_with_string_list: ' + str(int_with_string_list) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.STRING)

        ret_val = self.recapitulate.determineDataTypeFromList(int_with_float_list)
        print('int_with_float_list: ' + str(int_with_float_list) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.FLOATINGPOINT)

        # TODO - Determine if we like this behavior - where a blank string will cause the data type to be String
        ret_val = self.recapitulate.determineDataTypeFromList(int_with_blank_list)
        print('int_with_blank_list: ' + str(int_with_blank_list) + ' ret_val: ' + str(ret_val))
        self.assertEqual(ret_val, RecapitulateClass.ColumnDataType.STRING)

        print('Finished with test')

    def test_1_excel_sheet(self):
        print('Start test test_1_excel_sheet()')

        ret_val = self.recapitulate.parse_excel_data()

        tab_count = len(ret_val.data_sets)
        print('Make sure there are 6 tabs')
        self.assertEqual(tab_count, 6)

        print('Make sure we got the right tab names')
        data_sets = ret_val.data_sets
        self.assertEqual(data_sets[0].name, 'Basic')
        self.assertEqual(data_sets[1].name, 'Titles')
        self.assertEqual(data_sets[2].name, 'Sheet Name With Spaces')
        self.assertEqual(data_sets[3].name, 'Sheet `~!@#$%^&()_-+={}|;"')
        self.assertEqual(data_sets[4].name, 'Sheet \'<,>.')
        self.assertEqual(data_sets[5].name, 'Sheet 1234567890 With Number')
        
        
        

        print('Check the columns in the Basic sheet to make sure the data types are right')

        print('Finished with test')


if __name__ == '__main__':
    unittest.main()