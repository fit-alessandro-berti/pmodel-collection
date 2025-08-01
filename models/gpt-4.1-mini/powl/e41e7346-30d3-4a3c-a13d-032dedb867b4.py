# Generated from: e41e7346-30d3-4a3c-a13d-032dedb867b4.json
# Description: This process governs the integrated management of an urban vertical farm, combining hydroponics, climate control, and automated logistics. It begins with seed selection based on market demand and environmental factors, followed by nutrient mix calibration tailored for each plant species. The system continuously monitors microclimate parameters such as humidity, CO2, and light spectrum, adjusting them dynamically. Crop growth is tracked via AI-driven imaging, predicting harvest readiness and potential pest outbreaks. Harvested produce is sorted, packaged using biodegradable materials, and dispatched through automated delivery drones. Waste is recycled into bio-compost used to enhance future cycles. The entire process ensures sustainability, efficiency, and responsiveness to urban consumers' needs while minimizing resource consumption and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')

# Climate control: microclimate parameters adjusted concurrently
climate_setup = Transition(label='Climate Setup')
light_adjust = Transition(label='Light Adjust')
co2_control = Transition(label='CO2 Control')
humidity_tune = Transition(label='Humidity Tune')

# Crop growth tracking and pest detection - partial order (growth monitor before pest detect)
growth_monitor = Transition(label='Growth Monitor')
pest_detect = Transition(label='Pest Detect')

# Harvest planning and produce sorting, packaging, dispatching (sequence)
harvest_plan = Transition(label='Harvest Plan')
produce_sort = Transition(label='Produce Sort')
pack_biodeg = Transition(label='Pack Biodeg')
drone_dispatch = Transition(label='Drone Dispatch')

# Waste recycling and compost creation - partial order (recycle before compost)
waste_recycle = Transition(label='Waste Recycle')
compost_create = Transition(label='Compost Create')

# Cycle review - followed by loop back to start (loop with nutrient mix calibration)
cycle_review = Transition(label='Cycle Review')

# Build partial orders representing concurrency and sequences

# Climate partial order (concurrent microclimate adjustments after climate setup)
climate_po = StrictPartialOrder(nodes=[climate_setup, light_adjust, co2_control, humidity_tune])
climate_po.order.add_edge(climate_setup, light_adjust)
climate_po.order.add_edge(climate_setup, co2_control)
climate_po.order.add_edge(climate_setup, humidity_tune)
# light_adjust, co2_control, humidity_tune are concurrent (no order between them)

# Growth monitoring and pest detection partial order (growth_monitor before pest_detect)
growth_po = StrictPartialOrder(nodes=[growth_monitor, pest_detect])
growth_po.order.add_edge(growth_monitor, pest_detect)

# Harvest sequence partial order
harvest_po = StrictPartialOrder(nodes=[harvest_plan, produce_sort, pack_biodeg, drone_dispatch])
harvest_po.order.add_edge(harvest_plan, produce_sort)
harvest_po.order.add_edge(produce_sort, pack_biodeg)
harvest_po.order.add_edge(pack_biodeg, drone_dispatch)

# Waste recycling and compost partial order
waste_po = StrictPartialOrder(nodes=[waste_recycle, compost_create])
waste_po.order.add_edge(waste_recycle, compost_create)

# Loop body: from nutrient mix, then all rest of cycle except seed select
# We model the whole cycle after seed select as a loop:
# Loop(body=A, redo=B):
# A = StrictPartialOrder with all activities except seed_select and cycle_review, ending at cycle_review
# B = cycle_review to nutrient_mix to start next iteration

# Inside loop body, build a partial order including:
# nutrient_mix
# climate_po
# growth_po
# harvest_po
# waste_po
# cycle_review
# plus edges representing flow and dependencies

# Collect all nodes involved inside loop body
loop_nodes = [nutrient_mix, climate_po, growth_po, harvest_po, waste_po, cycle_review]

# We need to embed partial orders inside a StrictPartialOrder nodes list.
# POWL in pm4py can nest StrictPartialOrder inside StrictPartialOrder
# For ordering edges, we use these nested nodes as nodes themselves

loop_body = StrictPartialOrder(nodes=loop_nodes)

# Add ordering edges in loop_body:
# sequence edges among these main nodes/partials:

# nutrient_mix before climate_po, growth_po, harvest_po, waste_po, cycle_review
# Although some of these happen concurrently or in sequence internally,
# at a high level, nutrient_mix starts the cycle after seed_select
loop_body.order.add_edge(nutrient_mix, climate_po)
loop_body.order.add_edge(nutrient_mix, growth_po)
loop_body.order.add_edge(nutrient_mix, harvest_po)
loop_body.order.add_edge(nutrient_mix, waste_po)
loop_body.order.add_edge(nutrient_mix, cycle_review)

# Climate setup (inside climate_po) logically before growth_po and harvest_po
# So link climate_po before growth_po and harvest_po
loop_body.order.add_edge(climate_po, growth_po)
loop_body.order.add_edge(climate_po, harvest_po)
# Growth_po before harvest_po (harvest depends on growth monitoring)
loop_body.order.add_edge(growth_po, harvest_po)

# Harvest_po before waste_po (harvest ends before waste recycling)
loop_body.order.add_edge(harvest_po, waste_po)

# Waste_po before cycle_review (recycling happens before cycle review)
loop_body.order.add_edge(waste_po, cycle_review)

# Define the LOOP operator: body = loop_body, redo = nutrient_mix (new nutrient mix for next cycle)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, nutrient_mix])

# The overall root partial order:
# start with seed_select
# then the loop

root = StrictPartialOrder(nodes=[seed_select, loop])
root.order.add_edge(seed_select, loop)