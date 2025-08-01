# Generated from: 9fa46578-177c-4e8d-be0e-59258a17ada7.json
# Description: This process details the establishment of an urban rooftop farm in a densely populated city environment, integrating sustainable agriculture practices with modern technology. It begins with site assessment and structural analysis to ensure the rooftop can support the farm's weight. Subsequent steps include soil preparation and installation of hydroponic systems, followed by seed selection tailored to urban climate conditions. The process incorporates smart irrigation setup and renewable energy integration to optimize resource efficiency. Regular crop monitoring and pest management are conducted using IoT sensors and AI diagnostics. Finally, harvested produce undergoes quality checks before distribution to local markets, while continuous feedback is used to improve future crop cycles and sustainability metrics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
soil_prep = Transition(label='Soil Prep')
hydroponics_setup = Transition(label='Hydroponics Setup')
seed_select = Transition(label='Seed Select')
irrigation_install = Transition(label='Irrigation Install')
energy_integrate = Transition(label='Energy Integrate')

sensor_deploy = Transition(label='Sensor Deploy')
ai_diagnostics = Transition(label='AI Diagnostics')
crop_monitor = Transition(label='Crop Monitor')
pest_control = Transition(label='Pest Control')

harvest_collect = Transition(label='Harvest Collect')
quality_check = Transition(label='Quality Check')
market_deliver = Transition(label='Market Deliver')
feedback_review = Transition(label='Feedback Review')

# Loop for continuous monitoring and pest management
loop_body = StrictPartialOrder(nodes=[ai_diagnostics, crop_monitor, pest_control])
loop_body.order.add_edge(ai_diagnostics, crop_monitor)
loop_body.order.add_edge(crop_monitor, pest_control)

monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, loop_body])

# Root partial order
root = StrictPartialOrder(nodes=[
    site_assess, structure_check, soil_prep, hydroponics_setup, seed_select,
    irrigation_install, energy_integrate, monitor_loop,
    harvest_collect, quality_check, market_deliver, feedback_review
])

# Define the workflow order
root.order.add_edge(site_assess, structure_check)
root.order.add_edge(structure_check, soil_prep)
root.order.add_edge(soil_prep, hydroponics_setup)
root.order.add_edge(hydroponics_setup, seed_select)
root.order.add_edge(seed_select, irrigation_install)
root.order.add_edge(irrigation_install, energy_integrate)
root.order.add_edge(energy_integrate, monitor_loop)
root.order.add_edge(monitor_loop, harvest_collect)
root.order.add_edge(harvest_collect, quality_check)
root.order.add_edge(quality_check, market_deliver)
root.order.add_edge(market_deliver, feedback_review)