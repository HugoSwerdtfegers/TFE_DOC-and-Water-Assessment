# TFE: Optimization of Energy Systems with Carbon Capture and Storage to Reach a Carbon- Free Energy System in Belgium

# Installation
First you need to prepare your python environment with:   

`pip install -r requirements.txt`

In particular, the basic numpy and matplotlibs libraries are used, in addition to GBOML, where the documentation   
and installation can be found here https://gboml.readthedocs.io/en/latest/

# How to run simulation and save results for DOC part

To run the simulation with the desired parameters and save the results:

`python3 main_DOC.py -sc $scenario`

where you choose between 3 scenarios:    
 
`$scenario \in {reference, optimistic, conservative}`   

The default case is the reference scenario

If you have a prepared bash environment, you can run: 

`bash run_all_DOC.sh`   

to start all simulation at once

# How to run analysis and save plots for DOC part

To obtain all graphs related to analyses:

`python3 analysis_DOC.py -sc $scenario`

where you choose between 4 scenarios

`$scenario \in {reference, optimistic, conservative, comparison}`  

The default case is the reference scenario

Comparison scenario will provide the costs of all scenarios on the same graph,    
the 3 scenarios must have been simulated beforehand.

# How to run simulation and save results for water assessment part

To run the simulation with the desired parameters and save the results:

`python3 main_water_demand.py -sc $scenario`

where you choose between 5 scenarios:    
 
`$scenario \in {reference, improve_desal, summer_demand, variable_desal, all_change}`   

The default case is the reference scenario

If you have a prepared bash environment, you can run: 

`bash run_all_water_demand.sh`   

to start all simulation at once

# How to run analysis and save plots for water assessment part

To obtain all graphs related to analyses:

`python3 analysis_water_demand.py -sc $scenario`

where you choose between 5 scenarios:    
 
`$scenario \in {reference, improve_desal, summer_demand, variable_desal, all_change}`   

The default case is the reference scenario
