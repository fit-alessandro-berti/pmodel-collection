# Generated from: 6f2d6f28-7c12-40f5-b816-94283f969594.json
# Description: This process details the comprehensive operational cycle of an urban vertical farm specializing in microgreens and exotic herbs. It includes site preparation with modular hydroponic systems, nutrient solution formulation, seed sourcing from rare cultivars, and continuous environmental monitoring using AI sensors. The process also covers adaptive lighting schedules, pest bio-control deployment, automated harvesting, quality grading, packaging with sustainable materials, and logistics coordination for same-day delivery to local restaurants. Additionally, customer feedback loops are integrated to refine crop varieties and improve yield predictions, ensuring a resilient and innovative urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_prep = Transition(label='Site Prep')
system_setup = Transition(label='System Setup')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_mix = Transition(label='Nutrient Mix')
ai_monitoring = Transition(label='AI Monitoring')
light_adjust = Transition(label='Light Adjust')
pest_control = Transition(label='Pest Control')
growth_tracking = Transition(label='Growth Tracking')
harvesting = Transition(label='Harvesting')
quality_check = Transition(label='Quality Check')
packing = Transition(label='Packing')
labeling = Transition(label='Labeling')
order_dispatch = Transition(label='Order Dispatch')

feedback_loop = Transition(label='Feedback Loop')
yield_analysis = Transition(label='Yield Analysis')
variety_update = Transition(label='Variety Update')

# Main farming cycle (A)
A = StrictPartialOrder(nodes=[
    site_prep, system_setup, seed_sourcing, nutrient_mix,
    ai_monitoring, light_adjust, pest_control, growth_tracking,
    harvesting, quality_check, packing, labeling, order_dispatch
])
A.order.add_edge(site_prep, system_setup)
A.order.add_edge(system_setup, seed_sourcing)
A.order.add_edge(seed_sourcing, nutrient_mix)
A.order.add_edge(nutrient_mix, ai_monitoring)
A.order.add_edge(ai_monitoring, light_adjust)
A.order.add_edge(light_adjust, pest_control)
A.order.add_edge(pest_control, growth_tracking)
A.order.add_edge(growth_tracking, harvesting)
A.order.add_edge(harvesting, quality_check)
A.order.add_edge(quality_check, packing)
A.order.add_edge(packing, labeling)
A.order.add_edge(labeling, order_dispatch)

# Feedback/update cycle (B)
B = StrictPartialOrder(nodes=[feedback_loop, yield_analysis, variety_update])
B.order.add_edge(feedback_loop, yield_analysis)
B.order.add_edge(yield_analysis, variety_update)

# Loop: execute A, then optionally B and repeat A, until exit
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])