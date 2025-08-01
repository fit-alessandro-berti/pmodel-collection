# Generated from: 04f613a5-3ae2-455f-8a74-09c0fee36d56.json
# Description: This process outlines the establishment of a sustainable urban rooftop farming system in a densely populated city. It involves site assessment, structural analysis, soil testing, and environmental impact evaluation. The process also includes sourcing organic seeds, installing hydroponic systems, setting up automated irrigation, and integrating renewable energy sources. Additionally, it covers obtaining necessary permits, training local staff, implementing pest control measures, monitoring crop health with IoT sensors, harvesting schedules, and establishing distribution channels to local markets. The goal is to create a resilient, eco-friendly food production method within urban spaces that maximizes yield while minimizing environmental footprint and resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Check = Transition(label='Load Check')
Soil_Test = Transition(label='Soil Test')
Impact_Eval = Transition(label='Impact Eval')
Permit_Apply = Transition(label='Permit Apply')
Seed_Source = Transition(label='Seed Source')
Hydro_Install = Transition(label='Hydro Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Energy_Connect = Transition(label='Energy Connect')
Staff_Train = Transition(label='Staff Train')
Pest_Control = Transition(label='Pest Control')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Monitor = Transition(label='Crop Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Market_Link = Transition(label='Market Link')

# Establish the structural assessment partial order (Site Survey, Load Check, Soil Test, Impact Eval)
# Concurrency allowed except that Site Survey precedes others
structural_assessment = StrictPartialOrder(nodes=[Site_Survey, Load_Check, Soil_Test, Impact_Eval])
structural_assessment.order.add_edge(Site_Survey, Load_Check)
structural_assessment.order.add_edge(Site_Survey, Soil_Test)
structural_assessment.order.add_edge(Site_Survey, Impact_Eval)

# Setup partial order: Seed sourcing and hydroponics installations and irrigation and energy connect concurrently after structural assessment
setup_nodes = [Seed_Source, Hydro_Install, Irrigation_Setup, Energy_Connect]
setup = StrictPartialOrder(nodes=setup_nodes)
# All start only after structural_assessment ends, so partial order linking structural_assessment --> setup
# This will be expressed at root level edges

# Training and permits may happen concurrently, but must start after site and setup are done
training_and_permits = StrictPartialOrder(nodes=[Permit_Apply, Staff_Train])

# Pest control, sensor deploy, crop monitor form a chain of dependencies:
# Pest Control -> Sensor Deploy -> Crop Monitor
crop_monitoring = StrictPartialOrder(nodes=[Pest_Control, Sensor_Deploy, Crop_Monitor])
crop_monitoring.order.add_edge(Pest_Control, Sensor_Deploy)
crop_monitoring.order.add_edge(Sensor_Deploy, Crop_Monitor)

# Harvest plan and market link: harvest precedes market link
harvest_distribution = StrictPartialOrder(nodes=[Harvest_Plan, Market_Link])
harvest_distribution.order.add_edge(Harvest_Plan, Market_Link)

# Partial order that groups pest control chain and harvest/distribution in sequence:
# Crop monitoring must happen before harvest plan
# pest control -> sensor -> crop monitor -> harvest plan -> market link
monitor_and_harvest = StrictPartialOrder(
    nodes=[crop_monitoring, harvest_distribution]
)
# Add edges to connect crop_monitoring -> harvest_distribution
monitor_and_harvest.order.add_edge(crop_monitoring, harvest_distribution)

# Compose the overall root partial order
# The top-level order:
# structural_assessment -> setup
# structural_assessment -> training_and_permits
# setup -> training_and_permits
# training_and_permits -> monitor_and_harvest

root = StrictPartialOrder(
    nodes=[
        structural_assessment,
        setup,
        training_and_permits,
        monitor_and_harvest,
    ]
)
root.order.add_edge(structural_assessment, setup)
root.order.add_edge(structural_assessment, training_and_permits)
root.order.add_edge(setup, training_and_permits)
root.order.add_edge(training_and_permits, monitor_and_harvest)