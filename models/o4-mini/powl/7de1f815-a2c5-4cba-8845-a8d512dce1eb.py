# Generated from: 7de1f815-a2c5-4cba-8845-a8d512dce1eb.json
# Description: This process outlines the setup of an urban rooftop farm, integrating advanced hydroponics with renewable energy sources and waste recycling systems. It involves site assessment, structural analysis, soil and water testing, equipment procurement, installation of solar panels and water recycling units, seed selection, planting schedules, pest control using natural predators, data monitoring through IoT devices, and community engagement for educational workshops. The process ensures sustainability, maximizes crop yield in limited space, and promotes urban greening while adhering to local regulations and safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey    = Transition(label='Site Survey')
structure_check= Transition(label='Structure Check')
soil_sample    = Transition(label='Soil Sample')
water_test     = Transition(label='Water Test')
procure_gear   = Transition(label='Procure Gear')
install_panels = Transition(label='Install Panels')
setup_hydro    = Transition(label='Setup Hydro')
waste_recycle  = Transition(label='Waste Recycle')
safety_audit   = Transition(label='Safety Audit')
seed_select    = Transition(label='Seed Select')
plant_crop     = Transition(label='Plant Crop')
pest_control   = Transition(label='Pest Control')
iot_config     = Transition(label='IoT Config')
data_monitor   = Transition(label='Data Monitor')
host_workshop  = Transition(label='Host Workshop')
yield_review   = Transition(label='Yield Review')

# Create the partial‐order model and register all nodes
root = StrictPartialOrder(nodes=[
    site_survey, structure_check,
    soil_sample, water_test,
    procure_gear,
    install_panels, setup_hydro, waste_recycle,
    safety_audit,
    seed_select, plant_crop,
    pest_control, iot_config, data_monitor,
    host_workshop, yield_review
])

# Define the control‐flow dependencies (→)
root.order.add_edge(site_survey,    structure_check)
root.order.add_edge(structure_check, soil_sample)
root.order.add_edge(structure_check, water_test)
root.order.add_edge(soil_sample,    procure_gear)
root.order.add_edge(water_test,     procure_gear)

root.order.add_edge(procure_gear,   install_panels)
root.order.add_edge(procure_gear,   setup_hydro)
root.order.add_edge(procure_gear,   waste_recycle)

root.order.add_edge(install_panels, safety_audit)
root.order.add_edge(setup_hydro,    safety_audit)
root.order.add_edge(waste_recycle,  safety_audit)

root.order.add_edge(safety_audit,   seed_select)
root.order.add_edge(seed_select,    plant_crop)

root.order.add_edge(plant_crop,     pest_control)
root.order.add_edge(plant_crop,     iot_config)
root.order.add_edge(plant_crop,     host_workshop)

root.order.add_edge(pest_control,   data_monitor)
root.order.add_edge(iot_config,     data_monitor)

root.order.add_edge(data_monitor,   yield_review)
root.order.add_edge(host_workshop,  yield_review)