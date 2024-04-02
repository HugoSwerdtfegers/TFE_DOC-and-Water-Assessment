#!/bin/bash
pip install -r requirements.txt
for scenario in reference optimistic conservative; do
    echo "Simulation launch for $scenario scenario"    
    python3 main_DOC.py --scenario $scenario
    echo ""
done