# Generated from: e6e73b62-44cd-4136-b5e3-a12da139f46a.json
# Description: This process describes the establishment of an urban vertical farming system that integrates advanced hydroponics, IoT sensors, and renewable energy management. It involves site evaluation, modular infrastructure assembly, nutrient solution calibration, environmental monitoring setup, and crop cycle optimization. The workflow also includes waste recycling, pest control without chemicals, real-time data analytics for yield prediction, and community engagement for local produce distribution. The process aims to maximize space efficiency and sustainability in densely populated areas by leveraging technology and innovative farming techniques, ensuring fresh, organic produce year-round while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey        = Transition(label='Site Survey')
design_layout      = Transition(label='Design Layout')
procure_modules    = Transition(label='Procure Modules')
install_framework  = Transition(label='Install Framework')
setup_sensors      = Transition(label='Setup Sensors')
calibrate_nutrients= Transition(label='Calibrate Nutrients')
configure_iot      = Transition(label='Configure IoT')
plant_seeding      = Transition(label='Plant Seeding')
monitor_growth     = Transition(label='Monitor Growth')
manage_lighting    = Transition(label='Manage Lighting')
pest_control       = Transition(label='Pest Control')
recycle_waste      = Transition(label='Recycle Waste')
analyze_data       = Transition(label='Analyze Data')
adjust_environment = Transition(label='Adjust Environment')
harvest_crops      = Transition(label='Harvest Crops')
distribute_produce = Transition(label='Distribute Produce')

# Silent transition used for loop exit/redo
skip = SilentTransition()

# Define the growth‐cycle body (partial order of monitoring, controls, data, etc.)
growth_cycle = StrictPartialOrder(nodes=[
    monitor_growth,
    manage_lighting,
    pest_control,
    recycle_waste,
    analyze_data,
    adjust_environment
])
growth_cycle.order.add_edge(monitor_growth, manage_lighting)
growth_cycle.order.add_edge(manage_lighting, pest_control)
growth_cycle.order.add_edge(pest_control, recycle_waste)
growth_cycle.order.add_edge(recycle_waste, analyze_data)
growth_cycle.order.add_edge(analyze_data, adjust_environment)

# Loop over the growth cycle until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_cycle, skip])

# Build the top‐level strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    procure_modules,
    install_framework,
    setup_sensors,
    calibrate_nutrients,
    configure_iot,
    plant_seeding,
    loop,
    harvest_crops,
    distribute_produce
])

# Define the sequential flow between these nodes
root.order.add_edge(site_survey,       design_layout)
root.order.add_edge(design_layout,     procure_modules)
root.order.add_edge(procure_modules,   install_framework)
root.order.add_edge(install_framework, setup_sensors)
root.order.add_edge(setup_sensors,     calibrate_nutrients)
root.order.add_edge(calibrate_nutrients, configure_iot)
root.order.add_edge(configure_iot,     plant_seeding)
root.order.add_edge(plant_seeding,     loop)
root.order.add_edge(loop,              harvest_crops)
root.order.add_edge(harvest_crops,     distribute_produce)