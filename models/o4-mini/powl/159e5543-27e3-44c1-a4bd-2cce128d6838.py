# Generated from: 159e5543-27e3-44c1-a4bd-2cce128d6838.json
# Description: This process details the establishment of an urban vertical farming facility, integrating advanced hydroponics and IoT-based environmental controls. It begins with site evaluation and structural assessment, followed by modular system design and nutrient solution formulation. After installation, sensors are calibrated for optimal growth conditions, and AI-driven monitoring is initiated. The process includes crop selection based on local demand and seasonal factors, pest management through organic methods, and continuous data analysis to improve yield. Finally, harvested produce undergoes quality inspection before packaging and distribution to local markets, ensuring freshness and sustainability throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess      = Transition(label='Site Assess')
structure_check  = Transition(label='Structure Check')
system_design    = Transition(label='System Design')
nutrient_mix     = Transition(label='Nutrient Mix')
install_modules  = Transition(label='Install Modules')
sensor_setup     = Transition(label='Sensor Setup')
calibrate_sensors= Transition(label='Calibrate Sensors')
select_crops     = Transition(label='Select Crops')
seed_planting    = Transition(label='Seed Planting')
monitor_growth   = Transition(label='Monitor Growth')
pest_control     = Transition(label='Pest Control')
data_analyze     = Transition(label='Data Analyze')
harvest_crops    = Transition(label='Harvest Crops')
quality_check    = Transition(label='Quality Check')
pack_produce     = Transition(label='Pack Produce')
market_delivery  = Transition(label='Market Delivery')

# Concurrency: System Design and Nutrient Mix
concurrent_design_nutrient = StrictPartialOrder(
    nodes=[system_design, nutrient_mix]
)

# Concurrency: Pest Control and Data Analyze (body of the growth loop)
concurrent_pest_data = StrictPartialOrder(
    nodes=[pest_control, data_analyze]
)

# Loop: monitor growth, then optionally do pest/data then repeat
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_growth, concurrent_pest_data]
)

# Main partial order
root = StrictPartialOrder(
    nodes=[
        site_assess,
        structure_check,
        concurrent_design_nutrient,
        install_modules,
        sensor_setup,
        calibrate_sensors,
        select_crops,
        seed_planting,
        growth_loop,
        harvest_crops,
        quality_check,
        pack_produce,
        market_delivery
    ]
)

# Define the control-flow edges
root.order.add_edge(site_assess,      structure_check)
root.order.add_edge(structure_check,  concurrent_design_nutrient)
root.order.add_edge(concurrent_design_nutrient, install_modules)
root.order.add_edge(install_modules,  sensor_setup)
root.order.add_edge(sensor_setup,     calibrate_sensors)
root.order.add_edge(calibrate_sensors, select_crops)
root.order.add_edge(select_crops,     seed_planting)
root.order.add_edge(seed_planting,    growth_loop)
root.order.add_edge(growth_loop,      harvest_crops)
root.order.add_edge(harvest_crops,    quality_check)
root.order.add_edge(quality_check,    pack_produce)
root.order.add_edge(pack_produce,     market_delivery)