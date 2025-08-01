# Generated from: 25797ad5-e936-48b5-ae1f-d6d8bc318bcd.json
# Description: This process outlines the comprehensive cycle for managing an urban vertical farm, integrating advanced hydroponic techniques with IoT monitoring and AI-driven crop optimization. It begins with seed selection based on market trends, followed by environment calibration and nutrient balancing. Continuous monitoring of plant health through sensor data informs dynamic adjustments in lighting and humidity. Periodic pest detection triggers targeted bio-control interventions. Harvesting is scheduled according to real-time growth analytics, and post-harvest processing includes automated sorting and packaging. Waste is minimized via composting and resource recycling, ensuring sustainability. The entire cycle is documented for traceability and compliance with urban agriculture regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
trend_analyze    = Transition(label='Trend Analyze')
seed_select      = Transition(label='Seed Select')
env_calibrate    = Transition(label='Env Calibrate')
nutrient_mix     = Transition(label='Nutrient Mix')
plant_setup      = Transition(label='Plant Setup')
sensor_deploy    = Transition(label='Sensor Deploy')
health_monitor   = Transition(label='Health Monitor')
light_adjust     = Transition(label='Light Adjust')
humidity_control = Transition(label='Humidity Control')
pest_detect      = Transition(label='Pest Detect')
bio_control      = Transition(label='Bio-Control')
growth_track     = Transition(label='Growth Track')
harvest_plan     = Transition(label='Harvest Plan')
auto_sort        = Transition(label='Auto Sort')
package_prep     = Transition(label='Package Prep')
waste_compost    = Transition(label='Waste Compost')
resource_recycle = Transition(label='Resource Recycle')
compliance_check = Transition(label='Compliance Check')
trace_document   = Transition(label='Trace Document')

# A: market trend analysis and seed selection
A = StrictPartialOrder(nodes=[trend_analyze, seed_select])
A.order.add_edge(trend_analyze, seed_select)

# B: the rest of the cycle
B = StrictPartialOrder(nodes=[
    env_calibrate, nutrient_mix, plant_setup, sensor_deploy,
    health_monitor, light_adjust, humidity_control,
    pest_detect, bio_control, growth_track,
    harvest_plan, auto_sort, package_prep,
    waste_compost, resource_recycle,
    compliance_check, trace_document
])
# Sequential flows
B.order.add_edge(env_calibrate,    nutrient_mix)
B.order.add_edge(nutrient_mix,     plant_setup)
B.order.add_edge(plant_setup,      sensor_deploy)
B.order.add_edge(sensor_deploy,    health_monitor)
# Concurrent adjustment
B.order.add_edge(health_monitor,   light_adjust)
B.order.add_edge(health_monitor,   humidity_control)
# Pest detection after adjustments
B.order.add_edge(light_adjust,     pest_detect)
B.order.add_edge(humidity_control, pest_detect)
# Bio-control and tracking
B.order.add_edge(pest_detect,      bio_control)
B.order.add_edge(bio_control,      growth_track)
B.order.add_edge(growth_track,     harvest_plan)
B.order.add_edge(harvest_plan,     auto_sort)
B.order.add_edge(auto_sort,        package_prep)
# Waste management
B.order.add_edge(package_prep,     waste_compost)
B.order.add_edge(package_prep,     resource_recycle)
# Compliance and traceability
B.order.add_edge(waste_compost,    compliance_check)
B.order.add_edge(resource_recycle, compliance_check)
B.order.add_edge(compliance_check, trace_document)

# Loop the cycle: (Trend Analyze -> Seed Select), then optionally do B then repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])