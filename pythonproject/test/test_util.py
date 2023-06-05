import unittest
import base64

from pm4py.objects.log.importer.xes import importer as xes_importer

from util import *


class TestUtilModule(unittest.TestCase):
    def test_check_validity_of_logstr(self):
        test_dict = {"<>1;": True, "<a,b>;": True, " <a>1;": True, "< a>1;": True, "<a >1;": True, 
                    "<a> 1;": True, "<a>1 ;": True, "<a>1; ": True, "<a,b,c>1;": True, 
                    "<a,b,c>1; < a,b , c > 1 ; ": True, "<a,b,c>20; < a>  ; ": True, 
                    "<a,b,c>20.0; < a>  ; ": False,  "<a,b,c>20; < a> ": False, 
                    "<a,Z,c>20; < abssdf> 1;": True, "<a,Z,c>20 <a,b,c> 1;": False, 
                    "a,Z,c>2; <a,b,c> 1;": False, "<a,Z,c 20 <a,b,c> 1;": False, 
                    "<a,Z,c 20 <a,b c> 1;": False}
        for key, value in test_dict.items():
            print("traces: " + key + " should be: " + str(value))
            self.assertEqual(check_validity_of_logstr(key), value)

    def test_read_xes_to_log(self):
        xes_file =  "./test/current_log.xes"
        log_df = read_xes_to_log(xes_file=xes_file)
        print(log_df)
        self.assertEqual(log_df.loc[:, "concept:name"].to_list()[0], 'a')
        print("done")
        
    def test_convert_dfg_to_d3(self):
        print("test convert_dfg_to_d3")
        dfg = DFG({('a', 'b'): 5, ('b', 'c'): 5, ('c', 'd'): 5}, {'a': 5}, {'d': 5})
        dfg_groups_inverted = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        d3_result = convert_dfg_to_d3(dfg, dfg_groups_inverted=dfg_groups_inverted)
        first_elem = d3_result['nodes'][0]
        self.assertEqual(first_elem.get('value'), 'start')
        second_elem = d3_result['nodes'][1]
        self.assertEqual(second_elem.get('value'), 'end')
        third_elem = d3_result['nodes'][2]
        self.assertEqual(third_elem.get('value'), 'a')
        self.assertEqual(third_elem.get('group'), 1)
        self.assertEqual(third_elem.get('id'), 2)
        
    def test_convert_log_to_json(self):
        log_counter = Counter({('a', 'b', 'c'): 5, ('a', 'c', 'd'): 10})
        res_traces_ls = convert_log_to_json(log=log_counter)
        self.assertEqual((res_traces_ls[0]).get('trace'), '<a, b, c>')
        self.assertEqual((res_traces_ls[0]).get('count'), '5')
        print(res_traces_ls[0])
        
    def test_convert_data_to_base64(self):
        data_str = 'asdf'
        encoding = 'utf-8'
        return_str = convert_data_to_base64(data_str=data_str, encoding=encoding)
        decoded_str = base64.b64decode(return_str).decode(encoding=encoding)
        print(decoded_str)
        self.assertEqual(decoded_str, data_str)
    
    
    
if __name__ == '__main__':
    unittest.main()