# Generated from: d67fb975-debf-49cd-82f1-238deeb66bcb.json
# Description: This process outlines the adaptive urban farming cycle designed to optimize crop yield in limited city spaces by integrating environmental data, community feedback, and resource availability. It begins with site analysis, followed by soil enhancement and precision planting. Sensor arrays continuously monitor microclimate and soil conditions, allowing dynamic irrigation and nutrient delivery adjustments. Community workshops gather experiential insights which feed into iterative crop selection and pest management strategies. Harvesting is coordinated with local distribution networks to minimize waste. Post-harvest, composting converts organic waste into soil amendments, completing the sustainability loop. Throughout, data analytics refine practices seasonally to adapt to urban environmental fluctuations and community needs, ensuring resilient and productive green spaces within dense urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_analyze     = Transition(label="Site Analyze")
soil_enhance     = Transition(label="Soil Enhance")
seed_select      = Transition(label="Seed Select")
plant_precise    = Transition(label="Plant Precise")
sensor_deploy    = Transition(label="Sensor Deploy")
climate_monitor  = Transition(label="Climate Monitor")
irrigate_adjust  = Transition(label="Irrigate Adjust")
nutrient_feed    = Transition(label="Nutrient Feed")
pest_control     = Transition(label="Pest Control")
community_engage = Transition(label="Community Engage")
feedback_collect = Transition(label="Feedback Collect")
yield_harvest    = Transition(label="Yield Harvest")
network_dist     = Transition(label="Network Distribute")
waste_sort       = Transition(label="Waste Sort")
compost_create   = Transition(label="Compost Create")
data_analyze     = Transition(label="Data Analyze")

# Inner loop for iterative crop selection and pest management
loop_crop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[seed_select, pest_control]
)

# Main partial‐order for one cycle (without the seasonal data‐analysis loop)
main_cycle = StrictPartialOrder(
    nodes=[
        site_analyze,
        soil_enhance,
        loop_crop,
        plant_precise,
        sensor_deploy,
        climate_monitor,
        irrigate_adjust,
        nutrient_feed,
        community_engage,
        feedback_collect,
        yield_harvest,
        network_dist,
        waste_sort,
        compost_create
    ]
)

# Define the control‐flow edges
o = main_cycle.order
o.add_edge(site_analyze,     soil_enhance)
o.add_edge(soil_enhance,     loop_crop)
o.add_edge(loop_crop,        plant_precise)
o.add_edge(plant_precise,    sensor_deploy)
o.add_edge(sensor_deploy,    climate_monitor)
o.add_edge(climate_monitor,  irrigate_adjust)
o.add_edge(climate_monitor,  nutrient_feed)
o.add_edge(irrigate_adjust,  community_engage)
o.add_edge(nutrient_feed,    community_engage)
o.add_edge(community_engage, feedback_collect)
o.add_edge(feedback_collect, yield_harvest)
o.add_edge(yield_harvest,    network_dist)
o.add_edge(network_dist,     waste_sort)
o.add_edge(waste_sort,       compost_create)

# Outer loop for seasonal adaptation via data analysis
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_cycle, data_analyze]
)