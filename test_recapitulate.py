import unittest

import Recapitulate as RecapitulateClass

class Test(unittest.TestCase):

    recapitulate = RecapitulateClass.Recapitulate()

    def test_0_basic_lists(self):
        print('Start test...')

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

if __name__ == '__main__':
    unittest.main()