# Generated from: aeb887cb-ac65-4a15-8315-2da5f2b955e2.json
# Description: This process involves establishing an urban vertical farm within a repurposed city warehouse. It starts with site evaluation and structural assessment, followed by climate control system design. Next, hydroponic system installation occurs alongside LED lighting setup. Seed selection and germination testing are performed to ensure optimal crop yield. Nutrient solution formulation and automated delivery configuration are conducted. Continuous environmental monitoring and pest management protocols are established. Harvest scheduling and post-harvest processing are integrated, followed by packaging design tailored for urban retail. Finally, logistics planning ensures timely distribution to local markets while maintaining product freshness. The process requires cross-disciplinary coordination between agronomists, engineers, and supply chain experts to optimize productivity in a confined urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Eval = Transition(label='Site Eval')
Structure_Check = Transition(label='Structure Check')
Climate_Plan = Transition(label='Climate Plan')
Hydroponic_Fit = Transition(label='Hydroponic Fit')
LED_Setup = Transition(label='LED Setup')
Seed_Test = Transition(label='Seed Test')
Nutrient_Mix = Transition(label='Nutrient Mix')
Delivery_Setup = Transition(label='Delivery Setup')
Env_Monitoring = Transition(label='Env Monitoring')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Post_Harvest = Transition(label='Post-Harvest')
Package_Design = Transition(label='Package Design')
Logistics_Map = Transition(label='Logistics Map')
Market_Sync = Transition(label='Market Sync')

# Partial order nodes list
nodes = [
    Site_Eval, Structure_Check, Climate_Plan,
    Hydroponic_Fit, LED_Setup,
    Seed_Test,
    Nutrient_Mix, Delivery_Setup,
    Env_Monitoring, Pest_Control,
    Harvest_Plan, Post_Harvest,
    Package_Design,
    Logistics_Map, Market_Sync
]

root = StrictPartialOrder(nodes=nodes)

# Add ordering edges according to the description:

# Start: Site Eval --> Structure Check --> Climate Plan
root.order.add_edge(Site_Eval, Structure_Check)
root.order.add_edge(Structure_Check, Climate_Plan)

# Hydroponic Fit and LED Setup are concurrent after Climate Plan
# So Climate Plan must precede them
root.order.add_edge(Climate_Plan, Hydroponic_Fit)
root.order.add_edge(Climate_Plan, LED_Setup)

# Seed Test occurs after Hydroponic Fit and LED Setup, so they both precede Seed Test
root.order.add_edge(Hydroponic_Fit, Seed_Test)
root.order.add_edge(LED_Setup, Seed_Test)

# Nutrient Mix and Delivery Setup occur next, both after Seed Test
root.order.add_edge(Seed_Test, Nutrient_Mix)
root.order.add_edge(Seed_Test, Delivery_Setup)

# Env Monitoring and Pest Control protocols established concurrently after Nutrient Mix and Delivery Setup
root.order.add_edge(Nutrient_Mix, Env_Monitoring)
root.order.add_edge(Nutrient_Mix, Pest_Control)
root.order.add_edge(Delivery_Setup, Env_Monitoring)
root.order.add_edge(Delivery_Setup, Pest_Control)

# Harvest Plan and Post-Harvest integrated after Env Monitoring and Pest Control
root.order.add_edge(Env_Monitoring, Harvest_Plan)
root.order.add_edge(Env_Monitoring, Post_Harvest)
root.order.add_edge(Pest_Control, Harvest_Plan)
root.order.add_edge(Pest_Control, Post_Harvest)

# Package Design tailored for urban retail after Harvest Plan and Post-Harvest
root.order.add_edge(Harvest_Plan, Package_Design)
root.order.add_edge(Post_Harvest, Package_Design)

# Logistics Map after Package Design
root.order.add_edge(Package_Design, Logistics_Map)

# Market Sync after Logistics Map
root.order.add_edge(Logistics_Map, Market_Sync)