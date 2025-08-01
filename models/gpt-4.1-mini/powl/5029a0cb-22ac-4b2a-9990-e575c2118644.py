# Generated from: 5029a0cb-22ac-4b2a-9990-e575c2118644.json
# Description: This process governs the comprehensive cycle of urban vertical farming operations, integrating advanced hydroponics, AI-driven climate control, and waste recycling to optimize crop yield in limited spaces. It begins with site assessment and modular setup, followed by nutrient solution preparation and seed germination under automated lighting. Continuous monitoring adjusts environmental factors to maintain ideal growth conditions. Pollination is handled mechanically or via introduced insects. Harvesting is robotic, with quality sorting and packaging tailored for urban distribution channels. Waste biomass is processed into compost or bioenergy, closing the sustainability loop. Data analytics feed into predictive maintenance and crop planning, ensuring maximum efficiency and minimal resource consumption throughout the cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Assess = Transition(label='Site Assess')
Module_Setup = Transition(label='Module Setup')
Seed_Germinate = Transition(label='Seed Germinate')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Control = Transition(label='Climate Control')
Pollination_Aid = Transition(label='Pollination Aid')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Detect = Transition(label='Pest Detect')
Harvest_Crop = Transition(label='Harvest Crop')
Quality_Check = Transition(label='Quality Check')
Package_Goods = Transition(label='Package Goods')
Waste_Process = Transition(label='Waste Process')
Compost_Create = Transition(label='Compost Create')
Energy_Generate = Transition(label='Energy Generate')
Data_Analyze = Transition(label='Data Analyze')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Site assessment and module setup partial order
site_module = StrictPartialOrder(nodes=[Site_Assess, Module_Setup])
site_module.order.add_edge(Site_Assess, Module_Setup)

# Nutrient solution preparation and seed germination concurrent
nutrient_seed = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Germinate])
# No order between Nutrient Mix and Seed Germinate (concurrent)

# Autonomous lighting included in Seed Germinate implicitly

# Continuous monitoring cluster and pest detection concurrent (both adjusting environmental factors)
monitoring = StrictPartialOrder(nodes=[Climate_Control, Growth_Monitor, Pest_Detect])
# No order between these nodes (concurrent)

# Pollination handled mechanically or via introduced insects - modeled as choice
pollination_choice = OperatorPOWL(operator=Operator.XOR, children=[Pollination_Aid, Pest_Detect]) 
# Pollination or Pest Detect - but Pest Detect is also in monitoring; 
# However, Pest Detect is monitoring activity, not an alternative pollination.
# Re-examine: Pollination is done mechanically or via introduced insects.
# Pest_Detect is separate (detect pests), so pollination choice is mechanical or insects.
# We'll model Pollination Aid or silent transition to represent insects introduced (no explicit insect activity)
# But insects introduced is not an activity. So we use choice Pollination Aid or silent activity
pollination_choice = OperatorPOWL(operator=Operator.XOR, children=[Pollination_Aid, SilentTransition()])

# Harvesting, quality check, packaging - linear flow
harvest_phase = StrictPartialOrder(nodes=[Harvest_Crop, Quality_Check, Package_Goods])
harvest_phase.order.add_edge(Harvest_Crop, Quality_Check)
harvest_phase.order.add_edge(Quality_Check, Package_Goods)

# Waste biomass processing choice: compost or bioenergy
waste_choice = OperatorPOWL(operator=Operator.XOR, children=[Compost_Create, Energy_Generate])
waste_processing = StrictPartialOrder(nodes=[Waste_Process, waste_choice])
waste_processing.order.add_edge(Waste_Process, waste_choice)

# Data analytics leads to maintenance planning (sequential)
data_maintenance = StrictPartialOrder(nodes=[Data_Analyze, Maintenance_Plan])
data_maintenance.order.add_edge(Data_Analyze, Maintenance_Plan)

# Now combine all phases, respecting the logical order from description:

# Phase 1: site_module --> nutrient_seed --> monitoring --> pollination_choice --> harvest_phase --> waste_processing --> data_maintenance

root = StrictPartialOrder(
    nodes=[site_module, nutrient_seed, monitoring, pollination_choice, harvest_phase, waste_processing, data_maintenance]
)

root.order.add_edge(site_module, nutrient_seed)
root.order.add_edge(nutrient_seed, monitoring)
root.order.add_edge(monitoring, pollination_choice)
root.order.add_edge(pollination_choice, harvest_phase)
root.order.add_edge(harvest_phase, waste_processing)
root.order.add_edge(waste_processing, data_maintenance)