# Generated from: 175cacaa-1d8a-4b0a-aa71-94e96309fc0d.json
# Description: This process details the establishment of a vertical farming operation within an urban environment, combining advanced hydroponics and IoT-driven monitoring systems. It involves site acquisition, environmental assessment, modular farm design, automated nutrient delivery setup, climate control calibration, crop scheduling, continuous data analysis, pest management integration, and sustainable waste recycling, aiming to optimize food production in limited spaces while minimizing environmental impact and maximizing yield through innovative technology and strategic urban planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Design_Layout = Transition(label='Design Layout')
Module_Assembly = Transition(label='Module Assembly')
Sensor_Install = Transition(label='Sensor Install')
Water_Setup = Transition(label='Water Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Config = Transition(label='Climate Config')
Crop_Planting = Transition(label='Crop Planting')
Data_Sync = Transition(label='Data Sync')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Prep = Transition(label='Harvest Prep')
Waste_Sorting = Transition(label='Waste Sorting')
Yield_Analysis = Transition(label='Yield Analysis')
Market_Sync = Transition(label='Market Sync')

# Create partial order with dependencies
# Following a logical ordering from description:

# Site Survey --> Permit Filing --> Design Layout
# Design Layout -> Module Assembly
# Module Assembly enables Sensor Install, Water Setup, Nutrient Mix (concurrent)
# Then Climate Config
# Crop Planting after Climate Config
# After Crop Planting, Data Sync, Pest Control, Growth Monitor run concurrently as continuous monitoring
# Growth Monitor leads to Harvest Prep
# Harvest Prep --> Waste Sorting and Yield Analysis (concurrent)
# Yield Analysis --> Market Sync

root = StrictPartialOrder(
    nodes=[
        Site_Survey, Permit_Filing, Design_Layout,
        Module_Assembly, Sensor_Install, Water_Setup, Nutrient_Mix,
        Climate_Config, Crop_Planting,
        Data_Sync, Pest_Control, Growth_Monitor,
        Harvest_Prep, Waste_Sorting, Yield_Analysis, Market_Sync
    ]
)

order = root.order
order.add_edge(Site_Survey, Permit_Filing)
order.add_edge(Permit_Filing, Design_Layout)
order.add_edge(Design_Layout, Module_Assembly)
order.add_edge(Module_Assembly, Sensor_Install)
order.add_edge(Module_Assembly, Water_Setup)
order.add_edge(Module_Assembly, Nutrient_Mix)

order.add_edge(Sensor_Install, Climate_Config)
order.add_edge(Water_Setup, Climate_Config)
order.add_edge(Nutrient_Mix, Climate_Config)

order.add_edge(Climate_Config, Crop_Planting)

order.add_edge(Crop_Planting, Data_Sync)
order.add_edge(Crop_Planting, Pest_Control)
order.add_edge(Crop_Planting, Growth_Monitor)

order.add_edge(Growth_Monitor, Harvest_Prep)

order.add_edge(Harvest_Prep, Waste_Sorting)
order.add_edge(Harvest_Prep, Yield_Analysis)

order.add_edge(Yield_Analysis, Market_Sync)