#!/bin/bash
pip install -r requirements.txt
for scenario in reference improve_desal summer_demand variable_desal all_change; do
    echo "Simulation launch for $scenario scenario"    
    python3 main_water_demand.py --scenario $scenario
    echo ""
done