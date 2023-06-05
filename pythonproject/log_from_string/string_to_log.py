"""
The contents of this file handle with the conversion of a logsting to a log object 

The content was provided by the chair of Artifical Intelligence Methods at the University of 
Mannheim
    """
from typing import List

from pm4py.objects.log.obj import Event, Trace, EventLog
from datetime import datetime


def list_to_trace(activity_list: List, case_id) -> Trace:
    # input is e.g., a list [a, b, c, d]
    event_list = []
    for activity in activity_list:
        event_list.append(Event({"concept:name": activity, "time:timestamp": datetime.fromtimestamp(0)}))
    trace = Trace(event_list)
    trace.attributes['concept:name'] = str(case_id)
    return trace


def _string_to_trace(trace_string: str) -> Trace:
    # Expected String format is "<a,b,c,d>;<a,b,c,e>10" (numbers can be used to indicate counts
    #    WARNING: There is very little sanity checking on here
    return Trace(
        [Event({"concept:name": label.strip(), "time:timestamp": datetime.fromtimestamp(0)}) for label in trace_string.split(',')])


def string_to_log(log_string: str) -> EventLog:
    """ Method to convert a logstring to an EventLog

    Args:
        log_string (str): 

    Returns:
        EventLog: logstring that has been converted to 
    """
    log_string = log_string.strip().replace(' ', '')
    log = EventLog()
    if log_string.endswith(';'):
        log_string = log_string[:-1]
    trace_strings = log_string.split(';')
    case_id = 0
    for trace_str in trace_strings:
        trace_str = trace_str.strip()
        trace_str = trace_str.replace('<', '')
        (trace_str, count) = trace_str.split('>')
        if not count:
            count = 1
        for i in range(int(count)):
            case_id += 1
            trace = _string_to_trace(trace_str)
            trace.attributes['concept:name'] = str(case_id)
            log.append(trace)
    return log