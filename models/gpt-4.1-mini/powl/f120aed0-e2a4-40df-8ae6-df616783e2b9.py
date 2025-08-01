# Generated from: f120aed0-e2a4-40df-8ae6-df616783e2b9.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming enterprise within a repurposed industrial building. It includes site evaluation, modular rack design, hydroponic system installation, climate control calibration, nutrient solution preparation, crop selection based on market demand, seed germination, continuous monitoring using IoT sensors, pest control with integrated biocontrol agents, automated harvesting, post-harvest quality assessment, packaging for urban consumers, data analytics for yield optimization, community engagement for local sourcing, and finally, distribution logistics tailored to minimize carbon footprint in densely populated areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Rack_Design = Transition(label='Rack Design')
System_Setup = Transition(label='System Setup')
Climate_Calibrate = Transition(label='Climate Calibrate')
Nutrient_Prep = Transition(label='Nutrient Prep')
Crop_Select = Transition(label='Crop Select')
Seed_Germinate = Transition(label='Seed Germinate')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Harvest_Automate = Transition(label='Harvest Automate')
Quality_Check = Transition(label='Quality Check')
Pack_Produce = Transition(label='Pack Produce')
Data_Analyze = Transition(label='Data Analyze')
Engage_Community = Transition(label='Engage Community')
Logistics_Plan = Transition(label='Logistics Plan')

# Define the partial order according to the typical workflow described

# Phase 1: Site Survey -> Rack Design -> System Setup -> Climate Calibrate -> Nutrient Prep
phase1_nodes = [Site_Survey, Rack_Design, System_Setup, Climate_Calibrate, Nutrient_Prep]
phase1 = StrictPartialOrder(nodes=phase1_nodes)
phase1.order.add_edge(Site_Survey, Rack_Design)
phase1.order.add_edge(Rack_Design, System_Setup)
phase1.order.add_edge(System_Setup, Climate_Calibrate)
phase1.order.add_edge(Climate_Calibrate, Nutrient_Prep)

# Phase 2: Crop Select -> Seed Germinate
phase2_nodes = [Crop_Select, Seed_Germinate]
phase2 = StrictPartialOrder(nodes=phase2_nodes)
phase2.order.add_edge(Crop_Select, Seed_Germinate)

# Phase 3: Sensor Deploy and Pest Control are concurrent monitoring activities after Seed Germinate
monitoring_nodes = [Sensor_Deploy, Pest_Control]

# Phase 4: Harvest Automate -> Quality Check -> Pack Produce
phase4_nodes = [Harvest_Automate, Quality_Check, Pack_Produce]
phase4 = StrictPartialOrder(nodes=phase4_nodes)
phase4.order.add_edge(Harvest_Automate, Quality_Check)
phase4.order.add_edge(Quality_Check, Pack_Produce)

# Phase 5: Data Analyze and Engage Community can be concurrent after Pack Produce
post_harvest_nodes = [Data_Analyze, Engage_Community]

# Phase 6: Logistics Plan final step after Data Analyze and Engage Community

# Build monitoring partial order (concurrent between Sensor Deploy and Pest Control)
monitoring = StrictPartialOrder(nodes=monitoring_nodes)
# no order edges -> concurrent

# Build post-harvest partial order (concurrent Data Analyze and Engage Community)
post_harvest = StrictPartialOrder(nodes=post_harvest_nodes)
# no order edges -> concurrent

# Compose the whole partial order

# Create one top-level partial order including all nodes and order dependencies

all_nodes = (
    phase1_nodes +
    phase2_nodes +
    monitoring_nodes +
    phase4_nodes +
    post_harvest_nodes +
    [Logistics_Plan]
)

root = StrictPartialOrder(nodes=all_nodes)

# Add edges for phase1
root.order.add_edge(Site_Survey, Rack_Design)
root.order.add_edge(Rack_Design, System_Setup)
root.order.add_edge(System_Setup, Climate_Calibrate)
root.order.add_edge(Climate_Calibrate, Nutrient_Prep)

# phase1 --> phase2
root.order.add_edge(Nutrient_Prep, Crop_Select)

# phase2 --> Seed Germinate
root.order.add_edge(Crop_Select, Seed_Germinate)

# Seed Germinate --> monitoring (Sensor Deploy and Pest Control concurrent)
root.order.add_edge(Seed_Germinate, Sensor_Deploy)
root.order.add_edge(Seed_Germinate, Pest_Control)

# Sensor Deploy and Pest Control complete before Harvest Automate
root.order.add_edge(Sensor_Deploy, Harvest_Automate)
root.order.add_edge(Pest_Control, Harvest_Automate)

# Harvest Automate -> Quality Check -> Pack Produce
root.order.add_edge(Harvest_Automate, Quality_Check)
root.order.add_edge(Quality_Check, Pack_Produce)

# Pack Produce -> Data Analyze and Engage Community (concurrent)
root.order.add_edge(Pack_Produce, Data_Analyze)
root.order.add_edge(Pack_Produce, Engage_Community)

# Data Analyze and Engage Community must complete before Logistics Plan
root.order.add_edge(Data_Analyze, Logistics_Plan)
root.order.add_edge(Engage_Community, Logistics_Plan)