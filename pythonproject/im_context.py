
from typing import Optional, Dict, Any, List

from pm4py.algo.discovery.inductive.algorithm_modified_v2 import Variants, apply
from pm4py.objects.log.obj import Event, Trace, EventLog
from pm4py.objects.process_tree.obj import ProcessTree

class IMContext(object):
    """ The IM_Context class is implementing the context part of the strategy pattern. This pattern has the different miner algorithms as strategies

    Args:
        object (_type_): _description_
    """    
    
    
    def __init__(self) -> None:
        self.algorithm_variant = None
    
    def set_algorithm(self, algorithm_variant: Variants):
        """ Set the algorithm that shall be applied when the execute_algo method is called

        Args:
            algorithm_variant (Variants): the algorithm variant to set 
        """
        self.algorithm_variant = algorithm_variant
    
    def execute_algo(self, log: EventLog, parameters: Optional[Dict[Any, Any]] = None) -> List:
        """ Method to trigger the execution of the inductive miner algorithm

        Args:
            log (EventLog): EventLog the inductive miner is  applied to 

        Returns:
            ProcessTree: object created during application of the im algorithm
        """
        tree, tree_nodes_ls = apply(log, variant=self.algorithm_variant, parameters=parameters)
        return tree, tree_nodes_ls
    
    
















