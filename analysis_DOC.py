from gboml import *
import json
import matplotlib.pyplot as plt
import numpy as np
import gboml.compiler.classes as gcc
import argparse
import os

if not os.path.exists("images_DOC"):
        os.makedirs("images_DOC")



parser = argparse.ArgumentParser()

parser.add_argument('-sc', '--scenario', help='Scenario', 
                        type=str, default="reference", choices=['reference','optimistic','conservative', 'comparison'])


args = parser.parse_args()
scenario = args.scenario

if scenario == "comparison":

    years = 5
    class MakeMeReadable:
        def __init__(self, d):
            self.d = d
    
        def __dir__(self):
            return self.d.keys()
    
        def __getattr__(self, v):
            try:
                out = self.d[v]
                if isinstance(out, dict):
                    return MakeMeReadable(out)
                return out
            except:
                return getattr(self.d, v)
        
        def __str__(self):
            return str(self.d)
    
        def __repr__(self):
            return repr(self.d)


    filename = "results_DOC/reference.json"
    dico = {}
    with open(filename, "r") as fp:
        dico = json.load(fp)
    
    d = MakeMeReadable(dico)

    filename = "results_DOC/optimistic.json"
    dico = {}
    with open(filename, "r") as fp:
        dico = json.load(fp)
    
    e = MakeMeReadable(dico)

    filename = "results_DOC/conservative.json"
    dico = {}
    with open(filename, "r") as fp:
        dico = json.load(fp)
    
    f = MakeMeReadable(dico)

    wind1 = (np.sum([e.solution.elements.WIND_PLANTS.objectives.unnamed[0], e.solution.elements.WIND_PLANTS.objectives.unnamed[1]]))/(10*years)
    hydrogen1 = (e.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0] + e.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[1] + e.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0] + e.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[1])/(10*years)
    battery1 = ( np.sum([e.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],e.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]))/(10*years)
    solar1 = (e.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0] + e.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[1])/(10*years)
    methanation1 = (e.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[0] + e.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[1] + e.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[0] + e.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[1] + e.solution.elements.METHANATION_PLANTS.objectives.unnamed[0] + e.solution.elements.METHANATION_PLANTS.objectives.unnamed[1] + e.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[0] + e.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[1] + e.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[0] + e.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[1] + e.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[0] + e.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[1])/(10*years)
    CO21 = (e.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[0] + e.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[1] + e.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[0] + e.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[1]  )/(10*years)
    Others1 = (e.solution.elements.HVDC.objectives.unnamed[0] + e.solution.elements.HVDC.objectives.unnamed[1]  + e.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0] + e.solution.elements.DESALINATION_PLANTS.objectives.unnamed[1] + e.solution.elements.WATER_STORAGE.objectives.unnamed[0] + e.solution.elements.WATER_STORAGE.objectives.unnamed[1])/(10*years)

    wind2 = (np.sum([d.solution.elements.WIND_PLANTS.objectives.unnamed[0], d.solution.elements.WIND_PLANTS.objectives.unnamed[1]]))/(10*years)
    hydrogen2 = (d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0] + d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[1] + d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0] + d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[1])/(10*years)
    battery2 = ( np.sum([d.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],d.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]))/(10*years)
    solar2 = (d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0] + d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[1])/(10*years)
    methanation2 = (d.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[0] + d.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[1] + d.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[0] + d.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[1] + d.solution.elements.METHANATION_PLANTS.objectives.unnamed[0] + d.solution.elements.METHANATION_PLANTS.objectives.unnamed[1] + d.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[0] + d.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[1] + d.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[0] + d.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[1] + d.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[0] + d.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[1])/(10*years)
    CO22 = (d.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[0] + d.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[1] + d.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[0] + d.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[1]  )/(10*years)
    Others2 = (d.solution.elements.HVDC.objectives.unnamed[0] + d.solution.elements.HVDC.objectives.unnamed[1]  + d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0] + d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[1] + d.solution.elements.WATER_STORAGE.objectives.unnamed[0] + d.solution.elements.WATER_STORAGE.objectives.unnamed[1])/(10*years)

    wind3 = (np.sum([f.solution.elements.WIND_PLANTS.objectives.unnamed[0], f.solution.elements.WIND_PLANTS.objectives.unnamed[1]]))/(10*years)
    hydrogen3 = (f.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0] + f.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[1] + f.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0] + f.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[1])/(10*years)
    battery3 = ( np.sum([f.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],f.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]))/(10*years)
    solar3 = (f.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0] + f.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[1])/(10*years)
    methanation3 = (f.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[0] + f.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[1] + f.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[0] + f.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[1] + f.solution.elements.METHANATION_PLANTS.objectives.unnamed[0] + f.solution.elements.METHANATION_PLANTS.objectives.unnamed[1] + f.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[0] + f.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[1] + f.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[0] + f.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[1] + f.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[0] + f.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[1])/(10*years)
    CO23 = (f.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[0] + f.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[1] + f.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[0] + f.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[1]  )/(10*years)
    Others3 = (f.solution.elements.HVDC.objectives.unnamed[0] + f.solution.elements.HVDC.objectives.unnamed[1]  + f.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0] + f.solution.elements.DESALINATION_PLANTS.objectives.unnamed[1] + f.solution.elements.WATER_STORAGE.objectives.unnamed[0] + f.solution.elements.WATER_STORAGE.objectives.unnamed[1])/(10*years)

    colors = ['#BFC9CA', '#D35400', '#F5B041', '#F4D03F', '#ABEBC6', '#5DADE2', '#2ECC71']
    categories = ['Conservative', 'Reference', 'Optimistic']
    cost_types = ['Others', 'Methanation', 'Battery', 'Solar PV', 'Wind', 'Hydrogen', 'CO2']
    values = np.array([[Others3, Others2, Others1 ],
                    [methanation3, methanation2, methanation1],
                        [battery3, battery2, battery1],
                    [solar3, solar2, solar1],
                    [wind3, wind2, wind1],
                    [hydrogen3, hydrogen2, hydrogen1],
                    [CO23, CO22, CO21],])


    fig, ax = plt.subplots()
    bottoms = np.zeros(len(categories))
    for i, cost_type in enumerate(cost_types):
        bars = ax.barh(categories, values[i], left=bottoms, label=cost_type, color=colors[i])
        bottoms += values[i]

    last_bottoms = bottoms
    for j, bar in enumerate(bars):
        value = last_bottoms[j]
        ax.text(bar.get_x() + bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, str(round(value, 1)), ha='left',
                va='center')


    ax.legend(loc='upper right', bbox_to_anchor=(1.4, 1))
    ax.set_xlim(right=max(bottoms) * 1.2)  
    plt.savefig('images_DOC/all_cost_comparison', dpi=150, bbox_inches='tight')
    plt.show()

else:
    years = 5

    class MakeMeReadable:
        def __init__(self, d):
            self.d = d
    
        def __dir__(self):
            return self.d.keys()
    
        def __getattr__(self, v):
            try:
                out = self.d[v]
                if isinstance(out, dict):
                    return MakeMeReadable(out)
                return out
            except:
                return getattr(self.d, v)
        
        def __str__(self):
            return str(self.d)
    
        def __repr__(self):
            return repr(self.d)


    filename = "results_DOC/" + str(scenario) +".json"
    dico = {}
    with open(filename, "r") as fp:
        dico = json.load(fp)
    
    d = MakeMeReadable(dico)

    x = ['Battery Storage', 'Wind Turbines', 'HVDC', 'Hydrogen storage', 'Electrolysis', 'Methanation', 'Direct Ocean Capture', 'Solar PV', 'Methane Liquefaction', 'Liquefied Methane Regasification', 'Liquefied Methane Storage', 'Water Desalination', 'Liquefied Methane Carriers', 'Pipeline']
    y = np.array([np.sum([d.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],d.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]), np.sum([d.solution.elements.WIND_PLANTS.objectives.unnamed[0], d.solution.elements.WIND_PLANTS.objectives.unnamed[1]]), d.solution.elements.HVDC.objectives.unnamed[0], d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0], d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0], d.solution.elements.METHANATION_PLANTS.objectives.unnamed[0], np.sum([d.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[0], d.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[1]]), d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0], d.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[0], d.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[0], np.add(d.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[0],d.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[0]), np.sum([d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0],d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0]]), d.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[0],np.sum([d.solution.elements.PIPELINE.objectives.named.pipe_cost_fix, d.solution.elements.PIPELINE.objectives.named.pipe_cost_var])  ])/(10*years)

    sorted_indices = np.argsort(y)
    sorted_x = [x[i] for i in sorted_indices]
    sorted_y = y[sorted_indices]
    sorted_y_rounded = np.round(sorted_y, 1)

    colors = ['#F9E79F', '#F9E79F', '#F9E79F', '#ADE2F0', '#ADE2F0', '#D68B11', '#ABE78C', '#F9E79F', '#D68B11', '#D68B11', '#D68B11', '#588AD3', '#D68B11', '#ABE78C']

    plt.figure(figsize=(10,7))
    bars = plt.barh(sorted_x, sorted_y_rounded.flatten(), height=0.6, color=[colors[i] for i in sorted_indices])
    plt.xlabel('€/MWh')
    plt.title(f'Synthetic Methane Cost Breakdown (€/MWh) - Total Cost: {np.sum(d.solution.objective/(10*years)):.1f} €/MWh')

    for i, bar in enumerate(bars):
        plt.text(bar.get_width(), i, str(bar.get_width()))
        
    plt.savefig('images_DOC/cost_breakdown_' + str(scenario) + '.png', dpi=150, bbox_inches='tight')


    wind2 = (np.sum([d.solution.elements.WIND_PLANTS.objectives.unnamed[0], d.solution.elements.WIND_PLANTS.objectives.unnamed[1]]))/(10*years)
    hydrogen2 = (d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0] + d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[1] + d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0] + d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[1])/(10*years)
    battery2 = ( np.sum([d.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],d.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]))/(10*years)
    solar2 = (d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0] + d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[1])/(10*years)
    methanation2 = (d.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[0] + d.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[1] + d.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[0] + d.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[1] + d.solution.elements.METHANATION_PLANTS.objectives.unnamed[0] + d.solution.elements.METHANATION_PLANTS.objectives.unnamed[1] + d.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[0] + d.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[1] + d.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[0] + d.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[1] + d.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[0] + d.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[1])/(10*years)
    CO22 = (d.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[0] + d.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.objectives.unnamed[1] + d.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[0] + d.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[1] + d.solution.elements.PIPELINE.objectives.named.pipe_cost_fix + d.solution.elements.PIPELINE.objectives.named.pipe_cost_var )/(10*years)
    Others2 = (d.solution.elements.HVDC.objectives.unnamed[0] + d.solution.elements.HVDC.objectives.unnamed[1]  + d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0] + d.solution.elements.WATER_STORAGE.objectives.unnamed[0])/(10*years)

    filename = "data/DAC_remote_hub.json"
    dico = {}
    with open(filename, "r") as fp:
        dico = json.load(fp)
    
    e = MakeMeReadable(dico)


    wind1 = (np.sum([e.solution.elements.WIND_PLANTS.objectives.unnamed[0], e.solution.elements.WIND_PLANTS.objectives.unnamed[1]]))/(10*years)
    hydrogen1 = (e.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0] + e.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[1] + e.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0] + e.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[1])/(10*years)
    battery1 = ( np.sum([e.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],e.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]))/(10*years)
    solar1 = (e.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0] + e.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[1])/(10*years)
    methanation1 = (e.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[0] + e.solution.elements.METHANE_LIQUEFACTION_PLANTS.objectives.unnamed[1] + e.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[0] + e.solution.elements.LIQUEFIED_METHANE_REGASIFICATION.objectives.unnamed[1] + e.solution.elements.METHANATION_PLANTS.objectives.unnamed[0] + e.solution.elements.METHANATION_PLANTS.objectives.unnamed[1] + e.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[0] + e.solution.elements.LIQUEFIED_METHANE_CARRIERS.objectives.unnamed[1] + e.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[0] + e.solution.elements.LIQUEFIED_METHANE_STORAGE_DESTINATION.objectives.unnamed[1] + e.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[0] + e.solution.elements.LIQUEFIED_METHANE_STORAGE_HUB.objectives.unnamed[1])/(10*years)
    CO21 = (e.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[0] + e.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[1] + e.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[0] + e.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[1]  )/(10*years)
    Others1 = (e.solution.elements.HVDC.objectives.unnamed[0] + e.solution.elements.HVDC.objectives.unnamed[1]  + e.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0] + e.solution.elements.DESALINATION_PLANTS.objectives.unnamed[1] + e.solution.elements.WATER_STORAGE.objectives.unnamed[0] + e.solution.elements.WATER_STORAGE.objectives.unnamed[1])/(10*years)


    colors = ['#BFC9CA', '#D35400', '#F5B041', '#F4D03F', '#ABEBC6', '#5DADE2', '#2ECC71']
    categories = ['DOC remote hub', 'DAC remote hub']
    cost_types = ['Others', 'Methanation', 'Battery', 'Solar PV', 'Wind', 'Hydrogen', 'CO2']
    values = np.array([[Others2, Others1 ],
                    [methanation2, methanation1],
                        [battery2, battery1],
                    [solar2, solar1],
                    [wind2, wind1],
                    [hydrogen2, hydrogen1],
                    [CO22, CO21],])

    fig, ax = plt.subplots()

    bottoms = np.zeros(len(categories))
    for i, cost_type in enumerate(cost_types):
        bars = ax.barh(categories, values[i], left=bottoms, label=cost_type, color=colors[i])
        bottoms += values[i]


    last_bottoms = bottoms
    for j, bar in enumerate(bars):
        value = last_bottoms[j]
        ax.text(bar.get_x() + bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, str(round(value, 1)), ha='left',
                va='center')

    ax.legend(loc='upper right', bbox_to_anchor=(1.4, 1))
    ax.set_xlim(right=max(bottoms) * 1.2) 
    plt.savefig('images_DOC/cost_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()

    categories = ['DAC remote hub', 'DOC remote hub']
    values1 = [e.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values[0], d.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values[0]] #PV
    values2 = [e.solution.elements.WIND_PLANTS.variables.capacity.values[0], d.solution.elements.WIND_PLANTS.variables.capacity.values[0]] #wind
    values3 = [e.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values[0], d.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values[0]] #batteries
    bar_width = 0.25

    x = np.arange(len(categories))
    plt.bar(x - bar_width, values2, width=bar_width, label='Wind Turbines [GW]', color='#ABEBC6')
    plt.bar(x , values1, width=bar_width, label='PV Panels [GW]', color='#F4D03F')
    plt.bar(x + bar_width, values3, width=bar_width, label='Batteries [GWh]', color='#F5B041')
    plt.ylim(0, max(max(values1), max(values2), max(values3)) + 2)

    plt.tick_params(axis='x', length=0)
    plt.tick_params(axis='y', length=5, width=1, direction='inout')
    plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)
    plt.xticks(x, categories)
    plt.savefig('images_DOC/capacity_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()
