# Generated from: 49d62836-fb25-4270-a3a9-611365acf3da.json
# Description: This process outlines the establishment of an urban vertical farming system designed to maximize crop yield in limited city spaces by integrating hydroponics, AI-driven climate control, and automated harvesting. It begins with site scouting and structural assessment, followed by modular system design tailored to specific crops. Installation includes environmental sensors, water recycling units, and LED lighting arrays. After setup, the system undergoes calibration and AI model training to optimize growth conditions. Routine maintenance and yield analysis ensure continuous improvement. The process also incorporates community engagement for education and local distribution logistics to minimize food miles, creating a sustainable urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as POWL transitions
site_scouting   = Transition(label='Site Scouting')
structure_check = Transition(label='Structure Check')
modular_design  = Transition(label='Modular Design')
system_install  = Transition(label='System Install')
sensor_setup    = Transition(label='Sensor Setup')
water_recycling = Transition(label='Water Recycling')
led_wiring      = Transition(label='LED Wiring')
ai_calibration  = Transition(label='AI Calibration')
model_training  = Transition(label='Model Training')
crop_planting   = Transition(label='Crop Planting')
climate_control = Transition(label='Climate Control')
harvest_automate= Transition(label='Harvest Automate')
yield_analysis  = Transition(label='Yield Analysis')
maintenance     = Transition(label='Maintenance')
community_engage= Transition(label='Community Engage')
logistics_plan  = Transition(label='Logistics Plan')

# Installation sub‐process: sensor, recycling and LED wiring can occur in parallel
install_sub = StrictPartialOrder(nodes=[sensor_setup, water_recycling, led_wiring])

# Final engagement & logistics can occur in parallel
end_sub = StrictPartialOrder(nodes=[community_engage, logistics_plan])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_scouting,
    structure_check,
    modular_design,
    system_install,
    install_sub,
    ai_calibration,
    model_training,
    crop_planting,
    climate_control,
    harvest_automate,
    yield_analysis,
    maintenance,
    end_sub
])

# Add the control‐flow edges
root.order.add_edge(site_scouting,   structure_check)
root.order.add_edge(structure_check, modular_design)
root.order.add_edge(modular_design,  system_install)
root.order.add_edge(system_install,  install_sub)
root.order.add_edge(install_sub,     ai_calibration)
root.order.add_edge(ai_calibration,  model_training)
root.order.add_edge(model_training,  crop_planting)
root.order.add_edge(crop_planting,   climate_control)
root.order.add_edge(climate_control, harvest_automate)
root.order.add_edge(harvest_automate,yield_analysis)
root.order.add_edge(yield_analysis,  maintenance)
root.order.add_edge(maintenance,     end_sub)