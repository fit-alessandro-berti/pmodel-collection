# Generated from: 3184ef64-d280-4924-b9e4-a92af19d8a1d.json
# Description: This process outlines the complex operations involved in managing an urban vertical farming system that integrates automated hydroponics, climate control, and AI-driven nutrient optimization. It begins with seed selection tailored to urban environmental constraints, followed by precise germination monitoring using sensor arrays. Nutrient solution formulation adapts dynamically based on real-time plant growth data. Climate regulation adjusts humidity, temperature, and lighting to maximize photosynthesis efficiency. Periodic pest detection employs machine vision to identify and isolate affected zones. Harvesting is automated with robotic arms, while post-harvest sorting ensures quality consistency. Waste recycling converts organic remnants into bio-fertilizers, completing a sustainable loop. This atypical process requires coordination among IoT devices, AI analytics, and human oversight to maintain continuous production within limited urban spaces, addressing food security with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection   = Transition(label='Seed Selection')
germinate_check  = Transition(label='Germinate Check')
nutrient_mix     = Transition(label='Nutrient Mix')
growth_monitor   = Transition(label='Growth Monitor')
climate_adjust   = Transition(label='Climate Adjust')
light_control    = Transition(label='Light Control')
humidity_set     = Transition(label='Humidity Set')
pest_detect      = Transition(label='Pest Detect')
zone_isolation   = Transition(label='Zone Isolation')
robotic_harvest  = Transition(label='Robotic Harvest')
quality_sort     = Transition(label='Quality Sort')
waste_collect    = Transition(label='Waste Collect')
bio_fertilize    = Transition(label='Bio-fertilize')
data_sync        = Transition(label='Data Sync')
system_alert     = Transition(label='System Alert')

# Silent transitions for optional alert and loop back
skip_alert = SilentTransition()
skip_loop  = SilentTransition()

# Exclusive choice: optionally raise an alert after data sync
xor_alert = OperatorPOWL(
    operator=Operator.XOR,
    children=[skip_alert, system_alert]
)

# Build the core cycle as a strict partial order
cycle = StrictPartialOrder(nodes=[
    seed_selection,
    germinate_check,
    nutrient_mix,
    growth_monitor,
    climate_adjust,
    light_control,
    humidity_set,
    pest_detect,
    zone_isolation,
    robotic_harvest,
    quality_sort,
    waste_collect,
    bio_fertilize,
    data_sync,
    xor_alert
])

# Establish the control-flow (partial order) dependencies
cycle.order.add_edge(seed_selection,  germinate_check)
cycle.order.add_edge(germinate_check, nutrient_mix)
cycle.order.add_edge(nutrient_mix,    growth_monitor)
cycle.order.add_edge(growth_monitor,  climate_adjust)
cycle.order.add_edge(climate_adjust,  light_control)
cycle.order.add_edge(climate_adjust,  humidity_set)
cycle.order.add_edge(light_control,   pest_detect)
cycle.order.add_edge(humidity_set,    pest_detect)
cycle.order.add_edge(pest_detect,     zone_isolation)
cycle.order.add_edge(zone_isolation,  robotic_harvest)
cycle.order.add_edge(robotic_harvest, quality_sort)
cycle.order.add_edge(quality_sort,    waste_collect)
cycle.order.add_edge(waste_collect,   bio_fertilize)
cycle.order.add_edge(bio_fertilize,   data_sync)
cycle.order.add_edge(data_sync,       xor_alert)

# Wrap the cycle in a loop to model the continuous sustainable process
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle, skip_loop]
)