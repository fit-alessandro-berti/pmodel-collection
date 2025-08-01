# Generated from: 601a2a31-006b-48a5-b74d-68977e37f16c.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial warehouse. It begins with site evaluation and structural reinforcement, followed by modular rack assembly and installation of hydroponic systems. Specialized lighting calibration is conducted to optimize plant growth cycles. Nutrient solution formulation and water recycling integration ensure sustainable cultivation. Crop selection is aligned with local demand forecasting. Continuous environmental monitoring and pest management protocols are implemented via IoT devices. Harvest scheduling coordinates with automated packaging and distribution logistics, ensuring freshness and reducing waste. The process concludes with regular data analysis for yield optimization and adaptive system maintenance to sustain productivity in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_eval = Transition(label='Site Eval')
structure_check = Transition(label='Structure Check')
rack_install = Transition(label='Rack Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
light_calibrate = Transition(label='Light Calibrate')
nutrient_mix = Transition(label='Nutrient Mix')
water_cycle = Transition(label='Water Cycle')
crop_select = Transition(label='Crop Select')
demand_forecast = Transition(label='Demand Forecast')
enviro_monitor = Transition(label='Enviro Monitor')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
auto_package = Transition(label='Auto Package')
logistics_setup = Transition(label='Logistics Setup')
data_analyze = Transition(label='Data Analyze')
system_maintain = Transition(label='System Maintain')

# Partial orders for initial sequential activities
# Site evaluation and structural reinforcement
init_po = StrictPartialOrder(nodes=[site_eval, structure_check])
init_po.order.add_edge(site_eval, structure_check)

# Followed by modular rack assembly and hydroponic setup
modular_po = StrictPartialOrder(nodes=[rack_install, hydroponic_setup])
modular_po.order.add_edge(rack_install, hydroponic_setup)

# Specialized lighting calibration
light = light_calibrate

# Nutrient mix and water cycle integration (concurrent)
nutrient_water_po = StrictPartialOrder(nodes=[nutrient_mix, water_cycle])
# no order edges: concurrent

# Crop selection and demand forecasting (sequential)
crop_demand_po = StrictPartialOrder(nodes=[crop_select, demand_forecast])
crop_demand_po.order.add_edge(crop_select, demand_forecast)

# Environmental monitoring and pest control (concurrent)
env_pest_po = StrictPartialOrder(nodes=[enviro_monitor, pest_control])
# no order edges: concurrent

# Harvest plan followed by packaging and logistics (sequential chain)
harvest_pack_log_po = StrictPartialOrder(
    nodes=[harvest_plan, auto_package, logistics_setup]
)
harvest_pack_log_po.order.add_edge(harvest_plan, auto_package)
harvest_pack_log_po.order.add_edge(auto_package, logistics_setup)

# Data analysis and system maintenance (sequential)
final_po = StrictPartialOrder(nodes=[data_analyze, system_maintain])
final_po.order.add_edge(data_analyze, system_maintain)

# Compose overall partial order combining all parts
# Some parts are sequential, others concurrent

# We compose from start to end with proper ordering:

# Step 1: init_po --> modular_po
# Step 2: modular_po --> light
# Step 3: light --> nutrient_water_po
# Step 4: nutrient_water_po --> crop_demand_po
# Step 5: crop_demand_po --> env_pest_po
# Step 6: env_pest_po --> harvest_pack_log_po
# Step 7: harvest_pack_log_po --> final_po

# Gather all nodes
all_nodes = [
    init_po, 
    modular_po, 
    light,
    nutrient_water_po,
    crop_demand_po,
    env_pest_po,
    harvest_pack_log_po,
    final_po
]

root = StrictPartialOrder(nodes=all_nodes)

# Add ordering edges between the parts
root.order.add_edge(init_po, modular_po)
root.order.add_edge(modular_po, light)
root.order.add_edge(light, nutrient_water_po)
root.order.add_edge(nutrient_water_po, crop_demand_po)
root.order.add_edge(crop_demand_po, env_pest_po)
root.order.add_edge(env_pest_po, harvest_pack_log_po)
root.order.add_edge(harvest_pack_log_po, final_po)