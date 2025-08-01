# Generated from: c1cdf878-4398-451b-b236-c6f11a2a51d3.json
# Description: This process outlines the complex operational cycle of an urban vertical farm integrating IoT sensor data, AI-driven climate control, and automated harvesting robots. It begins with seed selection optimized by genetic algorithms, followed by nutrient solution formulation tailored per crop type. Environmental sensors continuously feed data to AI modules that adjust lighting, humidity, and airflow in real-time. Periodic pest detection triggers targeted biocontrol deployment. Harvesting robots identify mature crops via computer vision, ensuring selective picking without damaging plants. Post-harvest, produce undergoes automated quality grading and packaging. Waste biomass is recycled into organic compost through an on-site bio-reactor. Finally, logistics coordination ensures timely delivery to local markets and restaurants, optimizing freshness and reducing carbon footprint. This atypical process demands seamless integration of advanced technologies and sustainable practices to maximize yield within constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
seed_select        = Transition(label='Seed Select')
genetic_optimize   = Transition(label='Genetic Optimize')
nutrient_mix       = Transition(label='Nutrient Mix')
sensor_deploy      = Transition(label='Sensor Deploy')
data_monitor       = Transition(label='Data Monitor')
climate_adjust     = Transition(label='Climate Adjust')
pest_detect        = Transition(label='Pest Detect')
biocontrol_release = Transition(label='Biocontrol Release')
growth_analyze     = Transition(label='Growth Analyze')
harvest_identify   = Transition(label='Harvest Identify')
crop_pick          = Transition(label='Crop Pick')
quality_grade      = Transition(label='Quality Grade')
pack_produce       = Transition(label='Pack Produce')
waste_process      = Transition(label='Waste Process')
compost_cycle      = Transition(label='Compost Cycle')
logistics_plan     = Transition(label='Logistics Plan')
delivery_schedule  = Transition(label='Delivery Schedule')

# Silent transition for loop exits
skip = SilentTransition()

# Environment-control loop: continuously monitor data and adjust climate
env_body = StrictPartialOrder(nodes=[data_monitor, climate_adjust])
env_body.order.add_edge(data_monitor, climate_adjust)
env_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_body, skip])

# Pest-detection loop: detect pests and release biocontrol agents as needed
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_detect, biocontrol_release])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    seed_select,
    genetic_optimize,
    nutrient_mix,
    sensor_deploy,
    env_loop,
    pest_loop,
    growth_analyze,
    harvest_identify,
    crop_pick,
    quality_grade,
    pack_produce,
    waste_process,
    compost_cycle,
    logistics_plan,
    delivery_schedule
])

# Define the overall execution sequence
root.order.add_edge(seed_select,        genetic_optimize)
root.order.add_edge(genetic_optimize,   nutrient_mix)
root.order.add_edge(nutrient_mix,       sensor_deploy)
root.order.add_edge(sensor_deploy,      env_loop)
root.order.add_edge(env_loop,           pest_loop)
root.order.add_edge(pest_loop,          growth_analyze)
root.order.add_edge(growth_analyze,     harvest_identify)
root.order.add_edge(harvest_identify,   crop_pick)
root.order.add_edge(crop_pick,          quality_grade)
root.order.add_edge(quality_grade,      pack_produce)
root.order.add_edge(pack_produce,       waste_process)
root.order.add_edge(waste_process,      compost_cycle)
root.order.add_edge(compost_cycle,      logistics_plan)
root.order.add_edge(logistics_plan,     delivery_schedule)