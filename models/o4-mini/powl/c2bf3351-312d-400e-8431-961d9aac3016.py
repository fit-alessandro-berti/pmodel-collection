# Generated from: c2bf3351-312d-400e-8431-961d9aac3016.json
# Description: This process describes the adaptive urban farming cycle designed to optimize limited space agriculture through dynamic resource allocation, environmental monitoring, and community engagement. It begins with site analysis to assess microclimate and soil conditions, followed by modular bed setup. Sensors gather real-time data on moisture, light, and air quality, which feeds into an AI-driven irrigation and nutrient delivery system. Concurrently, crop selection adapts seasonally based on predictive analytics and community dietary needs. Pest control leverages integrated biological methods, minimizing chemical use. Harvesting is coordinated with local markets and direct consumer feedback to adjust future planting schedules. Continuous education workshops foster urban farmer skills, and waste composting closes the loop, ensuring sustainable nutrient cycling. This cyclical approach promotes resilience, efficiency, and social integration within urban agriculture systems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis     = Transition(label='Site Analysis')
bed_setup         = Transition(label='Bed Setup')
sensor_install    = Transition(label='Sensor Install')
data_capture      = Transition(label='Data Capture')
irrigation_adjust = Transition(label='Irrigation Adjust')
nutrient_supply   = Transition(label='Nutrient Supply')
crop_select       = Transition(label='Crop Select')
pest_monitor      = Transition(label='Pest Monitor')
biocontrol_deploy = Transition(label='Biocontrol Deploy')
harvest_plan      = Transition(label='Harvest Plan')
market_sync       = Transition(label='Market Sync')
feedback_gather   = Transition(label='Feedback Gather')
workshop_host     = Transition(label='Workshop Host')
waste_compost     = Transition(label='Waste Compost')
cycle_review      = Transition(label='Cycle Review')
schedule_update   = Transition(label='Schedule Update')

# Build the loop body (B)
B = StrictPartialOrder(nodes=[
    irrigation_adjust, nutrient_supply,
    crop_select,
    pest_monitor, biocontrol_deploy,
    harvest_plan,
    market_sync, feedback_gather,
    workshop_host, waste_compost,
    cycle_review, schedule_update
])

# pest_monitor -> biocontrol_deploy
B.order.add_edge(pest_monitor, biocontrol_deploy)
# after pest control and crop select, harvest plan
B.order.add_edge(crop_select, harvest_plan)
B.order.add_edge(biocontrol_deploy, harvest_plan)
# harvest plan -> market sync -> feedback gather
B.order.add_edge(harvest_plan, market_sync)
B.order.add_edge(market_sync, feedback_gather)
# after feedback, workshops and compost
B.order.add_edge(feedback_gather, workshop_host)
B.order.add_edge(feedback_gather, waste_compost)
# workshops & compost -> cycle review -> schedule update
B.order.add_edge(workshop_host, cycle_review)
B.order.add_edge(waste_compost, cycle_review)
B.order.add_edge(cycle_review, schedule_update)

# Define the LOOP operator: first execute data_capture (A), then repeatedly B then A
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, B])

# Build the root partial order: site analysis -> bed setup -> sensor install -> loop
root = StrictPartialOrder(nodes=[
    site_analysis, bed_setup, sensor_install, loop
])
root.order.add_edge(site_analysis, bed_setup)
root.order.add_edge(bed_setup, sensor_install)
root.order.add_edge(sensor_install, loop)