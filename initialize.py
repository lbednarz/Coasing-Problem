import numpy as np
import sympy 
import dataclasses
import header 

#def initialize(sys: header.SymSystem, initials: np.ndarray, var_list: list, fields: list): 
def initialize(init_args: dict):  # NOTE a dataclass would be much safer here  
    # take numeric list of initial values of each variable in var_list and map them 
    # pull args from dict 
    # sys = init_args["sys"]
    # initials = init_args["initials"]
    # var_list = init_args["var_list"]
    # fields = init_args["fields"] 
    # init_map = dict.fromkeys(var_list)
    # i = 0
    # for var in var_list:
    #     init_map[var] = initials[i]
    #     i = i + 1
    # # sub in conditions from map and return numeric arrays for the system
    # sys_dict = dataclasses.asdict(sys)
    # keys = sys_dict.keys()
    # i = 0
    # for key in keys:
    #     mat: sympy.Matrix = sys_dict[key]
    #     mat_vars = mat.free_symbols
    #     for var in mat_vars:
    #         mat = mat.subs(var, init_map[var])
    #     if i == 0: 
    #         args = [np.array(mat)]
    #     else: 
    #         args.append(np.array(mat))
    #     i = i + 1 
    # sys_out = header.ssSystem(*args)
    # return sys_out

    #take numeric list of initial values of each variable in var_list and map them 
    # pull args from dict 
    sys = init_args["sys"]
    initials = init_args["initials"]
    var_list = init_args["var_list"]
    fields = init_args["fields"] 
    init_map = dict.fromkeys(var_list)
    for i, var in enumerate(var_list):
        init_map[var] = initials[i]
    # sub in conditions from map and return numeric arrays for the system
    sys_dict = dataclasses.asdict(sys)
    keys = sys_dict.keys()
    for i,key in enumerate(keys):
        mat: sympy.Matrix = sys_dict[key]
        mat_vars = mat.free_symbols
        for var in mat_vars:
            mat = mat.subs(var, float(init_map[var]))
        if i == 0: 
            args = [np.array(mat).astype(float)]
        else: 
            args.append(np.array(mat).astype(float))
    sys_out = header.ssSystem(*args)
    return sys_out

    

    