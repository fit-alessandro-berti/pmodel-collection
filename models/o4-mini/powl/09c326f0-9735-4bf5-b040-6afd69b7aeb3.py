# Generated from: 09c326f0-9735-4bf5-b040-6afd69b7aeb3.json
# Description: This process outlines the setup of an urban vertical farming system within a repurposed industrial warehouse. It involves site assessment, modular rack installation, climate control calibration, nutrient solution preparation, seed selection, automated planting, sensor integration, lighting optimization, pest management strategy, growth monitoring, harvest scheduling, yield analysis, waste recycling, and final produce packaging. The process ensures sustainable food production by leveraging advanced hydroponic technology, IoT devices for real-time monitoring, and data-driven adjustments for maximizing yield in limited urban spaces while minimizing environmental impact and resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_assess    = Transition(label='Site Assess')
rack_install  = Transition(label='Rack Install')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
seed_select   = Transition(label='Seed Select')
sensor_setup  = Transition(label='Sensor Setup')
light_adjust  = Transition(label='Light Adjust')
auto_plant    = Transition(label='Auto Plant')
growth_track  = Transition(label='Growth Track')
pest_control  = Transition(label='Pest Control')
yield_review  = Transition(label='Yield Review')
data_sync     = Transition(label='Data Sync')
harvest_plan  = Transition(label='Harvest Plan')
produce_pack  = Transition(label='Produce Pack')
waste_sort    = Transition(label='Waste Sort')

# Body of the growth loop: Pest Control, Yield Review, Data Sync all concurrent
loop_body = StrictPartialOrder(nodes=[pest_control, yield_review, data_sync])

# LOOP: execute a Growth Track, then either exit or run the loop_body and repeat
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_track, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_assess, rack_install,
    climate_setup, nutrient_prep, seed_select,
    sensor_setup, light_adjust,
    auto_plant,
    growth_loop,
    harvest_plan, produce_pack, waste_sort
])

# Define the control‐flow dependencies
root.order.add_edge(site_assess,    rack_install)
root.order.add_edge(rack_install,   climate_setup)
root.order.add_edge(rack_install,   nutrient_prep)
root.order.add_edge(rack_install,   sensor_setup)
root.order.add_edge(rack_install,   light_adjust)
root.order.add_edge(nutrient_prep,  seed_select)
root.order.add_edge(climate_setup,  auto_plant)
root.order.add_edge(seed_select,    auto_plant)
root.order.add_edge(sensor_setup,   auto_plant)
root.order.add_edge(light_adjust,   auto_plant)
root.order.add_edge(auto_plant,     growth_loop)
root.order.add_edge(growth_loop,    harvest_plan)
root.order.add_edge(harvest_plan,   produce_pack)
root.order.add_edge(produce_pack,   waste_sort)