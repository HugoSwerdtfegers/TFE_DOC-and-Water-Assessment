from gboml import *
import json
import matplotlib.pyplot as plt
import numpy as np
import gboml.compiler.classes as gcc
import argparse
import os


if not os.path.exists("images_water_demand"):
        os.makedirs("images_water_demand")


parser = argparse.ArgumentParser()

parser.add_argument('-sc', '--scenario', help='Scenario', 
                        type=str, default="reference", choices=['reference','improve_desal','summer_demand', 'variable_desal', 'all_change'])

args = parser.parse_args()
scenario = args.scenario
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


filename = "results_water_demand/" + str(scenario) + ".json"
dico = {}
with open(filename, "r") as fp:
    dico = json.load(fp)
   
d = MakeMeReadable(dico)


x = ['[GWh] Batteries', '[GW] Solar PV', '[GW] Wind turbines', '[TWh] Hydrogen', '[GW_el] Electrolysis', '[GW_th] Methanation', '[Mt/y] DOC', '[kt/h] Desalination', '[kt/h] Water Storage ' ]
y = np.array([d.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values, d.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values, d.solution.elements.WIND_PLANTS.variables.capacity.values,np.divide(d.solution.elements.HYDROGEN_STORAGE.variables.capacity_stock.values,1/0.04), d.solution.elements.ELECTROLYSIS_PLANTS.variables.capacity.values , np.divide(d.solution.elements.METHANATION_PLANTS.variables.capacity.values, 1/16), np.divide(d.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.variables.capacity.values, 1/8.76), d.solution.elements.DESALINATION_PLANTS.variables.capacity.values, d.solution.elements.WATER_STORAGE.variables.capacity_flow.values])
y_rounded = np.round(y, 2)

plt.figure(figsize=(10,7))
bars = plt.barh(x,y_rounded.flatten(), height=0.6)
plt.xlim(0, 6)
plt.title('Capacities of storage technologies')

for i, bar in enumerate(bars):
    plt.text(bar.get_width(), i, str(bar.get_width()))



p = d.solution.elements.DESALINATION_PLANTS.variables.water.values
q = d.model.hyperedges.COASTAL_WATER_BALANCE.parameters.w_demand
storage = d.solution.elements.WATER_STORAGE.variables.water_out.values
m = d.solution.elements.METHANATION_PLANTS.variables.water.values
q_e = np.tile(q, 5)
a = np.zeros(len(p))

i=0
while i < len(p):
    a[i] = 1 - ((p[i] + storage[i] + m[i] - q_e[i])/(p[i] + storage[i] + m[i]))
    i = i +1


plt.figure(figsize=(14, 6))
plt.plot(a[:800])
plt.xlabel('Hours')

plt.fill_between(range(800), a[:800], color='dodgerblue', alpha=0.5, label='Water Demand')
plt.fill_between(range(800), a[:800], max(a[:800]), color='white', alpha=0.5, label='Methane Production')
plt.legend()
plt.savefig('images_water_demand/water_uti.pdf', dpi=150)

elec_sto = d.solution.elements.WATER_STORAGE.variables.electricity.values
elec_desal = (d.solution.elements.DESALINATION_PLANTS.variables.electricity.values)
elec_TOT = (d.solution.elements.HVDC.variables.electricity_out.values)
b = np.zeros(len(elec_sto))

i=0
while i < len(elec_sto):
    b[i] = (elec_sto[i] + elec_desal[i]*a[i])/(elec_TOT[i])
    i = i +1


plt.figure(figsize=(14, 6))
plt.plot(b[:800], color ='orange')
plt.xlabel('Hours')

plt.fill_between(range(800), b[:800], color='orange', alpha=0.2, label='Water Demand')
plt.fill_between(range(800), b[:800], max(b[:800]), color='white', alpha=0.5, label='Methane Production')

plt.legend()
plt.savefig('images_water_demand/elec_uti.pdf', dpi=150)

filename = "data/no_water_demand.json"
dico = {}
with open(filename, "r") as fp:
    dico = json.load(fp)
   
e = MakeMeReadable(dico)

x = ['[GWh] Batteries', '[GW] Solar PV', '[GW] Wind turbines', '[TWh] Hydrogen', '[GW_el] Electrolysis', '[GW_th] Methanation', '[Mt/y] DOC', '[kt/h] Desalination', '[kt/h] Water Storage ' ]
y = np.array([d.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values, d.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values, d.solution.elements.WIND_PLANTS.variables.capacity.values,np.divide(d.solution.elements.HYDROGEN_STORAGE.variables.capacity_stock.values,1/0.04), d.solution.elements.ELECTROLYSIS_PLANTS.variables.capacity.values , np.divide(d.solution.elements.METHANATION_PLANTS.variables.capacity.values, 1/16), np.divide(d.solution.elements.DIRECT_OCEAN_CAPTURE_PLANTS.variables.capacity.values, 1/8.76), d.solution.elements.DESALINATION_PLANTS.variables.capacity.values, d.solution.elements.WATER_STORAGE.variables.capacity_flow.values])
y_rounded = np.round(y, 2)

plt.figure(figsize=(10,7))
bars = plt.barh(x,y_rounded.flatten(), height=0.6)
plt.xlim(0, 6)
plt.title('Capacities of storage technologies SANS DEMANDE')

for i, bar in enumerate(bars):
    plt.text(bar.get_width(), i, str(bar.get_width()))


cout_desal_t = (d.solution.elements.DESALINATION_PLANTS.variables.water.values)*a*0.000315
cout_desal_capa = d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0]*((d.solution.elements.DESALINATION_PLANTS.variables.capacity.values[0]- 0.17)/d.solution.elements.DESALINATION_PLANTS.variables.capacity.values[0])

cout_sto_capa = d.solution.elements.WATER_STORAGE.objectives.unnamed[0]*((d.solution.elements.WATER_STORAGE.variables.capacity_flow.values[0]- 0.32)/d.solution.elements.WATER_STORAGE.variables.capacity_flow.values[0])

cout_PV_capa = d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0]*((d.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values[0] - 3.82)/d.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values[0])
#vom PV = 0

cout_wind_capa = d.solution.elements.WIND_PLANTS.objectives.unnamed[0]*((d.solution.elements.WIND_PLANTS.variables.capacity.values[0] - 3.57)/d.solution.elements.WIND_PLANTS.variables.capacity.values[0])
cout_wind_t = (d.solution.elements.WIND_PLANTS.variables.electricity.values)*b*0.00135
cout_bat_capa = d.solution.elements.BATTERY_STORAGE.objectives.unnamed[0]*((d.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values[0] - 3.87)/d.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values[0])
cout_bat_t = (d.solution.elements.BATTERY_STORAGE.variables.electricity_stored.values)*b*0.0018

cout_eau = (cout_desal_capa + sum(cout_desal_t) + cout_sto_capa + cout_PV_capa + cout_wind_capa + sum(cout_wind_t) + sum(cout_bat_t) + cout_bat_capa)/(10000*365*5)
print("Cost (€/t)")
print(cout_eau*1e6) #M€/t


categories = ['Desalination plant', 'Storage Unit', 'Elec Production Increase', 'Battery Increase']
valeurs = [(cout_desal_capa + sum(cout_desal_t))*1e6/(10000*365*5), cout_sto_capa*1e6/(10000*365*5), (cout_PV_capa + cout_wind_capa + sum(cout_wind_t))*1e6/(10000*365*5), (sum(cout_bat_t) + cout_bat_capa)*1e6/(10000*365*5)]


couleurs = ['lightskyblue', 'yellowgreen', 'lightcoral', 'gold']
fig, ax = plt.subplots(figsize=(10, 2))

plt.barh('Total Cost', sum(valeurs), color='gray')

left_position = 0
for i in range(len(categories)):
    bar = ax.barh('Total Cost', valeurs[i], left=left_position, color=couleurs[i], label=categories[i])
    value = round(valeurs[i], 2)  
    ax.text(left_position + valeurs[i]/2, 0, f'{value} €', ha='center', va='center', color='BLACK')
    left_position += valeurs[i]
    

ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1), ncol=len(categories)+1)
plt.savefig('images_water_demand/' + str(scenario) + '.pdf', dpi=150, bbox_inches='tight')
