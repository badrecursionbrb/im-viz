import unittest

from pm4py.objects.log.exporter.xes import exporter as xes_exporter
from pm4py.objects.log.importer.xes import importer as xes_importer

from log_from_string.string_to_log import string_to_log


class TestStringToLog(unittest.TestCase):
    def test_string_to_log_export(self):
        # Input log string
        logstr = "<a,b,c,b,f,g,h>50;<a,b,e,h,g>60;<d,f,h,g>60;<d,e,g,h>50;a,b,a,e,h,g>2"
        
        # Convert the string to a log object
        log = string_to_log(logstr)
        
        # Export the log object to a XES file
        xes_exporter.apply(log, './test/last_log.xes')
        
        # Import the XES file as a log object
        imported_log = xes_importer.apply('./test/last_log.xes')
        
        # Assert that the number of traces in the original log and the imported log are the same
        self.assertEqual(len(log), len(imported_log))
        
        # Assert that the number of events in each trace of the original log and the imported log are the same
        for original_trace, imported_trace in zip(log, imported_log):
            self.assertEqual(len(original_trace), len(imported_trace))

if __name__ == '__main__':
    unittest.main()
    
