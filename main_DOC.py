from gboml import *
import json
import matplotlib.pyplot as plt
import numpy as np
import gboml.compiler.classes as gcc
import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument('-sc', '--scenario', help='Scenario', 
                        type=str, default="reference", choices=['reference','optimistic','conservative', 'variable_DOC'])

args = parser.parse_args()
scenario = args.scenario


if scenario == "optimistic":
    facteur = 0.8
    conversion_factor_electricity = 0.663
    years = 5
    minimum_level = 1.0
elif scenario == "reference":
    facteur = 1
    conversion_factor_electricity = 0.953
    years = 5
    minimum_level = 1.0
elif scenario == "conservative":
    facteur = 1.2
    conversion_factor_electricity = 1.528
    years = 5
    minimum_level = 1.0
elif scenario == "variable_DOC":
    facteur = 1
    conversion_factor_electricity = 0.953
    years = 1
    minimum_level = 0.5
else:
    print("Choose an appropriate scenario")



gboml_model = GbomlGraph(8760*years)
nodes, edges, global_params = gboml_model.import_all_nodes_and_edges("DOC.gboml")




global_params = list(filter(lambda x: x.name != "facteur", global_params))
global_params.append(gcc.Parameter("facteur", 
                            gcc.Expression("literal", facteur)))    
    
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


if not os.path.exists("results_DOC"):
        os.makedirs("results_DOC")


solution, objective, status, solver_info, constraints_information, variables_information = solution
dico = gboml_model.turn_solution_to_dictionary(solver_info, status, solution, objective, constraints_information, variables_information)

with open("results_DOC/"+ str(scenario) + ".json", "w") as json_file:
    json_obj = json.dumps(dico)
    json_file.write(json_obj)

print("Json done")