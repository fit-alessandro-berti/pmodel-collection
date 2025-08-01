# Generated from: 5070eaa7-81cd-4e9e-9eb9-9f45374a974c.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a constrained city environment. It begins with site analysis and zoning approval, followed by modular infrastructure assembly and environmental control calibration. The process includes nutrient solution formulation, crop selection tailored to vertical layers, and integration of AI-driven monitoring systems. Waste recycling loops and energy optimization are implemented to ensure sustainability. Continuous data analysis guides adaptive growth protocols, while supply chain synchronization ensures timely distribution to local markets. The entire operation demands coordination between agricultural scientists, engineers, local authorities, and logistics teams to achieve efficient urban agriculture that maximizes yield and minimizes ecological footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Analysis = Transition(label='Site Analysis')
Zoning_Approval = Transition(label='Zoning Approval')
Modular_Assembly = Transition(label='Modular Assembly')
Env_Control = Transition(label='Env Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Selection = Transition(label='Crop Selection')
AI_Monitoring = Transition(label='AI Monitoring')
Waste_Recycling = Transition(label='Waste Recycling')
Energy_Audit = Transition(label='Energy Audit')
Data_Analysis = Transition(label='Data Analysis')
Growth_Tuning = Transition(label='Growth Tuning')
Supply_Sync = Transition(label='Supply Sync')
Market_Outreach = Transition(label='Market Outreach')
Staff_Training = Transition(label='Staff Training')
Quality_Check = Transition(label='Quality Check')
Harvest_Plan = Transition(label='Harvest Plan')

# Loop for Waste Recycling and Energy Optimization
# Loop body: Waste Recycling then Energy Audit, then decision to continue looping or exit.
waste_energy_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Waste_Recycling, Energy_Audit]
)

# Loop for Data Analysis and Growth Tuning
# Loop body: Data Analysis then Growth Tuning, then decision to continue looping or exit.
data_growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Data_Analysis, Growth_Tuning]
)

# Partial order capturing sequential activities and concurrency

# First phase: Site Analysis -> Zoning Approval -> Modular Assembly -> Env Control
phase1 = StrictPartialOrder(
    nodes=[Site_Analysis, Zoning_Approval, Modular_Assembly, Env_Control]
)
phase1.order.add_edge(Site_Analysis, Zoning_Approval)
phase1.order.add_edge(Zoning_Approval, Modular_Assembly)
phase1.order.add_edge(Modular_Assembly, Env_Control)

# Second phase: Nutrient Mix and Crop Selection concur, then both join into AI Monitoring
nutrient_crop = StrictPartialOrder(
    nodes=[Nutrient_Mix, Crop_Selection, AI_Monitoring]
)
nutrient_crop.order.add_edge(Nutrient_Mix, AI_Monitoring)
nutrient_crop.order.add_edge(Crop_Selection, AI_Monitoring)

# Third phase: Trash loop and data loop run concurrently but both precede Supply Sync
phase3 = StrictPartialOrder(
    nodes=[waste_energy_loop, data_growth_loop, Supply_Sync]
)
phase3.order.add_edge(waste_energy_loop, Supply_Sync)
phase3.order.add_edge(data_growth_loop, Supply_Sync)

# Fourth phase:
# Market Outreach, Staff Training, Quality Check, Harvest Plan
# Staff Training, Quality Check, Harvest Plan all after Market Outreach
phase4 = StrictPartialOrder(
    nodes=[Market_Outreach, Staff_Training, Quality_Check, Harvest_Plan]
)
phase4.order.add_edge(Market_Outreach, Staff_Training)
phase4.order.add_edge(Market_Outreach, Quality_Check)
phase4.order.add_edge(Market_Outreach, Harvest_Plan)

# Compose partial orders in final model with global order between phases:
# phase1 -> nutrient_crop -> Env_Control -> phase3 -> phase4

# Since Env_Control is end of phase1, and nutrient_crop starts after Env_Control,
# we link Env_Control to Nutrient Mix and Crop Selection (both start nutrient_crop)
# Then AI Monitoring completes nutrient_crop. We'll infer the dependency only in one place because
# nutrient_crop nodes: Nutrient_Mix, Crop_Selection, AI_Monitoring. Dependencies already inside nutrient_crop.

# We'll build root as a partial order combining all components, linking with edges:

root = StrictPartialOrder(
    nodes=[phase1, nutrient_crop, phase3, phase4, Env_Control]
)

# Phase1 orderings are internal, but phase1 is the POWL object with nodes inside it
# So we add edges across top-level nodes (the partial orders themselves) to impose global order.

# We know Env_Control is part of phase1 but we put it as separate node in root so that we can connect nutrient_crop after Env_Control.
# So instead, we have Env_Control twice? No, we already included Env_Control in phase1.
# We should not add Env_Control separately in root if it's in phase1.

# Correcting this: Env_Control is node of phase1. So root nodes are phase1, nutrient_crop, phase3, phase4.

root = StrictPartialOrder(
    nodes=[phase1, nutrient_crop, phase3, phase4]
)

# Add edges between partial orders to capture ordering dependencies:
# phase1 -> nutrient_crop
# nutrient_crop -> phase3
# phase3 -> phase4

root.order.add_edge(phase1, nutrient_crop)
root.order.add_edge(nutrient_crop, phase3)
root.order.add_edge(phase3, phase4)