# Generated from: c71b3cb4-9d94-49f6-9d58-711947707bce.json
# Description: This process describes the comprehensive operational cycle of an urban vertical farm integrating hydroponic cultivation, automated nutrient delivery, and AI-driven climate control. It begins with seed selection and germination, followed by transplanting seedlings into multilayered vertical racks. Automated systems monitor and adjust water, nutrients, and light exposure based on real-time sensor data. Periodic health assessments detect pest or disease outbreaks, triggering targeted organic interventions. Harvesting is scheduled dynamically to optimize freshness and supply chain demands. Post-harvest, the system manages waste recycling and biomass conversion, feeding energy back into the farm's power grid. Data collected throughout the cycle informs predictive analytics for yield optimization and resource efficiency, ensuring sustainable urban agriculture with minimal environmental footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Germination_Start = Transition(label='Germination Start')
Seedling_Transplant = Transition(label='Seedling Transplant')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Delivery = Transition(label='Water Delivery')
Light_Adjustment = Transition(label='Light Adjustment')
Climate_Control = Transition(label='Climate Control')
Sensor_Monitoring = Transition(label='Sensor Monitoring')
Health_Check = Transition(label='Health Check')
Pest_Control = Transition(label='Pest Control')
Harvest_Planning = Transition(label='Harvest Planning')
Crop_Harvest = Transition(label='Crop Harvest')
Waste_Sorting = Transition(label='Waste Sorting')
Biomass_Process = Transition(label='Biomass Process')
Energy_Recycling = Transition(label='Energy Recycling')
Data_Analysis = Transition(label='Data Analysis')
Yield_Forecast = Transition(label='Yield Forecast')

# Loop for continuous monitoring and adjustments triggered by sensor data
# After Sensor Monitoring, execute in loop:
# Nutritient Mix, Water Delivery, Light Adjustment, Climate Control (can be partially ordered/concurrent)
# Then Health Check, if pest/disease detected then Pest Control
# Loop repeats to monitor and adjust continuously

# Actually build monitoring adjustment partial order
adjustments = StrictPartialOrder(nodes=[Nutrient_Mix, Water_Delivery, Light_Adjustment, Climate_Control])
# no order edges means these are concurrent

# Pest control choice: either Pest Control happens or skip it (tau)
from pm4py.objects.powl.obj import SilentTransition
skip = SilentTransition()

pest_choice = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, skip])

# Loop body after Sensor Monitoring: adjustments, then Health Check then pest_choice
inside_loop = StrictPartialOrder(
    nodes=[adjustments, Health_Check, pest_choice]
)
inside_loop.order.add_edge(adjustments, Health_Check)
inside_loop.order.add_edge(Health_Check, pest_choice)

# Loop structure: A=Sensor Monitoring, B=inside_loop
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Sensor_Monitoring, inside_loop])

# After monitoring loop, harvest scheduled then harvest
harvest = StrictPartialOrder(nodes=[Harvest_Planning, Crop_Harvest])
harvest.order.add_edge(Harvest_Planning, Crop_Harvest)

# Post-harvest process: waste sorting -> biomass processing -> energy recycling
post_harvest = StrictPartialOrder(nodes=[Waste_Sorting, Biomass_Process, Energy_Recycling])
post_harvest.order.add_edge(Waste_Sorting, Biomass_Process)
post_harvest.order.add_edge(Biomass_Process, Energy_Recycling)

# Data analysis and yield forecast concurrent to post-harvest (usually continuous processes)
data_processes = StrictPartialOrder(nodes=[Data_Analysis, Yield_Forecast])
# no order edges = concurrent

# Initial growth phases: Seed Selection -> Germination Start -> Seedling Transplant
initial_growth = StrictPartialOrder(nodes=[Seed_Selection, Germination_Start, Seedling_Transplant])
initial_growth.order.add_edge(Seed_Selection, Germination_Start)
initial_growth.order.add_edge(Germination_Start, Seedling_Transplant)

# Assemble full workflow partial order:
# initial_growth -> monitor_loop -> harvest -> (post_harvest || data_processes concurrent)

root = StrictPartialOrder(
    nodes=[initial_growth, monitor_loop, harvest, post_harvest, data_processes]
)

root.order.add_edge(initial_growth, monitor_loop)
root.order.add_edge(monitor_loop, harvest)
root.order.add_edge(harvest, post_harvest)
root.order.add_edge(harvest, data_processes)