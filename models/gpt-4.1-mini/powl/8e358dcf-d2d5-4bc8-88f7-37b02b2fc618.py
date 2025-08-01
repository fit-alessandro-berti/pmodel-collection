# Generated from: 8e358dcf-d2d5-4bc8-88f7-37b02b2fc618.json
# Description: This process outlines the integration of a vertical farming system within an urban commercial building, combining agriculture, technology, and logistics. The workflow includes site assessment, modular farm design, environmental control setup, automated nutrient delivery, crop monitoring via IoT sensors, AI-driven yield prediction, pest management, energy optimization, waste recycling, produce packaging, and distribution logistics. It involves coordination between architects, agronomists, IT specialists, and supply chain managers to ensure sustainable production, minimal environmental impact, and fresh produce delivery directly to local consumers and retailers in an efficient, scalable manner.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_modules = Transition(label='Install Modules')
setup_sensors = Transition(label='Setup Sensors')
calibrate_systems = Transition(label='Calibrate Systems')
deploy_ai = Transition(label='Deploy AI')
nutrient_mix = Transition(label='Nutrient Mix')
crop_planting = Transition(label='Crop Planting')
monitor_growth = Transition(label='Monitor Growth')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
waste_sort = Transition(label='Waste Sort')
package_produce = Transition(label='Package Produce')
schedule_delivery = Transition(label='Schedule Delivery')
customer_feedback = Transition(label='Customer Feedback')
system_update = Transition(label='System Update')

# Partial order 1: design & install farm modules after site survey
po1 = StrictPartialOrder(nodes=[site_survey, design_layout, install_modules])
po1.order.add_edge(site_survey, design_layout)
po1.order.add_edge(design_layout, install_modules)

# Partial order 2: setup and calibrate sensors and AI after module installation
po2 = StrictPartialOrder(nodes=[setup_sensors, calibrate_systems, deploy_ai])
po2.order.add_edge(setup_sensors, calibrate_systems)
po2.order.add_edge(calibrate_systems, deploy_ai)

# Partial order 3: farming activities starting with nutrient mix and planting,
# then grow monitoring with pest control; crop monitoring includes IoT sensors (monitor_growth)
# and pest control concurrently after planting
planting_block = StrictPartialOrder(nodes=[nutrient_mix, crop_planting])
planting_block.order.add_edge(nutrient_mix, crop_planting)

monitor_block = StrictPartialOrder(nodes=[monitor_growth, pest_control])
# monitor_growth and pest_control concurrent (no edges)

farming = StrictPartialOrder(nodes=[planting_block, monitor_block])
farming.order.add_edge(planting_block, monitor_block)  # monitor after planting block

# Partial order 4: sustainability activities concurrent to farming or after deploy AI
sustainability = StrictPartialOrder(nodes=[energy_audit, waste_sort])
# energy_audit and waste_sort concurrent (no edges)

# Partial order 5: packaging and delivery after farming and sustainability
packaging_delivery = StrictPartialOrder(nodes=[package_produce, schedule_delivery])
packaging_delivery.order.add_edge(package_produce, schedule_delivery)

# Partial order 6: feedback and system update after delivery
feedback_update = StrictPartialOrder(nodes=[customer_feedback, system_update])
feedback_update.order.add_edge(customer_feedback, system_update)

# Combine all major blocks in a single PO
root = StrictPartialOrder(
    nodes=[po1, po2, farming, sustainability, packaging_delivery, feedback_update]
)

# Define edges for ordering these blocks:
# po1 -> po2 -> farming
root.order.add_edge(po1, po2)
root.order.add_edge(po2, farming)

# deploy AI is inside po2, sustainability can start after deploy AI (i.e. after po2)
root.order.add_edge(po2, sustainability)

# packaging_delivery after farming and sustainability
root.order.add_edge(farming, packaging_delivery)
root.order.add_edge(sustainability, packaging_delivery)

# feedback_update after packaging_delivery
root.order.add_edge(packaging_delivery, feedback_update)