# Generated from: 8e358dcf-d2d5-4bc8-88f7-37b02b2fc618.json
# Description: This process outlines the integration of a vertical farming system within an urban commercial building, combining agriculture, technology, and logistics. The workflow includes site assessment, modular farm design, environmental control setup, automated nutrient delivery, crop monitoring via IoT sensors, AI-driven yield prediction, pest management, energy optimization, waste recycling, produce packaging, and distribution logistics. It involves coordination between architects, agronomists, IT specialists, and supply chain managers to ensure sustainable production, minimal environmental impact, and fresh produce delivery directly to local consumers and retailers in an efficient, scalable manner.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
install_modules   = Transition(label='Install Modules')
setup_sensors     = Transition(label='Setup Sensors')
calibrate_systems = Transition(label='Calibrate Systems')
deploy_ai         = Transition(label='Deploy AI')

nutrient_mix      = Transition(label='Nutrient Mix')
crop_planting     = Transition(label='Crop Planting')
monitor_growth    = Transition(label='Monitor Growth')

pest_control      = Transition(label='Pest Control')
energy_audit      = Transition(label='Energy Audit')
waste_sort        = Transition(label='Waste Sort')
system_update     = Transition(label='System Update')

package_produce   = Transition(label='Package Produce')
schedule_delivery = Transition(label='Schedule Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the planting-monitoring partial order (A)
A = StrictPartialOrder(nodes=[nutrient_mix, crop_planting, monitor_growth])
A.order.add_edge(nutrient_mix, crop_planting)
A.order.add_edge(crop_planting, monitor_growth)

# Define the maintenance-update partial order (B)
B = StrictPartialOrder(nodes=[pest_control, energy_audit, waste_sort, system_update])
B.order.add_edge(pest_control, system_update)
B.order.add_edge(energy_audit, system_update)
B.order.add_edge(waste_sort, system_update)

# Loop: do A (plant & monitor), then optionally B (maintenance & update), repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Assemble the full workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    install_modules,
    setup_sensors,
    calibrate_systems,
    deploy_ai,
    loop,
    package_produce,
    schedule_delivery,
    customer_feedback
])

# Define the control-flow edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, setup_sensors)
root.order.add_edge(setup_sensors, calibrate_systems)
root.order.add_edge(calibrate_systems, deploy_ai)
root.order.add_edge(deploy_ai, loop)
root.order.add_edge(loop, package_produce)
root.order.add_edge(package_produce, schedule_delivery)
root.order.add_edge(schedule_delivery, customer_feedback)