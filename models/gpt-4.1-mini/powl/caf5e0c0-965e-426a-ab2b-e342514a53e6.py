# Generated from: caf5e0c0-965e-426a-ab2b-e342514a53e6.json
# Description: This process outlines the complex workflow required to establish a fully automated urban vertical farm within a repurposed industrial building. It involves site analysis, modular system design, environmental calibration, seed selection based on climate simulation, nutrient cycling optimization, and AI-driven growth monitoring. Additionally, it includes integration with local energy grids for sustainable power usage, water recycling mechanisms, pest detection through image recognition, and community engagement for local produce distribution. The process culminates with regulatory compliance checks and ongoing system maintenance protocols to ensure continuous yield and minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
climate_sim = Transition(label='Climate Sim')
seed_select = Transition(label='Seed Select')
module_setup = Transition(label='Module Setup')
nutrient_mix = Transition(label='Nutrient Mix')
water_cycle = Transition(label='Water Cycle')
energy_link = Transition(label='Energy Link')
sensor_install = Transition(label='Sensor Install')
pest_detect = Transition(label='Pest Detect')
growth_scan = Transition(label='Growth Scan')
data_sync = Transition(label='Data Sync')
community_meet = Transition(label='Community Meet')
reg_compliance = Transition(label='Reg Compliance')
system_test = Transition(label='System Test')
maintenance_plan = Transition(label='Maintenance Plan')

# Based on the description, the workflow can be partially ordered roughly as follows:

# Phase 1: Establishment & Setup
# Site Survey --> System Design --> Module Setup --> Sensor Install
# Phase 2: Calibration & Selection (some concurrency possible)
# Climate Sim --> Seed Select
# Nutrient Mix
# The calibration and seed selection depend on design but can run concurrently with nutrient mix after module setup

# Phase 3: Operations & Monitoring
# Water Cycle and Energy Link (can run concurrently after module setup)
# Pest Detect --> Growth Scan --> Data Sync (pest detect before scan and sync)
# Community Meet (depends on Growth Scan and Data Sync to have data)

# Phase 4: Compliance & Testing
# Reg Compliance, System Test (can be done after core setup and monitoring start)

# Phase 5: Maintenance Plan (an ongoing loop after testing and compliance)
# Loop: Maintenance Plan and optionally repeat System Test

# Construct PO with the above partial order

# For the loop: execute Maintenance Plan, then choose to exit or do System Test then Maintenance Plan again
loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, system_test])

# We will build the strict partial order step by step

nodes = [site_survey, system_design, module_setup, sensor_install,
         climate_sim, seed_select, nutrient_mix,
         water_cycle, energy_link,
         pest_detect, growth_scan, data_sync,
         community_meet,
         reg_compliance, loop]

root = StrictPartialOrder(nodes=nodes)

# Site Survey --> System Design --> Module Setup --> Sensor Install
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, module_setup)
root.order.add_edge(module_setup, sensor_install)

# After Module Setup:
# Climate Sim and Nutrient Mix and Water Cycle and Energy Link can start
root.order.add_edge(module_setup, climate_sim)
root.order.add_edge(module_setup, nutrient_mix)
root.order.add_edge(module_setup, water_cycle)
root.order.add_edge(module_setup, energy_link)

# Seed Select after Climate Sim
root.order.add_edge(climate_sim, seed_select)

# Pest detection likely after Sensor Install
root.order.add_edge(sensor_install, pest_detect)

# Growth Scan after Pest Detect
root.order.add_edge(pest_detect, growth_scan)

# Data Sync after Growth Scan
root.order.add_edge(growth_scan, data_sync)

# Community Meet after Data Sync (and also after Seed Select logically, assume after seed select)
root.order.add_edge(data_sync, community_meet)
root.order.add_edge(seed_select, community_meet)

# Reg Compliance after Community Meet (and Nutrient Mix done before compliance)
root.order.add_edge(community_meet, reg_compliance)
root.order.add_edge(nutrient_mix, reg_compliance)

# The loop (Maintenance Plan and System Test) starts after Reg Compliance
root.order.add_edge(reg_compliance, loop)

# This defines the partial order with concurrency where edges are missing.

# final root variable contains the model