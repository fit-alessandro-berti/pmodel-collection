# Generated from: 65326aae-abe3-4378-a5ec-12bdb86fd491.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm. It includes site evaluation, structural assessments, and soil testing to ensure safety and feasibility. The process continues with irrigation system design, nutrient sourcing, and crop selection tailored for microclimates. It integrates community engagement, permits acquisition, and installation of renewable energy sources to minimize environmental impact. Ongoing monitoring of plant health, pest control using organic methods, and data collection for yield optimization complete the cycle. This atypical business process blends agriculture, engineering, and urban planning to create productive green spaces in dense urban environments, contributing to food security and ecological benefits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Soil_Testing = Transition(label='Soil Testing')

Permit_Filing = Transition(label='Permit Filing')
System_Design = Transition(label='System Design')
Nutrient_Sourcing = Transition(label='Nutrient Sourcing')
Crop_Selection = Transition(label='Crop Selection')

Community_Meet = Transition(label='Community Meet')
Solar_Setup = Transition(label='Solar Setup')
Irrigation_Install = Transition(label='Irrigation Install')

Planting_Seeds = Transition(label='Planting Seeds')
Pest_Control = Transition(label='Pest Control')
Health_Monitor = Transition(label='Health Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Waste_Manage = Transition(label='Waste Manage')
Data_Logging = Transition(label='Data Logging')

# First partial order: site evaluation steps (Site Survey -> Structural Check -> Soil Testing)
site_eval = StrictPartialOrder(nodes=[Site_Survey, Structural_Check, Soil_Testing])
site_eval.order.add_edge(Site_Survey, Structural_Check)
site_eval.order.add_edge(Structural_Check, Soil_Testing)

# Second partial order: design and sourcing activities with partial concurrency
# Permit filing must be done first before system design, sourcing, and crop selection which can run concurrently after
permits = Permit_Filing
design = System_Design
nutrient = Nutrient_Sourcing
crop = Crop_Selection

design_block = StrictPartialOrder(nodes=[design, nutrient, crop])
# design, nutrient, crop partly concurrent (no order edges)

# third partial order: community engagement and renewable setup (Community Meet -> Solar Setup & Irrigation Install concurrent)
comm_meet = Community_Meet
solar = Solar_Setup
irrigation = Irrigation_Install

comm_block = StrictPartialOrder(nodes=[comm_meet, solar, irrigation])
comm_block.order.add_edge(comm_meet, solar)
comm_block.order.add_edge(comm_meet, irrigation)

# Putting design and community blocks in parallel after permits
permits_and_design = StrictPartialOrder(nodes=[permits, design_block, comm_block])
permits_and_design.order.add_edge(permits, design_block)
permits_and_design.order.add_edge(permits, comm_block)

# Fourth partial order: planting and ongoing monitoring cycle
# Model the loop of monitoring: execute Planting Seeds, then loop over (Pest Control, Health Monitor, Yield Analyze, Waste Manage, Data Logging)
planting = Planting_Seeds
pest = Pest_Control
health = Health_Monitor
yield_a = Yield_Analyze
waste = Waste_Manage
data = Data_Logging

# Monitoring partial order (some concurrency allowed among pest control and health monitor, others sequential)
monitor = StrictPartialOrder(nodes=[pest, health, yield_a, waste, data])
# Pest Control and Health Monitor concurrent, both precede Yield Analyze
monitor.order.add_edge(pest, yield_a)
monitor.order.add_edge(health, yield_a)
# Yield Analyze precedes Waste Manage and Data Logging (order them sequentially)
monitor.order.add_edge(yield_a, waste)
monitor.order.add_edge(waste, data)

# Loop: execute Planting, then repeat monitoring and planting until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[planting, monitor])

# Combine all main parts sequentially: site evaluation -> permits and design+community -> loop planting+monitoring
root = StrictPartialOrder(nodes=[site_eval, permits_and_design, loop])
root.order.add_edge(site_eval, permits_and_design)
root.order.add_edge(permits_and_design, loop)