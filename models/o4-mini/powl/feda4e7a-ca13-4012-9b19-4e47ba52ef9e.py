# Generated from: feda4e7a-ca13-4012-9b19-4e47ba52ef9e.json
# Description: This process details the comprehensive lifecycle of an urban vertical farming operation integrating hydroponics, AI-driven climate control, and community-driven crop selection. It begins with site analysis and environmental scanning, followed by modular farm design and nutrient solution formulation. Automated seeding and growth monitoring leverage sensor data to optimize plant health. Periodic pest and disease management is conducted using bio-control agents and AI diagnostics. Harvesting is scheduled based on predictive analytics, with produce sorted and packaged through robotic lines. Community feedback is aggregated to refine crop varieties and distribution models. Waste is recycled into compost or biogas, closing the sustainability loop. This atypical process combines technology, ecology, and social dynamics to redefine urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis    = Transition(label='Site Analysis')
env_scanning     = Transition(label='Env Scanning')
farm_design      = Transition(label='Farm Design')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_automation  = Transition(label='Seed Automation')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
ai_diagnostics   = Transition(label='AI Diagnostics')
harvest_plan     = Transition(label='Harvest Plan')
robotic_sort     = Transition(label='Robotic Sort')
packaging_line   = Transition(label='Packaging Line')
community_input  = Transition(label='Community Input')
data_aggregation = Transition(label='Data Aggregation')
waste_recycle    = Transition(label='Waste Recycle')
sustainability   = Transition(label='Sustainability')

# A = the planting & early growth phase: Nutrient Mix -> Seeding -> Growth Monitor
A = StrictPartialOrder(nodes=[nutrient_mix, seed_automation, growth_monitor])
A.order.add_edge(nutrient_mix, seed_automation)
A.order.add_edge(seed_automation, growth_monitor)

# B = the production cycle: Pest Control -> AI Diagnostics -> Harvesting -> Sorting -> Packaging
#      -> Community Input -> Data Aggregation -> Waste Recycle
cycle_nodes = [
    pest_control,
    ai_diagnostics,
    harvest_plan,
    robotic_sort,
    packaging_line,
    community_input,
    data_aggregation,
    waste_recycle
]
B = StrictPartialOrder(nodes=cycle_nodes)
for src, tgt in zip(cycle_nodes, cycle_nodes[1:]):
    B.order.add_edge(src, tgt)

# Loop over the main production cycle:
#   1) do A (planting & early growth)
#   2) choose: exit OR do B then go back to A
main_cycle = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Top-level sequence: Site Analysis -> Env Scanning -> Farm Design -> main_cycle -> Sustainability
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_scanning,
    farm_design,
    main_cycle,
    sustainability
])
root.order.add_edge(site_analysis, env_scanning)
root.order.add_edge(env_scanning, farm_design)
root.order.add_edge(farm_design, main_cycle)
root.order.add_edge(main_cycle, sustainability)