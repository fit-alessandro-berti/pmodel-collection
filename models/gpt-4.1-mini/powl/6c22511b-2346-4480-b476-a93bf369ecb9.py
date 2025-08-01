# Generated from: 6c22511b-2346-4480-b476-a93bf369ecb9.json
# Description: This process outlines the establishment of a vertical farming system in an urban environment, integrating sustainable agriculture with smart technology. It involves site evaluation, modular farm design, installation of hydroponic or aeroponic systems, climate control setup, integration of IoT sensors for real-time monitoring, nutrient solution management, lighting calibration, crop selection optimized for vertical growth, staff training on system maintenance, pest control through biological agents, continuous data analysis for yield optimization, and establishing distribution channels for urban markets. The process emphasizes resource efficiency, minimal environmental impact, and scalability to adapt to various building types and urban constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
System_Install = Transition(label='System Install')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Deploy = Transition(label='Sensor Deploy')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Tune = Transition(label='Lighting Tune')
Crop_Select = Transition(label='Crop Select')
Staff_Train = Transition(label='Staff Train')
Pest_Control = Transition(label='Pest Control')
Data_Monitor = Transition(label='Data Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Supply_Chain = Transition(label='Supply Chain')
Waste_Manage = Transition(label='Waste Manage')
Compliance_Check = Transition(label='Compliance Check')

# Create partial order with dependencies reflecting process flow
root = StrictPartialOrder(nodes=[
    Site_Survey, Design_Layout, System_Install, Climate_Setup, Sensor_Deploy,
    Nutrient_Mix, Lighting_Tune, Crop_Select, Staff_Train, Pest_Control,
    Data_Monitor, Yield_Analyze, Supply_Chain, Waste_Manage, Compliance_Check
])

order = root.order
# Site survey first
order.add_edge(Site_Survey, Design_Layout)

# After Design Layout, System Install happens
order.add_edge(Design_Layout, System_Install)

# System Install leads to parallel activities: Climate Setup, Sensor Deploy, Nutrient Mix, Lighting Tune
order.add_edge(System_Install, Climate_Setup)
order.add_edge(System_Install, Sensor_Deploy)
order.add_edge(System_Install, Nutrient_Mix)
order.add_edge(System_Install, Lighting_Tune)

# Crop Select depends on Design Layout (choice of crops made after design)
order.add_edge(Design_Layout, Crop_Select)

# Staff Train depends on system and setup: after Climate Setup and Sensor Deploy and Crop Select
order.add_edge(Climate_Setup, Staff_Train)
order.add_edge(Sensor_Deploy, Staff_Train)
order.add_edge(Crop_Select, Staff_Train)

# Pest Control can be in parallel with Staff Train and depends on Crop Select
order.add_edge(Crop_Select, Pest_Control)

# After Staff Train and Pest Control, Data Monitor starts
order.add_edge(Staff_Train, Data_Monitor)
order.add_edge(Pest_Control, Data_Monitor)

# Yield Analyze depends on Data Monitor
order.add_edge(Data_Monitor, Yield_Analyze)

# Supply Chain depends on Yield Analyze (distribution after yield analysis)
order.add_edge(Yield_Analyze, Supply_Chain)

# Waste Manage runs in parallel but after Crop Select (resource efficiency)
order.add_edge(Crop_Select, Waste_Manage)

# Compliance Check final step depends on Supply Chain and Waste Manage
order.add_edge(Supply_Chain, Compliance_Check)
order.add_edge(Waste_Manage, Compliance_Check)