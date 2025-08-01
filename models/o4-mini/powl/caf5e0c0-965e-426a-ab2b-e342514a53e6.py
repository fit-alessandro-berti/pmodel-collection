# Generated from: caf5e0c0-965e-426a-ab2b-e342514a53e6.json
# Description: This process outlines the complex workflow required to establish a fully automated urban vertical farm within a repurposed industrial building. It involves site analysis, modular system design, environmental calibration, seed selection based on climate simulation, nutrient cycling optimization, and AI-driven growth monitoring. Additionally, it includes integration with local energy grids for sustainable power usage, water recycling mechanisms, pest detection through image recognition, and community engagement for local produce distribution. The process culminates with regulatory compliance checks and ongoing system maintenance protocols to ensure continuous yield and minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
site_survey     = Transition(label='Site Survey')
system_design   = Transition(label='System Design')
climate_sim     = Transition(label='Climate Sim')
seed_select     = Transition(label='Seed Select')
module_setup    = Transition(label='Module Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
water_cycle     = Transition(label='Water Cycle')
energy_link     = Transition(label='Energy Link')
sensor_install  = Transition(label='Sensor Install')
pest_detect     = Transition(label='Pest Detect')
growth_scan     = Transition(label='Growth Scan')
data_sync       = Transition(label='Data Sync')
community_meet  = Transition(label='Community Meet')
reg_compliance  = Transition(label='Reg Compliance')
system_test     = Transition(label='System Test')
maintenance_plan= Transition(label='Maintenance Plan')

# Silent transition for loop exits
skip = SilentTransition()

# Branch 1: physical setup & testing
branch1 = StrictPartialOrder(nodes=[module_setup, sensor_install, system_test])
branch1.order.add_edge(module_setup, sensor_install)
branch1.order.add_edge(sensor_install, system_test)

# Branch 2: environment calibration & resource linking
branch2 = StrictPartialOrder(nodes=[climate_sim, seed_select, nutrient_mix, water_cycle, energy_link])
branch2.order.add_edge(climate_sim,   seed_select)
branch2.order.add_edge(seed_select,   nutrient_mix)
branch2.order.add_edge(nutrient_mix,  water_cycle)
branch2.order.add_edge(water_cycle,   energy_link)

# Loop for repeated pest detection & growth scanning
inner_loop = StrictPartialOrder(nodes=[pest_detect, growth_scan])
inner_loop.order.add_edge(pest_detect, growth_scan)
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[inner_loop, skip])

# Loop for ongoing maintenance protocols
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, skip])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    system_design,
    branch1,
    branch2,
    data_sync,
    loop1,
    community_meet,
    reg_compliance,
    loop2
])
# Establish control‐flow dependencies
root.order.add_edge(site_survey,   system_design)
root.order.add_edge(system_design, branch1)
root.order.add_edge(system_design, branch2)
root.order.add_edge(branch1,       data_sync)
root.order.add_edge(branch2,       data_sync)
root.order.add_edge(data_sync,     loop1)
root.order.add_edge(loop1,         community_meet)
root.order.add_edge(community_meet,reg_compliance)
root.order.add_edge(reg_compliance,loop2)