# Generated from: 930a521e-2cc4-48bc-9e0f-7d35e879280f.json
# Description: This process outlines the comprehensive cycle of urban vertical farming where crops are grown in stacked layers within controlled indoor environments. It involves site assessment, modular installation, seed selection, nutrient preparation, climate calibration, automated seeding, growth monitoring, pest control, adaptive lighting, water recycling, data analytics, crop harvesting, quality inspection, packaging automation, and distribution logistics. The process integrates IoT sensors and AI-driven analytics to optimize yield while minimizing resource consumption, addressing urban space constraints and sustainability goals in agriculture. Continuous feedback loops ensure adjustments to environmental factors and operational parameters for maximum productivity and minimal waste.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition(label='Site Assess')
Module_Install = Transition(label='Module Install')
Seed_Select = Transition(label='Seed Select')
Nutrient_Prep = Transition(label='Nutrient Prep')
Climate_Calibrate = Transition(label='Climate Calibrate')
Auto_Seed = Transition(label='Auto Seed')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Light_Adjust = Transition(label='Light Adjust')
Water_Recycle = Transition(label='Water Recycle')
Data_Analyze = Transition(label='Data Analyze')
Crop_Harvest = Transition(label='Crop Harvest')
Quality_Inspect = Transition(label='Quality Inspect')
Package_Auto = Transition(label='Package Auto')
Logistics_Plan = Transition(label='Logistics Plan')

# Define main cycle nodes (after site assessment and module install)
# Representing the continuous feedback loop for growth monitoring and adjustment activities

# Loop body: 
#   B = sequence of adjustment activities and monitoring (Pest_Control, Light_Adjust, Water_Recycle, Data_Analyze)
#   looping on Growth_Monitor (A)

# Adjustment activities partial order (all adjustments concurrent):
adjustments = StrictPartialOrder(nodes=[Pest_Control, Light_Adjust, Water_Recycle, Data_Analyze])

# Loop defined as LOOP(Growth_Monitor, adjustments)
# Meaning: execute Growth Monitor, then either exit or do adjustments and Growth Monitor again, looping
loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, adjustments])

# Setup the initial sequence before loop: Site Assess -> Module Install -> Seed Select -> Nutrient Prep -> Climate Calibrate -> Auto Seed
# After loop: Crop Harvest -> Quality Inspect -> Package Auto -> Logistics Plan

# Build partial order nodes with all activities including the loop
nodes = [
    Site_Assess,
    Module_Install,
    Seed_Select,
    Nutrient_Prep,
    Climate_Calibrate,
    Auto_Seed,
    loop,
    Crop_Harvest,
    Quality_Inspect,
    Package_Auto,
    Logistics_Plan
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for the initial sequence
root.order.add_edge(Site_Assess, Module_Install)
root.order.add_edge(Module_Install, Seed_Select)
root.order.add_edge(Seed_Select, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Climate_Calibrate)
root.order.add_edge(Climate_Calibrate, Auto_Seed)
root.order.add_edge(Auto_Seed, loop)

# After the loop, proceed to harvesting and subsequent steps
root.order.add_edge(loop, Crop_Harvest)
root.order.add_edge(Crop_Harvest, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Package_Auto)
root.order.add_edge(Package_Auto, Logistics_Plan)