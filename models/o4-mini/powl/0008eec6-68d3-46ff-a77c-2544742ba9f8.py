# Generated from: 0008eec6-68d3-46ff-a77c-2544742ba9f8.json
# Description: This process outlines the complex and atypical series of activities involved in launching an urban vertical farming operation within a densely populated city. It starts with site analysis, followed by modular system design tailored to space constraints, integration of IoT sensors for environmental control, and optimization of nutrient delivery systems. The process also involves securing permits from multiple municipal authorities, coordinating logistics for equipment transport through narrow urban corridors, and training staff on sustainable farming practices. Continuous monitoring of crop health using AI-driven analytics and adaptive lighting schedules ensures maximum yield. Additionally, the operation includes establishing partnerships with local restaurants and markets to create a direct-to-consumer supply chain, reducing food miles and enhancing freshness. The final stages focus on environmental impact assessments and scalability planning for future urban sites, making this process a unique blend of agriculture, technology, and urban planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey    = Transition(label='Site Survey')
modular_design = Transition(label='Modular Design')
permit_check   = Transition(label='Permit Check')
sensor_setup   = Transition(label='Sensor Setup')
nutrient_mix   = Transition(label='Nutrient Mix')
logistics_plan = Transition(label='Logistics Plan')
staff_training = Transition(label='Staff Training')
crop_seeding   = Transition(label='Crop Seeding')
light_adjust   = Transition(label='Light Adjust')
data_monitor   = Transition(label='Data Monitor')
ai_analytics   = Transition(label='AI Analytics')
yield_review   = Transition(label='Yield Review')
market_link    = Transition(label='Market Link')
impact_study   = Transition(label='Impact Study')
scale_plan     = Transition(label='Scale Plan')

# Define the monitoring cycle (Data Monitor -> AI Analytics -> Yield Review)
monitor_cycle = StrictPartialOrder(nodes=[data_monitor, ai_analytics, yield_review])
monitor_cycle.order.add_edge(data_monitor, ai_analytics)
monitor_cycle.order.add_edge(ai_analytics, yield_review)

# Define the loop of adaptive lighting + monitoring cycle
# LOOP(children=[A, B]) means: do A, then either exit or do B then A again, etc.
lighting_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_adjust, monitor_cycle])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    modular_design,
    sensor_setup,
    nutrient_mix,
    permit_check,
    logistics_plan,
    staff_training,
    crop_seeding,
    lighting_loop,
    market_link,
    impact_study,
    scale_plan
])

# Define the control‐flow edges
root.order.add_edge(site_survey,    modular_design)
root.order.add_edge(modular_design, sensor_setup)
root.order.add_edge(sensor_setup,   nutrient_mix)
root.order.add_edge(nutrient_mix,   permit_check)
root.order.add_edge(permit_check,   logistics_plan)
root.order.add_edge(logistics_plan, staff_training)
root.order.add_edge(staff_training, crop_seeding)
root.order.add_edge(crop_seeding,   lighting_loop)
root.order.add_edge(lighting_loop,  market_link)
root.order.add_edge(market_link,    impact_study)
root.order.add_edge(impact_study,   scale_plan)