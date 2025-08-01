# Generated from: 5193f5f5-df65-4865-99f3-b24b2b962b15.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm in a metropolitan environment. It involves site assessment, modular design planning, installation of hydroponic and aeroponic systems, integration of IoT sensors for environmental monitoring, seed selection based on microclimate data, nutrient solution formulation, automation programming, staff training on crop management, pest control using biocontrol agents, energy optimization through renewable sources, waste recycling protocols, harvest scheduling, packaging logistics, and continuous yield analysis to maximize production efficiency while minimizing environmental impact and ensuring sustainable urban agriculture practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey    = Transition(label='Site Survey')
design_plan    = Transition(label='Design Plan')
module_setup   = Transition(label='Module Setup')
system_install = Transition(label='System Install')
sensor_deploy  = Transition(label='Sensor Deploy')
seed_select    = Transition(label='Seed Select')
nutrient_mix   = Transition(label='Nutrient Mix')
automation_code= Transition(label='Automation Code')
staff_train    = Transition(label='Staff Train')
pest_control   = Transition(label='Pest Control')
energy_audit   = Transition(label='Energy Audit')
waste_sort     = Transition(label='Waste Sort')
harvest_plan   = Transition(label='Harvest Plan')
pack_prep      = Transition(label='Pack Prep')
yield_review   = Transition(label='Yield Review')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_plan, module_setup, system_install,
    sensor_deploy, seed_select, nutrient_mix, automation_code,
    staff_train, pest_control, energy_audit, waste_sort,
    harvest_plan, pack_prep, yield_review
])

# Sequential steps
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(design_plan, module_setup)
root.order.add_edge(module_setup, system_install)
root.order.add_edge(system_install, sensor_deploy)
root.order.add_edge(sensor_deploy, seed_select)
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, automation_code)

# Parallel branches after automation_code
root.order.add_edge(automation_code, staff_train)
root.order.add_edge(automation_code, pest_control)
root.order.add_edge(automation_code, energy_audit)
root.order.add_edge(automation_code, waste_sort)

# Join before harvesting
root.order.add_edge(staff_train, harvest_plan)
root.order.add_edge(pest_control, harvest_plan)
root.order.add_edge(energy_audit, harvest_plan)
root.order.add_edge(waste_sort, harvest_plan)

# Final steps
root.order.add_edge(harvest_plan, pack_prep)
root.order.add_edge(pack_prep, yield_review)