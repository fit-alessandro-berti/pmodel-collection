# Generated from: 2c0b4f1d-d001-42a6-b876-bba7d7e09dae.json
# Description: This process describes the establishment of an urban rooftop farm on a commercial building. It involves site evaluation, structural assessments, and securing permits to ensure safety compliance. After soil and environmental testing, a modular planting system is designed and installed. Specialized irrigation and renewable energy systems are integrated to maximize sustainability. Continuous monitoring with IoT sensors ensures optimal growth conditions. The process includes community engagement for educational workshops and local market distribution planning, creating a self-sustaining urban agriculture ecosystem that promotes green spaces and local food production in dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Load_Check = Transition(label='Load Check')
Permit_Apply = Transition(label='Permit Apply')
Soil_Sample = Transition(label='Soil Sample')
Enviro_Test = Transition(label='Enviro Test')
System_Design = Transition(label='System Design')
Module_Build = Transition(label='Module Build')
Irrigation_Setup = Transition(label='Irrigation Setup')
Solar_Install = Transition(label='Solar Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Analyze = Transition(label='Data Analyze')
Workshop_Plan = Transition(label='Workshop Plan')
Market_Setup = Transition(label='Market Setup')
Harvest_Cycle = Transition(label='Harvest Cycle')
Waste_Manage = Transition(label='Waste Manage')
Community_Meet = Transition(label='Community Meet')

# 1) Initial evaluation phase: Site Survey -> Load Check -> Permit Apply (strict order)
initial_eval = StrictPartialOrder(nodes=[Site_Survey, Load_Check, Permit_Apply])
initial_eval.order.add_edge(Site_Survey, Load_Check)
initial_eval.order.add_edge(Load_Check, Permit_Apply)

# 2) Testing phase: Soil Sample and Enviro Test are concurrent (no order)
testing = StrictPartialOrder(nodes=[Soil_Sample, Enviro_Test])
# no edges, concurrent

# 3) Design and Build: System Design -> Module Build (strict order)
design_build = StrictPartialOrder(nodes=[System_Design, Module_Build])
design_build.order.add_edge(System_Design, Module_Build)

# 4) Setup specialized systems: Irrigation Setup and Solar Install in parallel (concurrent)
setup_systems = StrictPartialOrder(nodes=[Irrigation_Setup, Solar_Install])
# no edges

# 5) Sensor deployment and growth monitor + data analyze pipeline (strict order):
# Sensor Deploy -> Growth Monitor -> Data Analyze
monitoring_pipeline = StrictPartialOrder(nodes=[Sensor_Deploy, Growth_Monitor, Data_Analyze])
monitoring_pipeline.order.add_edge(Sensor_Deploy, Growth_Monitor)
monitoring_pipeline.order.add_edge(Growth_Monitor, Data_Analyze)

# 6) Community engagement: Workshop Plan and Community Meet concurrent
community_engagement = StrictPartialOrder(nodes=[Workshop_Plan, Community_Meet])
# no edges

# 7) Market Setup (single activity)
market_setup = StrictPartialOrder(nodes=[Market_Setup])

# 8) Harvest and waste management cycle:
# Harvest Cycle and Waste Manage are looping cyclically to represent ongoing harvesting and waste management
# Represented as LOOP(Harvest Cycle, Waste Manage)
harvest_waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Cycle, Waste_Manage])

# Now compose the entire process partial order, reflecting the narration:

# - initial evaluation then
# - testing (concurrent Soil Sample and Enviro Test)
# - then design and build
# - then setup specialized systems
# - then sensor deployment and monitoring pipeline
# - concurrently community engagement and market setup (these two concurrent with each other, but both follow monitoring)
# - finally a looping harvest and waste management cycle running continuously

# Compose phases:

# Phase1: initial_eval -> testing -> design_build -> setup_systems -> monitoring_pipeline
phase1 = StrictPartialOrder(
    nodes=[initial_eval, testing, design_build, setup_systems, monitoring_pipeline]
)
phase1.order.add_edge(initial_eval, testing)
phase1.order.add_edge(testing, design_build)
phase1.order.add_edge(design_build, setup_systems)
phase1.order.add_edge(setup_systems, monitoring_pipeline)

# phase2: community_engagement and market_setup concurrent
phase2 = StrictPartialOrder(nodes=[community_engagement, market_setup])
# no edges for concurrency

# Compose phase1 -> phase2 with concurrency inside phase2
main_order = StrictPartialOrder(nodes=[phase1, phase2, harvest_waste_loop])
main_order.order.add_edge(phase1, phase2)
main_order.order.add_edge(phase2, harvest_waste_loop)

root = main_order