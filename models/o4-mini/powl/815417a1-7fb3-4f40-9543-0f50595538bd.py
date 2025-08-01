# Generated from: 815417a1-7fb3-4f40-9543-0f50595538bd.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a constrained city environment. It includes site evaluation considering sunlight and zoning laws, modular structure design, hydroponic system integration, nutrient solution formulation, automated climate control setup, plant species selection for optimal yield, continuous monitoring and data analytics for growth optimization, pest and disease management using integrated pest management techniques, workforce training on specialized equipment, community engagement for sustainable support, logistics planning for harvest distribution, and iterative feedback loops to refine operational efficiency and sustainability in a rapidly changing urban ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey    = Transition(label='Site Survey')
zoning_review  = Transition(label='Zoning Review')
modular_design = Transition(label='Modular Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_control = Transition(label='Climate Control')
species_select = Transition(label='Species Select')
growth_monitor = Transition(label='Growth Monitor')
data_analyze   = Transition(label='Data Analyze')
pest_control   = Transition(label='Pest Control')
worker_training = Transition(label='Worker Training')
community_meet = Transition(label='Community Meet')
harvest_plan   = Transition(label='Harvest Plan')
logistics_map  = Transition(label='Logistics Map')
feedback_loop  = Transition(label='Feedback Loop')

# Build the loop body: continuous cycle of monitoring, analysis, pest control, training, community, harvest, logistics
body = StrictPartialOrder(nodes=[
    growth_monitor, 
    data_analyze, 
    pest_control, 
    worker_training, 
    community_meet, 
    harvest_plan, 
    logistics_map
])
body.order.add_edge(growth_monitor, data_analyze)
body.order.add_edge(data_analyze, pest_control)
body.order.add_edge(pest_control, worker_training)
body.order.add_edge(worker_training, community_meet)
body.order.add_edge(community_meet, harvest_plan)
body.order.add_edge(harvest_plan, logistics_map)

# Create the LOOP operator for iterative feedback
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback_loop])

# Build the top‐level partial order: from site survey through design, setup, selection, then enter the loop
root = StrictPartialOrder(nodes=[
    site_survey,
    zoning_review,
    modular_design,
    hydroponic_setup,
    nutrient_mix,
    climate_control,
    species_select,
    loop
])
root.order.add_edge(site_survey, zoning_review)
root.order.add_edge(zoning_review, modular_design)
root.order.add_edge(modular_design, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_control)
root.order.add_edge(climate_control, species_select)
root.order.add_edge(species_select, loop)