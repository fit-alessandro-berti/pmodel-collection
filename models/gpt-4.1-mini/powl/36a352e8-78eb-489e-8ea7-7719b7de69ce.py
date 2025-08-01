# Generated from: 36a352e8-78eb-489e-8ea7-7719b7de69ce.json
# Description: This process outlines the comprehensive cycle of urban vertical farming, integrating advanced hydroponics, automated nutrient delivery, and environmental controls to maximize crop yield in limited city spaces. It involves seed selection, germination monitoring, nutrient mixing, growth tracking, pest control, harvesting automation, and waste recycling. Data from IoT sensors continuously optimize conditions for plant health, while logistics ensure fresh produce distribution within tight urban supply chains. The process also includes energy management for sustainable operation and post-harvest quality assessment to maintain food safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Germination_Check = Transition(label='Germination Check')
Nutrient_Mix = Transition(label='Nutrient Mix')
Planting_Setup = Transition(label='Planting Setup')
Environment_Adjust = Transition(label='Environment Adjust')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Inspection = Transition(label='Pest Inspection')
Irrigation_Control = Transition(label='Irrigation Control')
Light_Calibration = Transition(label='Light Calibration')
Harvest_Schedule = Transition(label='Harvest Schedule')
Automated_Picking = Transition(label='Automated Picking')
Waste_Sorting = Transition(label='Waste Sorting')
Energy_Audit = Transition(label='Energy Audit')
Quality_Assess = Transition(label='Quality Assess')
Produce_Packing = Transition(label='Produce Packing')
Supply_Dispatch = Transition(label='Supply Dispatch')

# Partial order modeling the process flow

# Initial phase: seed selection -> germination check -> nutrient mixing -> planting setup
initial_phase = StrictPartialOrder(nodes=[Seed_Selection, Germination_Check, Nutrient_Mix, Planting_Setup])
initial_phase.order.add_edge(Seed_Selection, Germination_Check)
initial_phase.order.add_edge(Germination_Check, Nutrient_Mix)
initial_phase.order.add_edge(Nutrient_Mix, Planting_Setup)

# Environment and growth monitoring activities can run concurrently after planting setup
env_growth_nodes = [Environment_Adjust, Growth_Monitor, Pest_Inspection, Irrigation_Control, Light_Calibration]
env_growth = StrictPartialOrder(nodes=env_growth_nodes)
# These run concurrently: no order edges set

# Harvest automation and waste sorting sequence
harvest_phase = StrictPartialOrder(nodes=[Harvest_Schedule, Automated_Picking, Waste_Sorting])
harvest_phase.order.add_edge(Harvest_Schedule, Automated_Picking)
harvest_phase.order.add_edge(Automated_Picking, Waste_Sorting)

# Energy audit can be performed anytime after planting setup (concurrent with monitoring and harvest)
energy_audit = Energy_Audit

# Quality assessment and packing follow harvest and waste sorting
post_harvest_phase = StrictPartialOrder(nodes=[Quality_Assess, Produce_Packing, Supply_Dispatch])
post_harvest_phase.order.add_edge(Quality_Assess, Produce_Packing)
post_harvest_phase.order.add_edge(Produce_Packing, Supply_Dispatch)

# Compose the monitoring and harvest-related phases in partial order
monitoring_and_energy = StrictPartialOrder(nodes=[env_growth, energy_audit])
monitoring_and_energy.order.add_edge(env_growth, energy_audit)  # Let energy audit start after environment/growth monitoring starts

# Combine harvest and post harvest phases with edge from harvest_phase to post_harvest_phase
harvest_and_post = StrictPartialOrder(nodes=[harvest_phase, post_harvest_phase])
harvest_and_post.order.add_edge(harvest_phase, post_harvest_phase)

# Root partial order: initial phase -> monitoring and energy and harvest_and_post phases run concurrently after initial phase
root = StrictPartialOrder(nodes=[initial_phase, monitoring_and_energy, harvest_and_post])
root.order.add_edge(initial_phase, monitoring_and_energy)
root.order.add_edge(initial_phase, harvest_and_post)