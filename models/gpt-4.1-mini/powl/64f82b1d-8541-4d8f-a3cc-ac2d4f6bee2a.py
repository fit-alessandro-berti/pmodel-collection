# Generated from: 64f82b1d-8541-4d8f-a3cc-ac2d4f6bee2a.json
# Description: This process outlines the adaptive urban farming cycle designed for optimizing limited city space agriculture through iterative environmental sensing, dynamic resource allocation, and community feedback integration. Beginning with soil analysis and microclimate monitoring, the system adapts water and nutrient delivery in real-time. Crop selection is continuously adjusted via AI-driven growth predictions, while pest management employs biological controls activated by sensor alerts. Harvesting schedules are coordinated with local market demands, and waste recycling integrates organic residues back into the soil. Community workshops and digital platforms gather resident input, feeding into future cycles for sustainable and responsive urban food production. This atypical yet practical approach ensures resilience and efficiency in metropolitan agronomy.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
soil_testing = Transition(label='Soil Testing')
climate_scan = Transition(label='Climate Scan')

water_allocation = Transition(label='Water Allocation')
nutrient_dosing = Transition(label='Nutrient Dosing')

pest_detection = Transition(label='Pest Detection')
biocontrol_release = Transition(label='Biocontrol Release')

growth_prediction = Transition(label='Growth Prediction')
crop_adjustment = Transition(label='Crop Adjustment')

market_sync = Transition(label='Market Sync')
harvest_planning = Transition(label='Harvest Planning')

compost_processing = Transition(label='Compost Processing')
waste_collection = Transition(label='Waste Collection')

workshop_hosting = Transition(label='Workshop Hosting')
community_feedback = Transition(label='Community Feedback')

data_integration = Transition(label='Data Integration')
cycle_review = Transition(label='Cycle Review')


# Partial Order for environmental sensing: Soil Testing and Climate Scan concurrent
env_sensing = StrictPartialOrder(nodes=[soil_testing, climate_scan])  # no order, concurrent


# Partial Order for resource allocation: Water Allocation --> Nutrient Dosing
resource_allocation = StrictPartialOrder(nodes=[water_allocation, nutrient_dosing])
resource_allocation.order.add_edge(water_allocation, nutrient_dosing)


# Partial Order for pest management: Pest Detection --> Biocontrol Release
pest_management = StrictPartialOrder(nodes=[pest_detection, biocontrol_release])
pest_management.order.add_edge(pest_detection, biocontrol_release)


# Partial Order for growth: Growth Prediction --> Crop Adjustment
growth_cycle = StrictPartialOrder(nodes=[growth_prediction, crop_adjustment])
growth_cycle.order.add_edge(growth_prediction, crop_adjustment)


# Partial Order for harvesting: Harvest Planning --> Market Sync
harvesting = StrictPartialOrder(nodes=[harvest_planning, market_sync])
harvesting.order.add_edge(harvest_planning, market_sync)


# Partial Order for waste recycling: Waste Collection --> Compost Processing
waste_recycling = StrictPartialOrder(nodes=[waste_collection, compost_processing])
waste_recycling.order.add_edge(waste_collection, compost_processing)


# Partial Order for community input: Workshop Hosting --> Community Feedback
community_input = StrictPartialOrder(nodes=[workshop_hosting, community_feedback])
community_input.order.add_edge(workshop_hosting, community_feedback)


# Data integration after community feedback
data_integration_po = StrictPartialOrder(nodes=[community_feedback, data_integration])
data_integration_po.order.add_edge(community_feedback, data_integration)


# Build the overall cycle loop: (A,B)
# A = main cycle partial order of all core activities before review
# B = data integration + cycle review, feeding back to A

# Core activities partial order (one big PO combining all core steps in logical flow)
# Flow:
# env_sensing (soil_testing, climate_scan) --> resource_allocation -->
# pest_management and growth_cycle concurrent -->
# harvesting and waste_recycling concurrent -->
# community_input --> data_integration --> cycle_review

# Combine pest_management and growth_cycle concurrent
pest_and_growth = StrictPartialOrder(nodes=[pest_management, growth_cycle])  # no edges, concurrent

# Combine harvesting and waste_recycling concurrent
harvest_and_waste = StrictPartialOrder(nodes=[harvesting, waste_recycling])  # no edges, concurrent

# Now connect env_sensing --> resource_allocation --> pest_and_growth --> harvest_and_waste --> community_input
# Build main body using pm4py StrictPartialOrder and adding edges accordingly

# Main nodes:
main_nodes = [
    env_sensing,
    resource_allocation,
    pest_and_growth,
    harvest_and_waste,
    community_input,
]
main_po = StrictPartialOrder(nodes=main_nodes)

# Adding edges to main partial order
main_po.order.add_edge(env_sensing, resource_allocation)
main_po.order.add_edge(resource_allocation, pest_and_growth)
main_po.order.add_edge(pest_and_growth, harvest_and_waste)
main_po.order.add_edge(harvest_and_waste, community_input)


# B part in the loop: data_integration_po and cycle_review
# cycle_review after data_integration already modeled
# Compose B as partial order with data_integration_po and cycle_review done (cycle_review is last node)

B = StrictPartialOrder(nodes=[data_integration_po, cycle_review])
B.order.add_edge(data_integration_po, cycle_review)

# Add control flow loop: LOOP(main_po, B)
root = OperatorPOWL(operator=Operator.LOOP, children=[main_po, B])