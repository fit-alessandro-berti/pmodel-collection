# Generated from: 45b114d1-7f1f-4d7e-8fa4-7396de6f6069.json
# Description: This process outlines the end-to-end setup of an urban vertical farming system within a repurposed industrial building. It involves site analysis, structural modifications, installation of hydroponic and aeroponic systems, integration of IoT sensors for environmental monitoring, calibration of nutrient delivery systems, implementation of energy-efficient LED lighting, and automation of climate control. The process further includes staff training on smart farming techniques, development of crop scheduling algorithms, pest management protocols without pesticides, and establishing partnerships with local markets for produce distribution. Continuous data collection and system optimization ensure sustainable and scalable urban agriculture in constrained city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey         = Transition(label='Site Survey')
structure_assess    = Transition(label='Structure Assess')
layout_design       = Transition(label='Layout Design')
install_frames      = Transition(label='Install Frames')
setup_hydroponics   = Transition(label='Setup Hydroponics')
add_sensors         = Transition(label='Add Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
install_lighting    = Transition(label='Install Lighting')
configure_climate   = Transition(label='Configure Climate')
develop_software    = Transition(label='Develop Software')
train_staff         = Transition(label='Train Staff')
pest_monitor        = Transition(label='Pest Monitor')
crop_scheduling     = Transition(label='Crop Scheduling')
market_liaison      = Transition(label='Market Liaison')
data_analysis       = Transition(label='Data Analysis')

# Loop for continuous data analysis / system optimization
skip      = SilentTransition()
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, skip])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_assess,
    layout_design,
    install_frames,
    setup_hydroponics,
    add_sensors,
    calibrate_nutrients,
    install_lighting,
    configure_climate,
    develop_software,
    train_staff,
    pest_monitor,
    crop_scheduling,
    market_liaison,
    loop_data
])

# 1) Sequential core setup up to climate configuration
root.order.add_edge(site_survey,      structure_assess)
root.order.add_edge(structure_assess, layout_design)
root.order.add_edge(layout_design,    install_frames)
root.order.add_edge(install_frames,   setup_hydroponics)
root.order.add_edge(setup_hydroponics, add_sensors)
root.order.add_edge(add_sensors,      calibrate_nutrients)
root.order.add_edge(calibrate_nutrients, install_lighting)
root.order.add_edge(install_lighting,   configure_climate)

# 2) After climate is configured, four branches start in parallel
root.order.add_edge(configure_climate, develop_software)
root.order.add_edge(configure_climate, train_staff)
root.order.add_edge(configure_climate, pest_monitor)
root.order.add_edge(configure_climate, market_liaison)

# 3) Software development precedes crop scheduling
root.order.add_edge(develop_software, crop_scheduling)

# 4) Once all four branches finish, enter the continuous data‐analysis loop
for n in [train_staff, pest_monitor, crop_scheduling, market_liaison]:
    root.order.add_edge(n, loop_data)