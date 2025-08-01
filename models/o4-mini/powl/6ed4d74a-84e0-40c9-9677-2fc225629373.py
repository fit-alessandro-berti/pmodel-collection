# Generated from: 6ed4d74a-84e0-40c9-9677-2fc225629373.json
# Description: This process outlines the complex steps involved in launching an urban rooftop farming initiative that integrates sustainable agriculture with smart city technology. It includes site assessment, regulatory compliance, sensor installation for microclimate monitoring, soil enhancement using biochar, seed selection tailored for urban environments, automated irrigation setup, pest management through integrated biological controls, community engagement for local support, harvesting logistics optimized for limited space, waste composting, data analysis for yield optimization, and continuous improvement cycles driven by sensor feedback. The goal is to create a self-sustaining, scalable urban farm that contributes to food security and environmental benefits while leveraging IoT and community involvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all the atomic activities
site_survey       = Transition(label='Site Survey')
permit_review     = Transition(label='Permit Review')
sensor_setup      = Transition(label='Sensor Setup')
soil_testing      = Transition(label='Soil Testing')
biochar_mix       = Transition(label='Biochar Mix')
irrigation_install= Transition(label='Irrigation Install')
seed_selection    = Transition(label='Seed Selection')
planting_phase    = Transition(label='Planting Phase')
pest_control      = Transition(label='Pest Control')
community_meet    = Transition(label='Community Meet')
harvest_plan      = Transition(label='Harvest Plan')
waste_compost     = Transition(label='Waste Compost')

# Transitions inside the continuous‐improvement loop
growth_monitor    = Transition(label='Growth Monitor')
data_upload       = Transition(label='Data Upload')
yield_analysis    = Transition(label='Yield Analysis')
feedback_loop     = Transition(label='Feedback Loop')

# Build the internal sequence of the loop: Growth Monitor -> Data Upload -> Yield Analysis
seq_loop = StrictPartialOrder(
    nodes=[growth_monitor, data_upload, yield_analysis]
)
seq_loop.order.add_edge(growth_monitor, data_upload)
seq_loop.order.add_edge(data_upload, yield_analysis)

# Build the LOOP operator: do (Growth Monitor → Data Upload → Yield Analysis), 
# then either exit or perform Feedback Loop and repeat
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[seq_loop, feedback_loop]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey, permit_review, sensor_setup, soil_testing, biochar_mix,
        irrigation_install, seed_selection, planting_phase, pest_control,
        community_meet, loop, harvest_plan, waste_compost
    ]
)

# Add the ordering relations
root.order.add_edge(site_survey,       permit_review)
root.order.add_edge(permit_review,     sensor_setup)
root.order.add_edge(permit_review,     soil_testing)
root.order.add_edge(soil_testing,      biochar_mix)
root.order.add_edge(biochar_mix,       irrigation_install)
root.order.add_edge(sensor_setup,      irrigation_install)
root.order.add_edge(irrigation_install,seed_selection)
root.order.add_edge(seed_selection,    planting_phase)
root.order.add_edge(planting_phase,    pest_control)
root.order.add_edge(planting_phase,    community_meet)
root.order.add_edge(planting_phase,    loop)
root.order.add_edge(loop,              harvest_plan)
root.order.add_edge(harvest_plan,      waste_compost)