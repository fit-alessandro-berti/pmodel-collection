# Generated from: 808a64a4-a89e-473b-8423-3e1418a72c01.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, environmental control calibration, nutrient solution preparation, seed selection, and automated planting. Continuous monitoring of plant growth, pest detection using AI, and adaptive lighting adjustments are essential. The process also includes waste recycling, data analytics for yield optimization, and community engagement for local distribution. Finally, the system undergoes periodic maintenance and scalability evaluation to ensure sustainable production and economic viability in a densely populated urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
system_design    = Transition(label='System Design')
env_calibration  = Transition(label='Env Calibration')
seed_selection   = Transition(label='Seed Selection')
nutrient_prep    = Transition(label='Nutrient Prep')
automated_plant  = Transition(label='Automated Plant')

growth_monitor   = Transition(label='Growth Monitor')
pest_detection   = Transition(label='Pest Detection')
lighting_adjust  = Transition(label='Lighting Adjust')

waste_recycle    = Transition(label='Waste Recycle')
data_analyze     = Transition(label='Data Analyze')
yield_optimize   = Transition(label='Yield Optimize')
community_engage = Transition(label='Community Engage')

system_maintain  = Transition(label='System Maintain')
scale_evaluate   = Transition(label='Scale Evaluate')

# Continuous monitoring loop: do growth_monitor, then optionally do pest_detection & lighting_adjust concurrently, then repeat
monitoring_redo = StrictPartialOrder(nodes=[pest_detection, lighting_adjust])
cont_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, monitoring_redo])

# Maintenance & scalability loop: do system_maintain, then optionally scale_evaluate, then repeat
maint_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_maintain, scale_evaluate])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    system_design,
    env_calibration,
    seed_selection,
    nutrient_prep,
    automated_plant,
    cont_loop,
    waste_recycle,
    data_analyze,
    yield_optimize,
    community_engage,
    maint_loop
])

# Define the control-flow order
root.order.add_edge(site_survey,     system_design)
root.order.add_edge(system_design,   env_calibration)
root.order.add_edge(env_calibration, seed_selection)
root.order.add_edge(seed_selection,  nutrient_prep)
root.order.add_edge(nutrient_prep,   automated_plant)

root.order.add_edge(automated_plant, cont_loop)

root.order.add_edge(cont_loop,       waste_recycle)
root.order.add_edge(waste_recycle,   data_analyze)
root.order.add_edge(data_analyze,    yield_optimize)
root.order.add_edge(yield_optimize,  community_engage)

root.order.add_edge(community_engage, maint_loop)