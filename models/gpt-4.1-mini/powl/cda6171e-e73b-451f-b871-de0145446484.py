# Generated from: cda6171e-e73b-451f-b871-de0145446484.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, structural modifications, environmental control installations, hydroponic system setup, nutrient solution preparation, seed selection, automated planting, growth monitoring via IoT sensors, pest control using integrated biological methods, energy optimization through smart grid integration, water recycling implementation, harvesting automation, packaging with minimal waste materials, distribution logistics coordination, and post-harvest data analysis to improve yield efficiency. Each step requires cross-disciplinary collaboration among architects, agronomists, engineers, and supply chain specialists to adapt traditional farming techniques to a compact, sustainable, and tech-driven urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Create transitions for all activities
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
modify_layout = Transition(label='Modify Layout')
install_hvac = Transition(label='Install HVAC')
setup_hydroponics = Transition(label='Setup Hydroponics')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds = Transition(label='Select Seeds')
automate_planting = Transition(label='Automate Planting')
deploy_sensors = Transition(label='Deploy Sensors')
pest_control = Transition(label='Pest Control')
optimize_energy = Transition(label='Optimize Energy')
recycle_water = Transition(label='Recycle Water')
automate_harvest = Transition(label='Automate Harvest')
package_crops = Transition(label='Package Crops')
coordinate_delivery = Transition(label='Coordinate Delivery')
analyze_data = Transition(label='Analyze Data')

# Define partial order nodes for site preparation and initial build sequence
site_prep = StrictPartialOrder(nodes=[site_analysis, structure_check, modify_layout])
site_prep.order.add_edge(site_analysis, structure_check)
site_prep.order.add_edge(structure_check, modify_layout)

# Environmental and system installations partial order
installations = StrictPartialOrder(nodes=[install_hvac, setup_hydroponics])
installations.order.add_edge(install_hvac, setup_hydroponics)

# Nutrient preparation and seed selection can be done concurrently with installations
nutrient_seed = StrictPartialOrder(nodes=[prepare_nutrients, select_seeds])
# no edges -> concurrent

# Automated planting after seed selection and nutrient prep
planting = StrictPartialOrder(nodes=[automate_planting])
# must come after prepare_nutrients and select_seeds, so edges from both to automate_planting added later

# Growth monitoring, pest control, energy optimization, and water recycling can happen concurrently after planting
monitoring = StrictPartialOrder(nodes=[deploy_sensors, pest_control, optimize_energy, recycle_water])
# no edges internally -> concurrent

# After growth phase, automate harvest
harvest = StrictPartialOrder(nodes=[automate_harvest])

# Packaging and distribution follow harvest, sequentially
pack_dist = StrictPartialOrder(nodes=[package_crops, coordinate_delivery])
pack_dist.order.add_edge(package_crops, coordinate_delivery)

# Final analysis after delivery
analysis = StrictPartialOrder(nodes=[analyze_data])

# Compose the whole process partial order
nodes_all = [
    site_prep,
    installations,
    nutrient_seed,
    planting,
    monitoring,
    harvest,
    pack_dist,
    analysis
]
root = StrictPartialOrder(nodes=nodes_all)

# Add dependencies between parts
# site_prep --> installations and nutrient_seed (these start after modify_layout)
root.order.add_edge(site_prep, installations)
root.order.add_edge(site_prep, nutrient_seed)

# installations and nutrient_seed --> automate_planting
root.order.add_edge(installations, planting)
root.order.add_edge(nutrient_seed, planting)

# automate_planting --> monitoring
root.order.add_edge(planting, monitoring)

# monitoring --> harvest
root.order.add_edge(monitoring, harvest)

# harvest --> packaging and distribution
root.order.add_edge(harvest, pack_dist)

# delivery --> analysis
root.order.add_edge(pack_dist, analysis)