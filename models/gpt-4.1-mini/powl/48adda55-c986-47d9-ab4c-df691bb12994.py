# Generated from: 48adda55-c986-47d9-ab4c-df691bb12994.json
# Description: This process outlines the adaptive urban farming cycle designed for maximizing crop yield within limited city spaces while integrating sustainable practices and community involvement. It involves site analysis, modular bed assembly, soil enrichment through organic composting, real-time environmental monitoring with IoT devices, automated irrigation adjustment, pest control using biological agents, crop rotation planning based on historical data, community harvesting events, waste recycling into biochar, and continuous feedback loops to optimize growth parameters. The process also includes stakeholder coordination, urban policy compliance checks, and expansion feasibility studies to ensure scalability and environmental impact mitigation in dense urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Site_Survey = Transition(label='Site Survey')
Bed_Setup = Transition(label='Bed Setup')
Soil_Prep = Transition(label='Soil Prep')
Compost_Mix = Transition(label='Compost Mix')
Sensor_Install = Transition(label='Sensor Install')
Irrigation_Adjust = Transition(label='Irrigation Adjust')
Pest_Control = Transition(label='Pest Control')
Crop_Rotate = Transition(label='Crop Rotate')
Harvest_Event = Transition(label='Harvest Event')
Waste_Convert = Transition(label='Waste Convert')
Data_Analyze = Transition(label='Data Analyze')
Feedback_Loop = Transition(label='Feedback Loop')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Policy_Check = Transition(label='Policy Check')
Expansion_Plan = Transition(label='Expansion Plan')

# Define partial orders to model the process

# Initial phase: site survey, stakeholder meet and policy check can be concurrent but all before Bed Setup
init_phase = StrictPartialOrder(
    nodes=[Site_Survey, Stakeholder_Meet, Policy_Check, Bed_Setup]
)
init_phase.order.add_edge(Site_Survey, Bed_Setup)
init_phase.order.add_edge(Stakeholder_Meet, Bed_Setup)
init_phase.order.add_edge(Policy_Check, Bed_Setup)

# Prepare soil in sequence Soil Prep -> Compost Mix
soil_prep_phase = StrictPartialOrder(
    nodes=[Soil_Prep, Compost_Mix]
)
soil_prep_phase.order.add_edge(Soil_Prep, Compost_Mix)

# Setup beds concurrently with soil prep phase but only after Bed_Setup
setup_soil = StrictPartialOrder(
    nodes=[Bed_Setup, soil_prep_phase]
)
setup_soil.order.add_edge(Bed_Setup, soil_prep_phase)

# Install sensors and irrigation adjustment in sequence
sensor_irrigation = StrictPartialOrder(
    nodes=[Sensor_Install, Irrigation_Adjust]
)
sensor_irrigation.order.add_edge(Sensor_Install, Irrigation_Adjust)

# Pest control and crop rotation in sequence
pest_crop = StrictPartialOrder(
    nodes=[Pest_Control, Crop_Rotate]
)
pest_crop.order.add_edge(Pest_Control, Crop_Rotate)

# Harvest event and waste convert can be concurrent
harvest_waste = StrictPartialOrder(
    nodes=[Harvest_Event, Waste_Convert]
)
# no order since concurrent

# Data analyze followed by feedback loop, which loops back to sensor installation and adjustments
# We model the loop as (* (Data Analyze, X(Feedback Loop, skip)))
skip = SilentTransition()
feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[Feedback_Loop, skip])

# The loop: execute Data Analyze, then choose to exit or perform feedback then Data Analyze again
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Data_Analyze, feedback_xor])

# Expansion plan to be done after Stakeholder meet and Policy check, independent from the core loop
expansion_phase = StrictPartialOrder(
    nodes=[Expansion_Plan]
)
# We connect expansion after Stakeholder_Meet and Policy_Check (done early in init phase)

# Core process ordering:
# After soil prep (prepare_soil) and setup_soil are done, sensor_irrigation and pest_crop can run concurrently
core_parallel = StrictPartialOrder(nodes=[setup_soil, sensor_irrigation, pest_crop])
core_parallel.order.add_edge(setup_soil, sensor_irrigation)
core_parallel.order.add_edge(setup_soil, pest_crop)
# sensor_irrigation and pest_crop concurrent

# After core_parallel, harvest and waste concurrent activities can occur
post_harvest = StrictPartialOrder(nodes=[core_parallel, harvest_waste])
post_harvest.order.add_edge(core_parallel, harvest_waste)

# After harvest_waste, the loop of data analyze and feedback happens
post_loop = StrictPartialOrder(nodes=[post_harvest, loop_feedback])
post_loop.order.add_edge(post_harvest, loop_feedback)

# Combine init phase, post loop, and expansion which depends on stakeholder and policy (already in init phase)
# So expansion after init phase
final_root = StrictPartialOrder(
    nodes=[init_phase, post_loop, expansion_phase]
)
final_root.order.add_edge(init_phase, post_loop)
final_root.order.add_edge(init_phase, expansion_phase)

root = final_root