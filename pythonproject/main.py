import logging
from typing import Dict, Union

from pandas import DataFrame
from pm4py.convert import convert_to_petri_net
from pm4py.algo.discovery.inductive.algorithm_modified_v2 import Variants
from pm4py.algo.discovery.inductive.variants.imf_custom import IMFParameters
from pm4py.objects.log.obj import EventLog

from log_from_string.string_to_log import string_to_log
from util import convert_data_to_base64
from visualization_data import VisualizationData
from exceptions.exceptions import LogstringError
from util import convert_to_json, convert_petri_net_to_image
from im_context import IMContext


ALGORITHM_PARAM = "algorithm"
THRESHOLD_PARAM = "threshold"

    
def main(log: Union[EventLog, DataFrame], request_args: Dict,  algorithm_type="im_standard") -> str:
    """ This is the main method  of the backend that handles how the algorithm is run. It uses 
        a context class for implementing the "Strategy" pattern. This is to ensure exchangability 

    Args:
        log (EventLog): event log the IM algorithm should be applied on 
        request_args : data structure storing the request arguments 

    Returns:
        str: _description_
    """
    try:
        if ALGORITHM_PARAM in request_args:
            algorithm_type = request_args[ALGORITHM_PARAM]
        parameters = {}
        logging.debug(log)
        im_context = IMContext()
        if algorithm_type == "im_standard":
            logging.info("using the  inductive miner standard (IM) algorithm")
            im_context.set_algorithm(algorithm_variant=Variants.IMcustom)   
        elif algorithm_type == "im_infrequent":
            threshold = float(request_args[THRESHOLD_PARAM])
            logging.info("using the inductive miner infrequent (IMf) algorithm, with threshold: " + str(threshold))
            parameters[IMFParameters.NOISE_THRESHOLD] = threshold
            im_context.set_algorithm(algorithm_variant=Variants.IMf_custom)
        else:
            logging.info("using the standard inductive miner algorithm, as the algorithm_type parameter value could not be matched with another algorithm")
            im_context.set_algorithm(algorithm_variant=Variants.IMcustom)
        tree, tree_nodes_ls = im_context.execute_algo(log, parameters=parameters)
        net, im, fm = convert_to_petri_net(tree)
        petri_net_image = convert_data_to_base64(convert_petri_net_to_image(net, im, fm, format="svg"))
        visualization_data = VisualizationData(tree_nodes_ls=tree_nodes_ls, algorithm_type=algorithm_type, 
                                            petri_net_image=petri_net_image)
        
        return_json = convert_to_json(visualization_data)
        return return_json
    except KeyError as e:
        e.code = 400
        raise e
    except Exception as e:
        raise e


if __name__ == "__main__":
    logstr = "<a,b,c,e,f>10;<a,d,b,c,d,e,f>10;<a,d,c,e,c,e,f>10;<a,d,e,c,d,e,f>10;<a,d,c,d,e,f>10"
    request_args = {"algorithm": "im_standard"}
    log = string_to_log(logstr)
    ret_val = main(log, request_args=request_args)
    print(ret_val)
    
    # res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext":"lalala"})
    # if res.ok:
    #     print(res.json())