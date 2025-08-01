# Generated from: ada68b79-6af4-48c8-b9b0-46fe29031a37.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed warehouse, integrating hydroponic systems and AI-driven climate controls. It involves site analysis, modular structure assembly, nutrient solution preparation, crop selection based on market trends, continuous environmental monitoring, pest detection using image recognition, automated harvesting scheduling, and supply chain synchronization with local retailers to ensure freshness and reduce carbon footprint. The process also includes waste recycling, energy optimization, and data analytics for yield improvement, making it a complex but sustainable agricultural innovation in city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities as POWL transitions
site_survey        = Transition(label='Site Survey')
design_layout      = Transition(label='Design Layout')
structure_build    = Transition(label='Structure Build')
install_hydroponics= Transition(label='Install Hydroponics')
prepare_nutrients  = Transition(label='Prepare Nutrients')
select_crops       = Transition(label='Select Crops')
setup_sensors      = Transition(label='Setup Sensors')
configure_ai       = Transition(label='Configure AI')
plant_seeding      = Transition(label='Plant Seeding')
monitor_growth     = Transition(label='Monitor Growth')
detect_pests       = Transition(label='Detect Pests')
schedule_harvest   = Transition(label='Schedule Harvest')
sort_produce       = Transition(label='Sort Produce')
pack_orders        = Transition(label='Pack Orders')
coordinate_delivery= Transition(label='Coordinate Delivery')
recycle_waste      = Transition(label='Recycle Waste')
analyze_data       = Transition(label='Analyze Data')
optimize_energy    = Transition(label='Optimize Energy')

# Loop for continuous monitoring and pest detection
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_growth, detect_pests]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, structure_build, install_hydroponics,
    setup_sensors, configure_ai, prepare_nutrients, select_crops,
    plant_seeding, growth_loop, schedule_harvest, sort_produce,
    pack_orders, coordinate_delivery, recycle_waste,
    optimize_energy, analyze_data
])

# Sequential dependencies for setup and planting
root.order.add_edge(site_survey,       design_layout)
root.order.add_edge(design_layout,     structure_build)
root.order.add_edge(structure_build,   install_hydroponics)
root.order.add_edge(install_hydroponics, setup_sensors)
root.order.add_edge(setup_sensors,     configure_ai)
root.order.add_edge(configure_ai,      prepare_nutrients)
root.order.add_edge(prepare_nutrients, select_crops)
root.order.add_edge(select_crops,      plant_seeding)

# After seeding, start the growth loop and parallel sustainability tasks
root.order.add_edge(plant_seeding,     growth_loop)
root.order.add_edge(configure_ai,      recycle_waste)
root.order.add_edge(configure_ai,      optimize_energy)

# Harvest and supply‐chain sequence
root.order.add_edge(growth_loop,       schedule_harvest)
root.order.add_edge(schedule_harvest,  sort_produce)
root.order.add_edge(sort_produce,      pack_orders)
root.order.add_edge(pack_orders,       coordinate_delivery)

# Data analytics after delivery
root.order.add_edge(coordinate_delivery, analyze_data)