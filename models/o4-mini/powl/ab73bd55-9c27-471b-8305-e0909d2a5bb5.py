# Generated from: ab73bd55-9c27-471b-8305-e0909d2a5bb5.json
# Description: This process manages an adaptive urban farming cycle designed to optimize crop yield in confined city environments by integrating real-time environmental monitoring, automated resource allocation, and dynamic crop rotation. The system begins with site assessment, followed by microclimate analysis and soil testing. Based on collected data, seed selection and planting schedules are dynamically adjusted. Nutrient delivery and irrigation are continuously monitored through IoT sensors, with AI-driven adjustments to optimize water and fertilizer use. Pest detection employs image recognition for early intervention. Crop growth is tracked via drone surveillance, enabling timely pruning and harvesting. Post-harvest, produce is quality-graded and packaged using automated sorting systems. Waste is minimized through composting and recycling of organic matter. Finally, feedback from sales trends and consumer preferences informs the next planting cycle, creating a sustainable loop tailored to urban demands and environmental constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_assess    = Transition(label='Site Assess')
climate_scan   = Transition(label='Climate Scan')
soil_test      = Transition(label='Soil Test')
seed_select    = Transition(label='Seed Select')
plant_schedule = Transition(label='Plant Schedule')
irrigation_set = Transition(label='Irrigation Set')
nutrient_feed  = Transition(label='Nutrient Feed')
pest_detect    = Transition(label='Pest Detect')
drone_scan     = Transition(label='Drone Scan')
growth_track   = Transition(label='Growth Track')
prune_crop     = Transition(label='Prune Crop')
harvest_crop   = Transition(label='Harvest Crop')
quality_grade  = Transition(label='Quality Grade')
auto_package   = Transition(label='Auto Package')
waste_manage   = Transition(label='Waste Manage')
sales_review   = Transition(label='Sales Review')
cycle_adjust   = Transition(label='Cycle Adjust')

# Build the main cycle body A: from seed selection through sales review
A = StrictPartialOrder(nodes=[
    seed_select,
    plant_schedule,
    irrigation_set,
    nutrient_feed,
    pest_detect,
    drone_scan,
    growth_track,
    prune_crop,
    harvest_crop,
    quality_grade,
    auto_package,
    waste_manage,
    sales_review
])
# Sequential dependencies in A
A.order.add_edge(seed_select,    plant_schedule)
A.order.add_edge(plant_schedule, irrigation_set)
A.order.add_edge(irrigation_set, nutrient_feed)
A.order.add_edge(nutrient_feed,  pest_detect)
A.order.add_edge(pest_detect,    drone_scan)
A.order.add_edge(drone_scan,     growth_track)
A.order.add_edge(growth_track,   prune_crop)
A.order.add_edge(prune_crop,     harvest_crop)
A.order.add_edge(harvest_crop,   quality_grade)
A.order.add_edge(quality_grade,  auto_package)
A.order.add_edge(auto_package,   waste_manage)
A.order.add_edge(waste_manage,   sales_review)

# Build the LOOP operator: execute A, then either exit or do cycle_adjust then A again
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A, cycle_adjust]
)

# Build the overall process: initial assessment, then enter the adaptive cycle
root = StrictPartialOrder(nodes=[
    site_assess,
    climate_scan,
    soil_test,
    loop
])
# Sequential dependencies before the loop
root.order.add_edge(site_assess,  climate_scan)
root.order.add_edge(climate_scan, soil_test)
root.order.add_edge(soil_test,    loop)