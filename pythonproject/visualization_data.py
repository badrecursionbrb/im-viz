from typing import Dict


class VisualizationDataObject():
    
    def __init__(self, step: int, dfg, pt_node_str_json: str, label: str, case_type: str, 
                dfg_groups: Dict, cur_log: str) -> None:
        """

        Args:
            step (int): the current step number
            dfg (_type_): the current dfg at the current step
            pt_node_str_json (str): the process tree of at the current step
            label (str): the actual label of the node i.e. the type of cut, or the base
                        case activity label e.g. "a", "b" or "z"
            case_type (str): describes what case is used so either a base case, fall through or a cut
            dfg_groups (Dict): dict object that specifies what nodes belong to which group 
            cur_log (str): the event log at the current step 
        """        
        self.step = step
        self.dfg = dfg
        self.dfg_groups_inverted = {}
        for group_key, group_list in dfg_groups.items():
            for activity in group_list:
                self.dfg_groups_inverted[activity] = group_key
        
        self.label = label
        self.case_type = case_type
        self.pt_str = pt_node_str_json
        self.cur_log = cur_log
        # print("label: {} pt: {}".format(self.label, self.pt_str))


class VisualizationData():
    
    def __init__(self, tree_nodes_ls, algorithm_type, petri_net_image) -> None:
        """ Initializes the wrapper VisualizationData object 

        Args:
            tree (_type_): _description_
            algorithm_type (_type_): _description_
            petri_net_image (_type_): _description_
        """
        self.step_counter = 0
        self.traverse_ls = []
        self.algorithm_type = algorithm_type
        self.petri_net_image = petri_net_image
        for pt_node in tree_nodes_ls:
            self.traverse_ls.append([self.step_counter, VisualizationDataObject(step=pt_node.node_id, dfg=pt_node.dfg, 
                                    pt_node_str_json= pt_node.pt_str_json, label=pt_node.value, case_type=pt_node.case_type,
                                    dfg_groups=pt_node.dfg_groups, cur_log=pt_node.log)])
            self.step_counter += 1
        # print("traverse_ls is: {}".format(self.traverse_ls))
        



