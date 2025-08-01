# Generated from: 8e95232d-b26d-4937-96cf-bf16a7928526.json
# Description: This process outlines the complex operational cycle of an urban vertical farm integrating hydroponics, AI-driven environmental controls, and sustainable waste recycling. Activities include seed selection, nutrient mixing, automated planting, continuous growth monitoring, pest bio-control, adaptive lighting adjustment, climate regulation, precision harvesting, biomass repurposing, energy optimization, data analytics feedback, and distribution logistics. The cycle emphasizes minimizing resource use while maximizing yield and quality, involving multiple feedback loops and cross-functional coordination between agronomy, engineering, and supply chain teams to ensure efficient, eco-friendly urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automated_Planting = Transition(label='Automated Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Light_Adjust = Transition(label='Light Adjust')
Climate_Regulate = Transition(label='Climate Regulate')
Water_Recycle = Transition(label='Water Recycle')
Harvest_Crop = Transition(label='Harvest Crop')
Biomass_Repurpose = Transition(label='Biomass Repurpose')
Energy_Optimize = Transition(label='Energy Optimize')
Data_Analyze = Transition(label='Data Analyze')
Quality_Check = Transition(label='Quality Check')
Supply_Pack = Transition(label='Supply Pack')
Delivery_Schedule = Transition(label='Delivery Schedule')

# Loop 1: Growth cycle loop after planting:
# Growth_Monitor then choice (Pest_Control or Light_Adjust or Climate_Regulate or Water_Recycle) then back to Growth_Monitor or exit
# Model the choice of treatments as XOR over Pest_Control, Light_Adjust, Climate_Regulate, Water_Recycle, plus option to skip (silent)
treatment_choice = OperatorPOWL(
    operator=Operator.XOR, 
    children=[Pest_Control, Light_Adjust, Climate_Regulate, Water_Recycle]
)
# To allow repeated monitoring and treatments, loop structure: 
# execute Growth_Monitor (A), then choose exit or (B) treatment_choice + Growth_Monitor again
growth_loop_body = StrictPartialOrder(nodes=[treatment_choice, Growth_Monitor])
growth_loop_body.order.add_edge(treatment_choice, Growth_Monitor)

growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Growth_Monitor, growth_loop_body]
)

# After growth loop, proceed to harvesting and post-harvest processing:
# Harvest_Crop -> Biomass_Repurpose and Energy_Optimize in parallel -> Data_Analyze -> Quality_Check -> Supply_Pack -> Delivery_Schedule

# Biomass_Repurpose and Energy_Optimize concurrent
post_harvest_po = StrictPartialOrder(nodes=[Biomass_Repurpose, Energy_Optimize])

# Full post-harvest sequence
post_harvest_seq = StrictPartialOrder(
    nodes=[Harvest_Crop, post_harvest_po, Data_Analyze, Quality_Check, Supply_Pack, Delivery_Schedule]
)
post_harvest_seq.order.add_edge(Harvest_Crop, post_harvest_po)
post_harvest_seq.order.add_edge(post_harvest_po, Data_Analyze)
post_harvest_seq.order.add_edge(Data_Analyze, Quality_Check)
post_harvest_seq.order.add_edge(Quality_Check, Supply_Pack)
post_harvest_seq.order.add_edge(Supply_Pack, Delivery_Schedule)

# Initial sequence: Seed_Selection -> Nutrient_Mix -> Automated_Planting -> growth_loop -> post_harvest_seq
initial_seq_nodes = [Seed_Selection, Nutrient_Mix, Automated_Planting, growth_loop, post_harvest_seq]
root = StrictPartialOrder(nodes=initial_seq_nodes)
root.order.add_edge(Seed_Selection, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Automated_Planting)
root.order.add_edge(Automated_Planting, growth_loop)
root.order.add_edge(growth_loop, post_harvest_seq)