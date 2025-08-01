# Generated from: b25cc843-0ec7-42c3-ae0d-cee7e919327c.json
# Description: This process outlines the establishment of an urban vertical farm designed to maximize crop yield within limited city space by integrating hydroponics, IoT monitoring, and renewable energy systems. It begins with site analysis and structural assessment, followed by modular rack installation, nutrient solution preparation, and seedling placement. Subsequent activities involve sensor calibration, automated irrigation scheduling, LED lighting optimization, and continuous environmental data collection. The process also covers pest management through biological controls, yield forecasting using AI models, and energy consumption balancing with solar panels. Finally, the harvested produce undergoes quality inspection, packaging, and distribution to local markets, ensuring sustainability and freshness throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as transitions
site_survey     = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
rack_setup      = Transition(label='Rack Setup')
seed_prep       = Transition(label='Seed Prep')
nutrient_mix    = Transition(label='Nutrient Mix')
seed_sowing     = Transition(label='Seed Sowing')
sensor_setup    = Transition(label='Sensor Setup')
irrigation_plan = Transition(label='Irrigation Plan')
light_adjust    = Transition(label='Light Adjust')
data_capture    = Transition(label='Data Capture')
pest_control    = Transition(label='Pest Control')
yield_forecast  = Transition(label='Yield Forecast')
energy_sync     = Transition(label='Energy Sync')
harvest_inspect = Transition(label='Harvest Inspect')
pack_dispatch   = Transition(label='Pack Dispatch')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structure_check, rack_setup,
    seed_prep, nutrient_mix, seed_sowing,
    sensor_setup, irrigation_plan, light_adjust, data_capture,
    pest_control, yield_forecast, energy_sync,
    harvest_inspect, pack_dispatch
])

# Add ordering constraints
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, rack_setup)
root.order.add_edge(rack_setup, seed_prep)
root.order.add_edge(seed_prep, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_sowing)

root.order.add_edge(seed_sowing, sensor_setup)
root.order.add_edge(sensor_setup, irrigation_plan)
root.order.add_edge(sensor_setup, light_adjust)
root.order.add_edge(sensor_setup, data_capture)

root.order.add_edge(data_capture, pest_control)
root.order.add_edge(data_capture, yield_forecast)
root.order.add_edge(data_capture, energy_sync)

root.order.add_edge(pest_control, harvest_inspect)
root.order.add_edge(yield_forecast, harvest_inspect)
root.order.add_edge(energy_sync, harvest_inspect)

root.order.add_edge(harvest_inspect, pack_dispatch)