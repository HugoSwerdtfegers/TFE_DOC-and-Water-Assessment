from gboml import *
import json
import matplotlib.pyplot as plt
import numpy as np
import gboml.compiler.classes as gcc
import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument('-sc', '--scenario', help='Scenario', 
                        type=str, default="reference", choices=['reference','improve_desal','summer_demand', 'variable_desal', 'all_change', 'no_water_demand'])

args = parser.parse_args()
scenario = args.scenario


years = 5
gboml_model = GbomlGraph(8760*years)
nodes, edges, global_params = gboml_model.import_all_nodes_and_edges("water_demand.gboml")


if scenario == "reference":
    activate_basic_demand = 1
    activate_summer_demand = 0
    conversion_factor_electricity = 0.004
    minimum_level = 1.0
elif scenario == "improve_desal":
    activate_basic_demand = 1
    activate_summer_demand = 0
    conversion_factor_electricity = 0.002
    minimum_level = 1.0
elif scenario == "summer_demand":
    activate_basic_demand = 0
    activate_summer_demand = 1
    conversion_factor_electricity = 0.004
    minimum_level = 1.0
elif scenario == "variable_desal":
    activate_basic_demand = 1
    activate_summer_demand = 0
    conversion_factor_electricity = 0.004
    minimum_level = 0.7
elif scenario == "all_change":
    activate_basic_demand = 0
    activate_summer_demand = 1
    conversion_factor_electricity = 0.002
    minimum_level = 0.7
elif scenario == "no_water_demand":
    activate_basic_demand = 0
    activate_summer_demand = 0
    conversion_factor_electricity = 0.004
    minimum_level = 1.0
else:
    print("Choose an appropriate scenario")



global_params = list(filter(lambda x: x.name != "activate_basic_demand", global_params))
global_params.append(gcc.Parameter("activate_basic_demand", 
                            gcc.Expression("literal", activate_basic_demand)))    
    
global_params = list(filter(lambda x: x.name != "activate_summer_demand", global_params))
global_params.append(gcc.Parameter("activate_summer_demand", 
                            gcc.Expression("literal", activate_summer_demand)))    
    
global_params = list(filter(lambda x: x.name != "conversion_factor_electricity", global_params))
global_params.append(gcc.Parameter("conversion_factor_electricity", 
                            gcc.Expression("literal", conversion_factor_electricity)))    
    
global_params = list(filter(lambda x: x.name != "minimum_level", global_params))
global_params.append(gcc.Parameter("minimum_level", 
                            gcc.Expression("literal", minimum_level)))    
    
 
    




gboml_model.add_nodes_in_model(*nodes)
gboml_model.add_hyperedges_in_model(*edges)
gboml_model.add_global_parameters(global_params)
gboml_model.build_model()
solution = gboml_model.solve_gurobi()
print("Solved")


if not os.path.exists("results_water_demand"):
        os.makedirs("results_water_demand")


solution, objective, status, solver_info, constraints_information, variables_information = solution
dico = gboml_model.turn_solution_to_dictionary(solver_info, status, solution, objective, constraints_information, variables_information)

with open("results_water_demand/"+ str(scenario) + ".json", "w") as json_file:
    json_obj = json.dumps(dico)
    json_file.write(json_obj)

print("Json done")