# Generated from: 56ff8dfc-f084-4883-a2a0-6b210f47e3a0.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It includes site analysis, structural modifications for optimal light penetration, integration of hydroponic and aeroponic systems, climate control calibration, nutrient monitoring, pest management with biological agents, automated harvesting mechanisms, waste recycling protocols, and community engagement initiatives. The process ensures sustainable, high-yield crop production in an urban environment by leveraging cutting-edge agricultural technologies while minimizing environmental impact and maximizing space efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label="Site Survey")
structural_audit = Transition(label="Structural Audit")
energy_audit     = Transition(label="Energy Audit")
light_design     = Transition(label="Light Design")
system_install   = Transition(label="System Install")
climate_setup    = Transition(label="Climate Setup")
tech_sync        = Transition(label="Tech Sync")
harvest_plan     = Transition(label="Harvest Plan")
seed_selection   = Transition(label="Seed Selection")

growth_monitor   = Transition(label="Growth Monitor")
nutrient_mix     = Transition(label="Nutrient Mix")
water_test       = Transition(label="Water Test")
pest_control     = Transition(label="Pest Control")

waste_cycle      = Transition(label="Waste Cycle")
data_review      = Transition(label="Data Review")
community_meet   = Transition(label="Community Meet")

# Build the loop body: parallel adjustments inside each growth cycle
loop_body = StrictPartialOrder(nodes=[nutrient_mix, water_test, pest_control])
# no order edges => these three can be done in parallel

# Define the loop: 
#   A = growth_monitor (happens first and after each redo)
#   B = loop_body  (redo part, then back to A)
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, loop_body]
)

# Root partial order combining all phases
root = StrictPartialOrder(
    nodes=[
        site_survey,
        structural_audit,
        energy_audit,
        light_design,
        system_install,
        climate_setup,
        tech_sync,
        harvest_plan,
        seed_selection,
        growth_loop,
        waste_cycle,
        data_review,
        community_meet
    ]
)

# Define the control-flow (partial order edges)
# 1. Assessment phase
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, energy_audit)

# 2. Design & integration phase
root.order.add_edge(energy_audit, light_design)
root.order.add_edge(light_design, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(climate_setup, tech_sync)

# 3. Planning phase (parallel Harvest Plan & Seed Selection)
root.order.add_edge(tech_sync, harvest_plan)
root.order.add_edge(tech_sync, seed_selection)

# 4. Enter growth loop after planning
root.order.add_edge(harvest_plan, growth_loop)
root.order.add_edge(seed_selection, growth_loop)

# 5. Exit loop and finalize
root.order.add_edge(growth_loop, waste_cycle)
root.order.add_edge(waste_cycle, data_review)
root.order.add_edge(data_review, community_meet)