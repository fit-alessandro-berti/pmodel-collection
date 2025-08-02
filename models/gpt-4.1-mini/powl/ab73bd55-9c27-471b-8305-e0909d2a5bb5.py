# Generated from: ab73bd55-9c27-471b-8305-e0909d2a5bb5.json
# Description: This process manages an adaptive urban farming cycle designed to optimize crop yield in confined city environments by integrating real-time environmental monitoring, automated resource allocation, and dynamic crop rotation. The system begins with site assessment, followed by microclimate analysis and soil testing. Based on collected data, seed selection and planting schedules are dynamically adjusted. Nutrient delivery and irrigation are continuously monitored through IoT sensors, with AI-driven adjustments to optimize water and fertilizer use. Pest detection employs image recognition for early intervention. Crop growth is tracked via drone surveillance, enabling timely pruning and harvesting. Post-harvest, produce is quality-graded and packaged using automated sorting systems. Waste is minimized through composting and recycling of organic matter. Finally, feedback from sales trends and consumer preferences informs the next planting cycle, creating a sustainable loop tailored to urban demands and environmental constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Assess = Transition(label='Site Assess')
Climate_Scan = Transition(label='Climate Scan')
Soil_Test = Transition(label='Soil Test')
Seed_Select = Transition(label='Seed Select')
Plant_Schedule = Transition(label='Plant Schedule')
Irrigation_Set = Transition(label='Irrigation Set')
Nutrient_Feed = Transition(label='Nutrient Feed')
Pest_Detect = Transition(label='Pest Detect')
Drone_Scan = Transition(label='Drone Scan')
Growth_Track = Transition(label='Growth Track')
Prune_Crop = Transition(label='Prune Crop')
Harvest_Crop = Transition(label='Harvest Crop')
Quality_Grade = Transition(label='Quality Grade')
Auto_Package = Transition(label='Auto Package')
Waste_Manage = Transition(label='Waste Manage')
Sales_Review = Transition(label='Sales Review')
Cycle_Adjust = Transition(label='Cycle Adjust')

# Partial order for initial assessment activities done sequentially:
initial_assess = StrictPartialOrder(nodes=[Site_Assess, Climate_Scan, Soil_Test])
initial_assess.order.add_edge(Site_Assess, Climate_Scan)
initial_assess.order.add_edge(Climate_Scan, Soil_Test)

# Partial order for seed selection and planting schedule, modified dynamically
seed_plant = StrictPartialOrder(nodes=[Seed_Select, Plant_Schedule])
seed_plant.order.add_edge(Seed_Select, Plant_Schedule)

# Partial order for irrigation and nutrient feed running in parallel (concurrent)
resources_monitor = StrictPartialOrder(nodes=[Irrigation_Set, Nutrient_Feed])
# No order edges => concurrent

# Pest detection: independent activity
pest_detect = Pest_Detect

# Partial order for crop monitoring: drone scan then growth tracking
crop_monitor = StrictPartialOrder(nodes=[Drone_Scan, Growth_Track])
crop_monitor.order.add_edge(Drone_Scan, Growth_Track)

# Partial order for pruning and harvesting
prune_harvest = StrictPartialOrder(nodes=[Prune_Crop, Harvest_Crop])
prune_harvest.order.add_edge(Prune_Crop, Harvest_Crop)

# Partial order for post-harvest: quality grading, packaging, and waste management concurrently
post_harvest = StrictPartialOrder(nodes=[Quality_Grade, Auto_Package, Waste_Manage])
# No order edges

# Partial order for sales review and cycle adjustment sequentially
sales_cycle = StrictPartialOrder(nodes=[Sales_Review, Cycle_Adjust])
sales_cycle.order.add_edge(Sales_Review, Cycle_Adjust)

# Combine crop monitoring with post-harvest steps to run after prune_harvest
after_harvest = StrictPartialOrder(
    nodes=[crop_monitor, prune_harvest, post_harvest]
)
# prune_harvest before crop_monitor and post_harvest (surveillance precedes packaging)
after_harvest.order.add_edge(prune_harvest, crop_monitor)
after_harvest.order.add_edge(prune_harvest, post_harvest)

# Combine pest detection with crop monitoring/post-harvest concurrently (no edges between pest detect)
pest_and_after = StrictPartialOrder(nodes=[pest_detect, after_harvest])
# No edges => concurrent

# Combine seed & plant with resource monitoring concurrently
seed_resources = StrictPartialOrder(nodes=[seed_plant, resources_monitor])
# No edges => concurrent

# These combined after initial assessments, so initial_assess before seed_resources and pest_and_after
main_flow = StrictPartialOrder(
    nodes=[initial_assess, seed_resources, pest_and_after, sales_cycle]
)
main_flow.order.add_edge(initial_assess, seed_resources)
main_flow.order.add_edge(initial_assess, pest_and_after)
main_flow.order.add_edge(seed_resources, pest_and_after)
main_flow.order.add_edge(pest_and_after, sales_cycle)

# Loop structure: the whole cycle repeats after sales review and cycle adjust
root = OperatorPOWL(operator=Operator.LOOP, children=[main_flow, Cycle_Adjust])