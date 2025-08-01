# Generated from: d548a8db-83e4-4782-9a32-ea910e84897e.json
# Description: This process outlines the operational cycle of an urban vertical farm integrating automated hydroponics, AI-driven crop monitoring, and community-supported distribution. Beginning with seed selection and nutrient calibration, the farm conducts continuous environmental adjustments to optimize growth. Automated harvesting robots coordinate with quality control sensors to ensure produce meets strict urban agricultural standards. Waste recycling and energy reuse loops minimize environmental impact. Finally, a dynamic delivery system synchronizes with local demand patterns to distribute fresh crops efficiently while engaging community members through participatory farming events and educational workshops.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Setup = Transition(label='Nutrient Setup')
Growth_Monitoring = Transition(label='Growth Monitoring')
Climate_Adjust = Transition(label='Climate Adjust')
Pest_Control = Transition(label='Pest Control')
Water_Recirculate = Transition(label='Water Recirculate')
Light_Calibration = Transition(label='Light Calibration')
Robotic_Harvest = Transition(label='Robotic Harvest')
Quality_Inspect = Transition(label='Quality Inspect')
Waste_Process = Transition(label='Waste Process')
Energy_Reuse = Transition(label='Energy Reuse')
Inventory_Update = Transition(label='Inventory Update')
Demand_Forecast = Transition(label='Demand Forecast')
Order_Dispatch = Transition(label='Order Dispatch')
Community_Event = Transition(label='Community Event')
Feedback_Collect = Transition(label='Feedback Collect')
Data_Analyze = Transition(label='Data Analyze')

# Initial partial order: Seed Selection --> Nutrient Setup
init_po = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Setup])
init_po.order.add_edge(Seed_Selection, Nutrient_Setup)

# Growth environment adjustment partial order with loop to simulate continuous adjustment:
# Loop node: A = Growth Monitoring and adjustments, B = other adjustments
# We'll define the loop as: first execute A = Growth_Monitoring
# then choose to exit or execute B = concurrent Climate_Adjust, Pest_Control, Water_Recirculate, Light_Calibration
# then execute A again, repeated until exit
# For B part, we will represent concurrency by PO with empty order

# concurrency: Climate_Adjust, Pest_Control, Water_Recirculate, Light_Calibration
env_adjust = StrictPartialOrder(nodes=[Climate_Adjust, Pest_Control, Water_Recirculate, Light_Calibration])

# Loop over Growth_Monitoring and env_adjust
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitoring, env_adjust])

# Harvesting and quality control partial order
harvest_qc_po = StrictPartialOrder(
    nodes=[Robotic_Harvest, Quality_Inspect]
)
harvest_qc_po.order.add_edge(Robotic_Harvest, Quality_Inspect)

# Waste recycling and energy reuse loop
waste_energy_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Waste_Process,
        Energy_Reuse
    ]
)

# Dynamic delivery system: Demand Forecast --> Order Dispatch
delivery_po = StrictPartialOrder(nodes=[Demand_Forecast, Order_Dispatch])
delivery_po.order.add_edge(Demand_Forecast, Order_Dispatch)

# Community engagement partial order: Community Event --> Feedback Collect
community_po = StrictPartialOrder(nodes=[Community_Event, Feedback_Collect])
community_po.order.add_edge(Community_Event, Feedback_Collect)

# Data analyze activity stands alone but we will synchronize it after harvest_qc_po
# Inventory Update comes after Waste_Process and Energy_Reuse (after loop finishes)
# We connect Inventory_Update after waste_energy_loop
# Then Data Analyze after Inventory_Update and Feedback Collect (coming from community engagement)
# We will combine community engagement and delivery system concurrently
# These two together after inventory update and harvest_qc_po

# Combine community engagement and delivery system concurrently
community_and_delivery = StrictPartialOrder(
    nodes=[community_po, delivery_po]
)

# No edges between community_po and delivery_po, so concurrent.

# Finally, create the root partial order including:
# init_po --> growth_loop
# growth_loop --> harvest_qc_po
# harvest_qc_po --> waste_energy_loop
# waste_energy_loop --> Inventory_Update
# Inventory_Update --> community_and_delivery
# community_po --> Feedback_Collect
# Feedback_Collect and Inventory_Update --> Data_Analyze

root = StrictPartialOrder(
    nodes=[
        init_po,
        growth_loop,
        harvest_qc_po,
        waste_energy_loop,
        Inventory_Update,
        community_and_delivery,
        Data_Analyze
    ]
)

# Define edges between these composite nodes:
root.order.add_edge(init_po, growth_loop)
root.order.add_edge(growth_loop, harvest_qc_po)
root.order.add_edge(harvest_qc_po, waste_energy_loop)
root.order.add_edge(waste_energy_loop, Inventory_Update)
root.order.add_edge(Inventory_Update, community_and_delivery)

# Feedback Collect is inside community_po inside community_and_delivery
# Add edges from Inventory_Update and Feedback_Collect to Data Analyze
# We cannot directly add edge from Feedback_Collect as it's nested,
# so we add edge from community_and_delivery to Data_Analyze to represent synchronization after both paths.

root.order.add_edge(community_and_delivery, Data_Analyze)
root.order.add_edge(Inventory_Update, Data_Analyze)