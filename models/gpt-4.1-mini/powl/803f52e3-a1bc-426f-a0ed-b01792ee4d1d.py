# Generated from: 803f52e3-a1bc-426f-a0ed-b01792ee4d1d.json
# Description: This process describes the comprehensive operational cycle of an urban vertical farm integrating IoT sensors, AI-driven crop monitoring, and automated nutrient delivery. It begins with environmental calibration and seed selection, followed by germination, growth monitoring, and adaptive lighting control. Concurrently, water recycling and pest detection systems operate to maintain optimal conditions. Harvesting is coordinated with supply chain logistics for immediate distribution to local markets. Post-harvest, waste composting and data analysis optimize future cycles, ensuring sustainability and efficient resource use within constrained urban spaces. The process intricately balances technology, biology, and logistics to maximize yield and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
env_setup = Transition(label='Env Setup')
seed_select = Transition(label='Seed Select')
seed_plant = Transition(label='Seed Plant')
germinate = Transition(label='Germinate')
monitor_growth = Transition(label='Monitor Growth')
adjust_light = Transition(label='Adjust Light')
nutrient_feed = Transition(label='Nutrient Feed')
water_recycle = Transition(label='Water Recycle')
pest_scan = Transition(label='Pest Scan')
harvest_crop = Transition(label='Harvest Crop')
pack_produce = Transition(label='Pack Produce')
dispatch_goods = Transition(label='Dispatch Goods')
waste_compost = Transition(label='Waste Compost')
data_analyze = Transition(label='Data Analyze')
cycle_review = Transition(label='Cycle Review')

# Loop body: Nutrient Feed then Monitor Growth - repeated adaptations
# Adapted the loop to Nutrient Feed (B), Monitor Growth (A)
loop_adaptation = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, nutrient_feed])

# Growth phase partial order includes germination then looped growth monitoring & nutrient feeding and adjustment of lighting
growth_phase = StrictPartialOrder(nodes=[germinate, adjust_light, loop_adaptation])
growth_phase.order.add_edge(germinate, loop_adaptation)
growth_phase.order.add_edge(loop_adaptation, adjust_light)

# Initial setup partial order: Env Setup -> Seed Select -> Seed Plant -> Growth phase
initial_setup = StrictPartialOrder(nodes=[env_setup, seed_select, seed_plant, growth_phase])
initial_setup.order.add_edge(env_setup, seed_select)
initial_setup.order.add_edge(seed_select, seed_plant)
initial_setup.order.add_edge(seed_plant, growth_phase)

# Concurrent environmental maintenance: Water Recycle and Pest Scan operate concurrently
env_maintenance = StrictPartialOrder(nodes=[water_recycle, pest_scan])  # no edges = concurrent

# Harvesting and logistics partial order: Harvest Crop -> Pack Produce -> Dispatch Goods
harvest_logistics = StrictPartialOrder(nodes=[harvest_crop, pack_produce, dispatch_goods])
harvest_logistics.order.add_edge(harvest_crop, pack_produce)
harvest_logistics.order.add_edge(pack_produce, dispatch_goods)

# Post-harvest optimization partial order: Waste Compost -> Data Analyze -> Cycle Review
post_harvest = StrictPartialOrder(nodes=[waste_compost, data_analyze, cycle_review])
post_harvest.order.add_edge(waste_compost, data_analyze)
post_harvest.order.add_edge(data_analyze, cycle_review)

# Combine environmental maintenance concurrent with growth phase execution
# So environmental maintenance runs concurrently with growth phase

grow_and_maintain = StrictPartialOrder(nodes=[growth_phase, env_maintenance])
# No order edges: growth_phase and env_maintenance concurrent

# After grow_and_maintain, Harvesting and logistics must happen
# After that, post-harvest optimization

middle_and_end = StrictPartialOrder(
    nodes=[grow_and_maintain, harvest_logistics, post_harvest]
)
middle_and_end.order.add_edge(grow_and_maintain, harvest_logistics)
middle_and_end.order.add_edge(harvest_logistics, post_harvest)

# Finally, initial_setup then middle_and_end
root = StrictPartialOrder(nodes=[initial_setup, middle_and_end])
root.order.add_edge(initial_setup, middle_and_end)