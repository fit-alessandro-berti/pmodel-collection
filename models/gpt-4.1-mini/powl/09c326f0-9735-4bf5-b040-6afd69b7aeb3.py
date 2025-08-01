# Generated from: 09c326f0-9735-4bf5-b040-6afd69b7aeb3.json
# Description: This process outlines the setup of an urban vertical farming system within a repurposed industrial warehouse. It involves site assessment, modular rack installation, climate control calibration, nutrient solution preparation, seed selection, automated planting, sensor integration, lighting optimization, pest management strategy, growth monitoring, harvest scheduling, yield analysis, waste recycling, and final produce packaging. The process ensures sustainable food production by leveraging advanced hydroponic technology, IoT devices for real-time monitoring, and data-driven adjustments for maximizing yield in limited urban spaces while minimizing environmental impact and resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_assess = Transition(label='Site Assess')
rack_install = Transition(label='Rack Install')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
seed_select = Transition(label='Seed Select')
auto_plant = Transition(label='Auto Plant')
sensor_setup = Transition(label='Sensor Setup')
light_adjust = Transition(label='Light Adjust')
pest_control = Transition(label='Pest Control')
growth_track = Transition(label='Growth Track')
harvest_plan = Transition(label='Harvest Plan')
yield_review = Transition(label='Yield Review')
waste_sort = Transition(label='Waste Sort')
produce_pack = Transition(label='Produce Pack')
data_sync = Transition(label='Data Sync')

# Setup partial order reflecting the process description:
# Sequential logical order with some concurrency:
# Site Assess --> Rack Install --> Climate Setup --> Nutrient Prep
# Seed Select --> Auto Plant --> Sensor Setup and Light Adjust (concurrent)
# Pest Control --> Growth Track --> Harvest Plan --> Yield Review
# Waste Sort and Data Sync (concurrent) before Produce Pack

# Create concurrency PO nodes:
# sensor_setup and light_adjust can be concurrent after auto_plant
sensor_light_PO = StrictPartialOrder(nodes=[sensor_setup, light_adjust])
# No order edges because concurrent

# waste_sort and data_sync before produce_pack (concurrent)
waste_data_PO = StrictPartialOrder(nodes=[waste_sort, data_sync])

# Now build partial order of entire process

nodes = [
    site_assess,
    rack_install,
    climate_setup,
    nutrient_prep,
    seed_select,
    auto_plant,
    sensor_light_PO,
    pest_control,
    growth_track,
    harvest_plan,
    yield_review,
    waste_data_PO,
    produce_pack,
]

root = StrictPartialOrder(nodes=nodes)
order = root.order

# Establish order edges reflecting dependencies
order.add_edge(site_assess, rack_install)
order.add_edge(rack_install, climate_setup)
order.add_edge(climate_setup, nutrient_prep)

order.add_edge(nutrient_prep, seed_select)
order.add_edge(seed_select, auto_plant)
order.add_edge(auto_plant, sensor_light_PO)  # sensor and light concurrent after auto plant

order.add_edge(sensor_light_PO, pest_control)
order.add_edge(pest_control, growth_track)
order.add_edge(growth_track, harvest_plan)
order.add_edge(harvest_plan, yield_review)

order.add_edge(yield_review, waste_data_PO)  # waste_sort and data_sync concurrent after yield review
order.add_edge(waste_data_PO, produce_pack)