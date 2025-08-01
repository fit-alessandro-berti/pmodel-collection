# Generated from: f8dd5f44-6a28-4928-9a74-73664ee2714e.json
# Description: This process outlines the end-to-end operations of an urban vertical farming supply chain, integrating advanced hydroponics, automated harvesting, and AI-driven demand forecasting. It begins with seed selection and nutrient formulation, followed by controlled environment monitoring and pest detection using IoT sensors. Crops are then harvested via robotic arms, quality-checked by computer vision systems, and packaged in biodegradable containers. Distribution leverages micro-fulfillment centers to enable rapid delivery to local markets while minimizing carbon footprint. Feedback loops from consumer preferences inform adaptive crop planning and resource allocation, ensuring sustainability and profitability in a complex urban agricultural ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Environment_Setup = Transition(label='Environment Setup')
Sensor_Deployment = Transition(label='Sensor Deployment')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Detection = Transition(label='Pest Detection')
Automated_Harvest = Transition(label='Automated Harvest')
Quality_Check = Transition(label='Quality Check')
Packaging_Prep = Transition(label='Packaging Prep')
Biodegradable_Pack = Transition(label='Biodegradable Pack')
Inventory_Sync = Transition(label='Inventory Sync')
Demand_Forecast = Transition(label='Demand Forecast')
Micro_Fulfillment = Transition(label='Micro Fulfillment')
Local_Dispatch = Transition(label='Local Dispatch')
Consumer_Feedback = Transition(label='Consumer Feedback')
Crop_Adjustment = Transition(label='Crop Adjustment')

skip = SilentTransition()

# Loop representing feedback and adjustment: (Consumer Feedback followed by Crop Adjustment) loops, possibility to exit
feedback_loop_body = StrictPartialOrder(
    nodes=[Consumer_Feedback, Crop_Adjustment],
)
feedback_loop_body.order.add_edge(Consumer_Feedback, Crop_Adjustment)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    feedback_loop_body,  # A
    skip               # B (to exit)
])

# Forward supply chain partial order before the loop

# Step 1 & 2: Seed Selection -> Nutrient Mix (sequential)
# Step 3 & 4: Environment Setup -> Sensor Deployment (sequential)
# Steps 5 & 6: Growth Monitoring -> Pest Detection (sequential); both after Sensor Deployment
# Step 7 -> Step 8 (Automated Harvest -> Quality Check -> Packaging Prep -> Biodegradable Pack)
# Packaging Prep -> Biodegradable Pack (sequential)
# Steps 9,10, and distribution steps 11-14

# Prepare partial orders for parallel stages:

# Node group 1: Seed Selection -> Nutrient Mix
sn = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix])
sn.order.add_edge(Seed_Selection, Nutrient_Mix)

# Node group 2: Environment Setup -> Sensor Deployment
es_sd = StrictPartialOrder(nodes=[Environment_Setup, Sensor_Deployment])
es_sd.order.add_edge(Environment_Setup, Sensor_Deployment)

# Node group 3: Growth Monitoring -> Pest Detection
gm_pd = StrictPartialOrder(nodes=[Growth_Monitoring, Pest_Detection])
gm_pd.order.add_edge(Growth_Monitoring, Pest_Detection)

# Combine groups 2 and 3 partially ordered: Sensor Deployment -> Growth Monitoring (GM and Pest Detection after Sensor Deployment)
# So: Sensor Deployment -> Growth Monitoring, pest detection after growth monitoring is already modeled in gm_pd

es_sd_gm_pd = StrictPartialOrder(nodes=[Environment_Setup, Sensor_Deployment, Growth_Monitoring, Pest_Detection])
es_sd_gm_pd.order.add_edge(Environment_Setup, Sensor_Deployment)
es_sd_gm_pd.order.add_edge(Sensor_Deployment, Growth_Monitoring)
es_sd_gm_pd.order.add_edge(Growth_Monitoring, Pest_Detection)

# We want to model that sn and es_sd_gm_pd run concurrently but with no ordering between these groups:
# So these two partial orders combined with nodes merged, but no order between sn and es_sd_gm_pd
# We'll do a PO over all 6 nodes with edges from the above two partial orders but no edges connecting nodes between these two groups.

sn_nodes = [Seed_Selection, Nutrient_Mix]
sn_order = [(Seed_Selection, Nutrient_Mix)]

es_nodes = [Environment_Setup, Sensor_Deployment, Growth_Monitoring, Pest_Detection]
es_order = [
    (Environment_Setup, Sensor_Deployment),
    (Sensor_Deployment, Growth_Monitoring),
    (Growth_Monitoring, Pest_Detection)
]

nodes1 = sn_nodes + es_nodes
po1 = StrictPartialOrder(nodes=nodes1)
for s, t in sn_order + es_order:
    po1.order.add_edge(s, t)


# Harvest and packaging chain: Automated Harvest -> Quality Check -> Packaging Prep -> Biodegradable Pack
harvest_pack_nodes = [Automated_Harvest, Quality_Check, Packaging_Prep, Biodegradable_Pack]
harvest_pack_order = [
    (Automated_Harvest, Quality_Check),
    (Quality_Check, Packaging_Prep),
    (Packaging_Prep, Biodegradable_Pack),
]
po2 = StrictPartialOrder(nodes=harvest_pack_nodes)
for s, t in harvest_pack_order:
    po2.order.add_edge(s, t)

# Distribution chain partial order:
# Inventory Sync -> Demand Forecast -> Micro Fulfillment -> Local Dispatch
distrib_nodes = [Inventory_Sync, Demand_Forecast, Micro_Fulfillment, Local_Dispatch]
distrib_order = [
    (Inventory_Sync, Demand_Forecast),
    (Demand_Forecast, Micro_Fulfillment),
    (Micro_Fulfillment, Local_Dispatch),
]

po3 = StrictPartialOrder(nodes=distrib_nodes)
for s, t in distrib_order:
    po3.order.add_edge(s, t)

# Combine the main supply chain partial order from po1, po2, po3 sequenced as:

# po1 (seed/nutrient and environment/sensor/growth/pest)
# -> Automated Harvest chain (po2)
# -> Distribution chain (po3)
# -> Feedback loop (feedback_loop)

root = StrictPartialOrder(
    nodes=[po1, po2, po3, feedback_loop]
)

# Add ordering edges between these parts:

root.order.add_edge(po1, po2)            # after initial growth/pest detection, harvest/packaging starts
root.order.add_edge(po2, po3)            # after packaging, distribution starts
root.order.add_edge(po3, feedback_loop) # after distribution, feedback loop runs

# Note: Within each PO, internal ordering exists; between them, sequencing is established with these edges.
