
# this module contains utility functions
from typing import Optional, Any,  Dict, List
import re
import base64
import logging
import os

from pandas import DataFrame

from collections import Counter
import pm4py
from pm4py.objects.dfg.obj import DFG
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.log.importer.xes.variants import iterparse, line_by_line
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.util import dataframe_utils

from visualization_data import VisualizationData

#LOGSTRING_VALID_REGEX = "^\s*(\s*<\s*(([a-zA-Z]+\s*,\s*)*)>+\s*\d*\s*;)+\s*$"
LOGSTRING_VALID_REGEX = "^(<((([a-zA-Z]+,)*[a-zA-Z]+)|())>\d*;)+$"
pattern = re.compile(LOGSTRING_VALID_REGEX)


def check_validity_of_logstr(logstring: str) -> bool:
    """ This method validates if a logstring is valid or not, this is done to a regular expression
    capturing the correctness of logstrings 
    
    Args:
        logstring (str) : The logstring which validity is checked
        
    Returns: 
        bool : True if the logstring is valid, False if not
    """    

    if pattern.match(logstring.replace(' ', '')):
        return True
    else: 
        return False
    

def read_xes_to_log(xes_file) -> DataFrame:
    """ This method converts a xes file to an event log, currently it converts it to a DataFrame
        as the pm4py framework is transitioning to it as a general data format.

    Args:
        xes_file : A xes file 

    Returns:
        DataFrame: The log that has been converted to the DataFrame representation
    """
    logging.info("converting xes file ...")
    log = _import_log(xes_file)
    logging.info("conversion of xes file done.")
    # following lines taken from read_xes function
    log = log_converter.apply(log, variant=log_converter.Variants.TO_DATA_FRAME)
    log = dataframe_utils.convert_timestamp_columns_in_df(log)
    return log


def convert_dfg_to_d3(dfg: DFG, dfg_groups_inverted: Dict) -> Dict:
    """ This method connverts a DFG error to the data format needed by the D3 graph in the front-end

    Args:
        dfg (DFG): DFG object listing all pairs with the respective counts for each dfg relation
        dfg_groups_inverted (Dict): The inverted Dict containing the groups of the cut each 

    Raises:
        e: _description_

    Returns:
        str: _description_
    """
    dfg_dict = {}
    links_ls, nodes_ls = [], [] 
    nodes_dict = {"start": 0, "end": 1}
    nodes_dict_counter = 2 # two so it is possible to have a start and end node
    try:
        
        def run_pair(pair, count, nodes_dict_counter):
            for node_val in pair:
                if node_val not in nodes_dict:
                    nodes_dict[node_val] = nodes_dict_counter
                    nodes_dict_counter += 1
            links_ls.append({"source": nodes_dict.get(pair[0]), "target": nodes_dict.get(pair[1]), 
                            "count" : count})
            return nodes_dict_counter
        
        for start_activity, count in dfg.start_activities.items():
            nodes_dict_counter = run_pair(("start", start_activity), count, nodes_dict_counter)
        
        for end_activity, count in dfg.end_activities.items():
            nodes_dict_counter = run_pair((end_activity, "end"), count, nodes_dict_counter)
        
        for pair, count in dfg.graph.items():
            nodes_dict_counter = run_pair(pair, count, nodes_dict_counter)
        
        for node_key, node_value in nodes_dict.items():
            # TODO group assignment --> only uncomment following lines when frontend legend is visible for groups
            # then also don't forget to change the assignment in process_tree_node.py !
            
            # here also the weight can be added 
            if node_key in dfg_groups_inverted.keys():
                group_no = dfg_groups_inverted[node_key] 
            elif node_key == "start" or node_key == "end":
                group_no = 0
            else:
                group_no = 0 # having group number = 0 for other group ( also for start / end nodes)
            # group_no = dfg_groups_inverted[node_key]
            
            nodes_ls.append({"id": node_value, "group": group_no, "value": node_key})
    
            dfg_dict["nodes"] = nodes_ls
            dfg_dict["links"] = links_ls
    
    except Exception as e:
        print("error in creating the json file from dfg to d3 ")
        #print(e)
        raise e
    #print(dfg_dict)
    return dfg_dict


def convert_log_to_json(log: Counter) -> List:
    """ With this method  a log compiled in  the Counter class format is converted to a List
        that then can be converted to a json. This is done to prepare for displaying the traces 
        in the front-end. 

    Args:
        log (Counter): The log in form of a Counter object 

    Returns:
        List: list of dictionaries each containing the trace with the respective count
    """
    traces_ls = []
    if hasattr(log, "items") and callable(log.items):
        for trace, count in log.items():
            traces_ls.append({"trace": str(trace).replace("'", "").replace("(", "<").replace(")", ">"), 
                            "count": str(count)})
    return traces_ls


def convert_to_json(visualization_data: VisualizationData) -> Dict:
    """ This method converts the VisualizationData object to a dictionary that can be converted to 
        a json for a request. 

    Args:
        visualization_data (VisualizationData): A VisualizationData object containing all the 
        necessary information for display in the front-end

    Returns:
        Dict: Dictionary having a "all_steps_list" attribute containing a list of steps and each of 
        those sub-dicts contains all information belonging to a certain step. 
        Also the petri-net picture is attached as a sibling attribute of the steps list. 
        (process_tree_image)
        
        Each step has:
        step = step number of the proces tree traversal
        label = label that names what action is performed at the step
        case_type = The type of case applied for example a CUT
    """
    json_dict = {}
    all_steps_ls = []
    for vis_step in visualization_data.traverse_ls:
        vis_object = vis_step[1]
        cur_pt = vis_object.pt_str
        cur_dfg = convert_dfg_to_d3(vis_object.dfg, vis_object.dfg_groups_inverted)
        step_dict = {}
        step_dict["step"] = str(vis_step[0])
        step_dict["label"] = vis_object.label
        step_dict["case_type"] = vis_object.case_type
        step_dict["cur_tree"] = cur_pt
        step_dict["cur_dfg"] = cur_dfg
        step_dict["cur_dfg_groups"] = vis_object.dfg_groups_inverted
        step_dict["cur_traces"] = convert_log_to_json(vis_object.cur_log)
        
        all_steps_ls.append(step_dict)
        # print(step_dict)
    json_dict["all_steps_list"] = all_steps_ls
    json_dict["process_tree_image"] = visualization_data.petri_net_image
    # print("json is: {}".format(json_dict))
    return json_dict


def convert_data_to_base64(data_str: str, encoding='utf-8'):
    """ This method converts data from a string to base64 encoding and decodes it to remove byte 
        representation

    Args:
        data_str (str): the string to be converted to base64
        encoding (str, optional): The encoding to use. Defaults to 'utf-8'.

    Returns:
        _type_: base64 representation of string converted as string again  
    """
    return base64.b64encode(data_str.encode(encoding)).decode(encoding)


def convert_petri_net_to_image(petri_net: PetriNet, initial_marking: Optional[Marking] = None,
                final_marking: Optional[Marking] = None, format: str = "png", bgcolor: str = "white",
                decorations: Dict[Any, Any] = None):
    """
    converts a petri net to a picture and returns this visualization (the function is mainly copied
    from pm4py.vis -> view_petri_net)

    :param petri_net: Petri net
    :param initial_marking: Initial marking
    :param final_marking: Final marking
    :param format: Format of the output picture (default: png)
    :param bgcolor: Background color of the visualization (default: white)
    :param decorations: Decorations (color, label) associated to the elements of the Petri net

    .. code-block:: python3

        import pm4py

        net, im, fm = pm4py.discover_petri_net_inductive(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
        pm4py.convert_petri_net_to_image(net, im, fm, format='svg')
    """
    gviz = pn_visualizer.apply(petri_net, initial_marking, final_marking,
                            parameters={pn_visualizer.Variants.WO_DECORATION.value.Parameters.FORMAT: format,
                                        "bgcolor": bgcolor, "decorations": decorations})
    svg_string = gviz.pipe(encoding='utf-8').replace("\n", "")
    return svg_string


def _import_log(f, parameters=None):
    """
    This is copied from iterparse / line_by_line and read.py from the importer.xes.(variants) package
    TODO the original method should incorporate / support streams 
    
    Imports an XES file into a log object

    Parameters
    ----------
    f:
        xes file
    parameters
        Parameters of the algorithm, including
            Parameters.TIMESTAMP_SORT -> Specify if we should sort log by timestamp
            Parameters.TIMESTAMP_KEY -> If sort is enabled, then sort the log by using this key
            Parameters.REVERSE_SORT -> Specify in which direction the log should be sorted
            Parameters.MAX_TRACES -> Specify the maximum number of traces to import from the log (read in order in the XML file)
            Parameters.SHOW_PROGRESS_BAR -> Enables/disables the progress bar (default: True)
            Parameters.ENCODING -> regulates the encoding (default: utf-8)

    Returns
    -------
    log : :class:`pm4py.log.log.EventLog`
        A log
    """
    from lxml import etree

    if parameters is None:
        parameters = {}

    encoding = iterparse.exec_utils.get_param_value(iterparse.Parameters.ENCODING, parameters, iterparse.constants.DEFAULT_ENCODING)
    #show_progress_bar = iterparse.exec_utils.get_param_value(iterparse.Parameters.SHOW_PROGRESS_BAR, parameters, True)
    # is_compressed = filename.lower().endswith(".gz")

    # if iterparse.pkgutil.find_loader("tqdm") and show_progress_bar:
    #     if is_compressed:
    #         f = iterparse.gzip.open(filename, "rb")
    #     else:
    #         f = open(filename, "rb")
    #     context = etree.iterparse(f, events=[iterparse._EVENT_START, iterparse._EVENT_END], encoding=encoding)
    #     num_traces = iterparse.count_traces(context)
    # else:
    #     # avoid the iteration to calculate the number of traces is "tqdm" is not used
    num_traces = 0

    # if is_compressed:
    #     f = iterparse.gzip.open(filename, "rb")
    # else:
    #     f = open(filename, "rb")
    

    from pm4py.objects.log.importer.xes import importer as xes_importer
    context = etree.iterparse(f, events=[iterparse._EVENT_START, iterparse._EVENT_END], encoding=encoding)
    if iterparse.pkgutil.find_loader("lxml"):
        return iterparse.import_from_context(context, num_traces, parameters=parameters)
    else:
        # else using standard line by line parsing
        file_size = os.stat(f.fileno()).st_size
        return line_by_line.import_log_from_file_object(f, encoding, file_size=file_size, parameters=parameters)

        
