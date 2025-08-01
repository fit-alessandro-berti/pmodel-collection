# Generated from: 48ff974a-794d-4e58-bb9c-418ea513c583.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm specializing in leafy greens and herbs. It begins with seed selection and preparation, followed by nutrient solution formulation and environmental calibration within stacked hydroponic layers. Continuous monitoring of plant health and growth metrics is conducted using IoT sensors and AI-driven analytics. Periodic pruning and pest control are integrated seamlessly to maintain optimal yield. Harvesting involves automated robotic arms to minimize damage, while post-harvest handling includes quality grading, packaging, and cold chain logistics. The process concludes with waste recycling and data feedback loops to improve subsequent cycles, ensuring sustainability and efficiency in an urban agriculture context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
seed_prep = Transition(label='Seed Prep')
nutrient_mix = Transition(label='Nutrient Mix')
env_calibration = Transition(label='Env Calibration')
planting_setup = Transition(label='Planting Setup')
growth_monitor = Transition(label='Growth Monitor')
health_check = Transition(label='Health Check')
pest_control = Transition(label='Pest Control')
pruning_task = Transition(label='Pruning Task')
automated_harvest = Transition(label='Automated Harvest')
quality_grade = Transition(label='Quality Grade')
packaging_line = Transition(label='Packaging Line')
cold_storage = Transition(label='Cold Storage')
waste_recycle = Transition(label='Waste Recycle')
data_analysis = Transition(label='Data Analysis')
cycle_review = Transition(label='Cycle Review')

# Inner loop: continuous monitoring followed by periodic control
monitor_PO = StrictPartialOrder(nodes=[growth_monitor, health_check])
# growth_monitor and health_check are concurrent

control_PO = StrictPartialOrder(nodes=[pest_control, pruning_task])
# pest_control and pruning_task are concurrent

inner_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_PO, control_PO])

# Main body of one production cycle
body_nodes = [
    seed_prep,
    nutrient_mix,
    env_calibration,
    planting_setup,
    inner_loop,
    automated_harvest,
    quality_grade,
    packaging_line,
    cold_storage,
    waste_recycle
]
body_PO = StrictPartialOrder(nodes=body_nodes)
body_PO.order.add_edge(seed_prep, nutrient_mix)
body_PO.order.add_edge(nutrient_mix, env_calibration)
body_PO.order.add_edge(env_calibration, planting_setup)
body_PO.order.add_edge(planting_setup, inner_loop)
body_PO.order.add_edge(inner_loop, automated_harvest)
body_PO.order.add_edge(automated_harvest, quality_grade)
body_PO.order.add_edge(quality_grade, packaging_line)
body_PO.order.add_edge(packaging_line, cold_storage)
body_PO.order.add_edge(cold_storage, waste_recycle)

# Review & feedback after each cycle
review_PO = StrictPartialOrder(nodes=[data_analysis, cycle_review])
review_PO.order.add_edge(data_analysis, cycle_review)

# Outer loop: repeat entire cycle with feedback
root = OperatorPOWL(operator=Operator.LOOP, children=[body_PO, review_PO])