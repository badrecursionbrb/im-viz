import unittest
import base64

from pm4py.objects.log.importer.xes import importer as xes_importer

from log_from_string.string_to_log import string_to_log
from main import main


class TestUtilModule(unittest.TestCase):
    def test_main(self):
        logstr = "<a,b,c,e,f>10;<a,d,b,c,d,e,f,g>1;<a,d,c,e,c,e,f>10;<a,d,e,c,d,e,f>10;<a,d,c,d,e,f>10"
        request_args = {"algorithm": "im_standard"}
        log = string_to_log(logstr)
        ret_val = main(log, request_args=request_args)
        all_steps_ls = ret_val.get('all_steps_list')
        print((all_steps_ls[0]).keys())
        print((all_steps_ls[0]).get('cur_dfg'))
        print((all_steps_ls[0]).get('cur_traces'))
        print((all_steps_ls[0]).get('cur_dfg_groups'))
        print((all_steps_ls[0]).get('cur_tree'))

        for step_data in all_steps_ls:
            print(step_data.get('step') + ' label: ' + str(step_data.get('label')) + 
                ' case_type: ' + str(step_data.get('case_type')) + ' ')
        
        print((all_steps_ls[-1]).get('cur_tree'))
        
        self.assertEqual(ret_val, 0)
        
        request_args = {"algorithm": "im_infrequent", "threshold": 0.2}
        ret_val = main(log, request_args=request_args)
        self.assertEqual(ret_val, 0)
        print("done")
    
    
    
if __name__ == '__main__':
    unittest.main()