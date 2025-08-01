# Generated from: 60eeb967-00e4-46dc-b889-14c0279b7324.json
# Description: This process outlines the complex establishment of an urban vertical farm within a repurposed industrial building. It involves assessing structural integrity, designing modular growth units, integrating IoT sensors for environmental control, sourcing sustainable water and nutrient supplies, and implementing energy-efficient LED lighting systems. The process also includes staff training on crop management, scheduling automated harvesting, and establishing supply chain logistics for local distribution. Continuous monitoring and iterative optimization ensure maximum yield and minimal resource waste, adapting to seasonal and market variations in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities with exact names
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Unit_Design = Transition(label='Unit Design')
Sensor_Setup = Transition(label='Sensor Setup')
Water_Sourcing = Transition(label='Water Sourcing')
Nutrient_Prep = Transition(label='Nutrient Prep')
Lighting_Install = Transition(label='Lighting Install')
System_Integrate = Transition(label='System Integrate')
Staff_Train = Transition(label='Staff Train')
Crop_Plan = Transition(label='Crop Plan')
Automation_Setup = Transition(label='Automation Setup')
Harvest_Schedule = Transition(label='Harvest Schedule')
Supply_Chain = Transition(label='Supply Chain')
Yield_Monitor = Transition(label='Yield Monitor')
Optimize_Process = Transition(label='Optimize Process')
Waste_Manage = Transition(label='Waste Manage')
Market_Adapt = Transition(label='Market Adapt')

# Build the partial order:

# Phase 1: Site survey and structural check in sequence
phase1 = StrictPartialOrder(nodes=[Site_Survey, Structural_Check])
phase1.order.add_edge(Site_Survey, Structural_Check)

# Phase 2: Design and installation in parallel branches then integration

# Design units branch: Unit_Design
# Sensor setup branch: Sensor_Setup
# Water and nutrient preparation branch (Water_Sourcing and Nutrient_Prep sequential)
water_nutrient = StrictPartialOrder(nodes=[Water_Sourcing, Nutrient_Prep])
water_nutrient.order.add_edge(Water_Sourcing, Nutrient_Prep)
# Lighting install branch: Lighting_Install

# Combine these four branches in parallel (no order edges)
phase2_nodes = [Unit_Design, Sensor_Setup, water_nutrient, Lighting_Install]

# Because water_nutrient is a StrictPartialOrder object, include nodes and edges accordingly
# We'll include water_nutrient as a node in a higher-level PO to have proper partial orders

# So phase2 is a StrictPartialOrder including Unit_Design, Sensor_Setup, Lighting_Install and water_nutrient PO as a node
phase2 = StrictPartialOrder(nodes=[Unit_Design, Sensor_Setup, Lighting_Install, water_nutrient])

# After these parallel branches, System_Integrate

# phase2 to System_Integrate
phase2_to_integrate = StrictPartialOrder(nodes=[phase2, System_Integrate])
phase2_to_integrate.order.add_edge(phase2, System_Integrate)

# Phase 3: Staff training, crop plan, automation setup, harvest schedule, supply chain logistics
# These are best modeled in a partial order reflecting dependencies from context:
# Staff_Train -> Crop_Plan
# Crop_Plan -> Automation_Setup
# Automation_Setup -> Harvest_Schedule
# Harvest_Schedule -> Supply_Chain

phase3 = StrictPartialOrder(nodes=[Staff_Train, Crop_Plan, Automation_Setup, Harvest_Schedule, Supply_Chain])
phase3.order.add_edge(Staff_Train, Crop_Plan)
phase3.order.add_edge(Crop_Plan, Automation_Setup)
phase3.order.add_edge(Automation_Setup, Harvest_Schedule)
phase3.order.add_edge(Harvest_Schedule, Supply_Chain)

# Phase 4: Continuous monitoring and iterative optimization (loop)
# Loop body A = Yield_Monitor
# Loop body B = Parallel optimization steps: Optimize_Process, Waste_Manage, Market_Adapt (concurrent)

phase4_body_B = StrictPartialOrder(nodes=[Optimize_Process, Waste_Manage, Market_Adapt])  # concurrent

loop_monitor_optimize = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Monitor, phase4_body_B])

# Bring together phases in the overall flow:

# Order:
# phase1 --> phase2_to_integrate --> phase3 --> loop_monitor_optimize

root = StrictPartialOrder(nodes=[phase1, phase2_to_integrate, phase3, loop_monitor_optimize])
root.order.add_edge(phase1, phase2_to_integrate)
root.order.add_edge(phase2_to_integrate, phase3)
root.order.add_edge(phase3, loop_monitor_optimize)