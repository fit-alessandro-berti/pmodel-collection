# Generated from: 98025af4-a756-49c6-b8d0-f2c8727aabc1.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm in a dense metropolitan area. It involves initial feasibility studies including structural integrity assessments, microclimate analysis, and community engagement. Following approvals, the process continues with soil-less media selection, irrigation system design, and seed sourcing tailored to urban conditions. Subsequent activities address installation of modular planters, integration of renewable energy sources, pest management using biological controls, and continuous monitoring via IoT sensors. The process concludes with crop harvesting, distribution logistics optimized for local markets, and iterative feedback collection to improve future cycles. This atypical yet practical approach merges urban planning, agriculture, and technology to enhance food security and urban greening.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Feasibility_Study = Transition(label='Feasibility Study')
Structure_Check = Transition(label='Structure Check')
Climate_Survey = Transition(label='Climate Survey')
Community_Meet = Transition(label='Community Meet')
Permit_Request = Transition(label='Permit Request')
Media_Select = Transition(label='Media Select')
Irrigation_Plan = Transition(label='Irrigation Plan')
Seed_Sourcing = Transition(label='Seed Sourcing')
Planter_Setup = Transition(label='Planter Setup')
Energy_Install = Transition(label='Energy Install')
Pest_Control = Transition(label='Pest Control')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Monitor = Transition(label='Crop Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Market_Route = Transition(label='Market Route')
Feedback_Loop = Transition(label='Feedback Loop')

# Initial feasibility studies partial order with concurrency:
# Structure_Check, Climate_Survey, Community_Meet are concurrent; all follow Feasibility_Study

# Partial order for Structure_Check, Climate_Survey, Community_Meet concurrent after Feasibility_Study
feasibility_PO = StrictPartialOrder(nodes=[Feasibility_Study, Structure_Check, Climate_Survey, Community_Meet])
feasibility_PO.order.add_edge(Feasibility_Study, Structure_Check)
feasibility_PO.order.add_edge(Feasibility_Study, Climate_Survey)
feasibility_PO.order.add_edge(Feasibility_Study, Community_Meet)

# Then Permit_Request after these three complete
permit_PO = StrictPartialOrder(
    nodes=[feasibility_PO, Permit_Request],
    # order will be added by edges from each activity in feasibility_PO "end" to Permit_Request,
    # but we can just add edges from the three concurrent tasks to Permit_Request
)

# Technically, the feasibility_PO is a node here; we need to link the leaf tasks:
# Because feasibility_PO is partial order, and nodes inside it, to model we link the three tasks to Permit_Request

# We model Permit_Request following all three concurrent feasibility activities (Structure_Check, Climate_Survey, Community_Meet)
# We'll build a PO with nodes: feasibility_PO and Permit_Request (feasibility_PO as a single node)
# But since POWL order edges go between nodes (POWL nodes can also be partial orders)
# We add the edge from feasibility_PO to Permit_Request for order

permit_PO = StrictPartialOrder(nodes=[feasibility_PO, Permit_Request])
permit_PO.order.add_edge(feasibility_PO, Permit_Request)

# Next stage: soil-less media selection, irrigation plan, seed sourcing
# These three can be concurrent after Permit_Request

media_Select = Media_Select
irrigation_Plan = Irrigation_Plan
seed_Sourcing = Seed_Sourcing

soil_PO = StrictPartialOrder(nodes=[Permit_Request, media_Select, irrigation_Plan, seed_Sourcing])
soil_PO.order.add_edge(Permit_Request, media_Select)
soil_PO.order.add_edge(Permit_Request, irrigation_Plan)
soil_PO.order.add_edge(Permit_Request, seed_Sourcing)

# Next: installation and integration: Planter_Setup, Energy_Install
# These should start after soil_PO's activities all finish

install_PO = StrictPartialOrder(nodes=[soil_PO, Planter_Setup, Energy_Install])
install_PO.order.add_edge(soil_PO, Planter_Setup)
install_PO.order.add_edge(soil_PO, Energy_Install)

# Next: Pest_Control and Sensor_Deploy can be concurrent after installation
pest_and_sensor_PO = StrictPartialOrder(nodes=[install_PO, Pest_Control, Sensor_Deploy])
pest_and_sensor_PO.order.add_edge(install_PO, Pest_Control)
pest_and_sensor_PO.order.add_edge(install_PO, Sensor_Deploy)

# Then Crop_Monitor starts after Pest_Control and Sensor_Deploy complete
monitor_PO = StrictPartialOrder(nodes=[pest_and_sensor_PO, Crop_Monitor])
monitor_PO.order.add_edge(pest_and_sensor_PO, Crop_Monitor)

# Then Harvest_Plan after Crop_Monitor
harvest_PO = StrictPartialOrder(nodes=[monitor_PO, Harvest_Plan])
harvest_PO.order.add_edge(monitor_PO, Harvest_Plan)

# Then Market_Route after Harvest_Plan
market_PO = StrictPartialOrder(nodes=[harvest_PO, Market_Route])
market_PO.order.add_edge(harvest_PO, Market_Route)

# Then Feedback_Loop after Market_Route

# We model Feedback_Loop as a LOOP with Crop_Monitor (monitor_PO part) for iterative feedback and improvement

# Build LOOP: execute Crop_Monitor and following steps, then repeat Feedback_Loop

# Feedback_Loop involves iterative feedback collection to improve future cycles
# LOOP operator: * (A,B): execute A, then choose to exit or execute B then A again

# Here A will be the cycle of Crop_Monitor to Market_Route
# B will be Feedback_Loop (the iterative feedback collection)

# Define cycle A: Crop_Monitor, Harvest_Plan, Market_Route in order (starting after Pest_Control and Sensor_Deploy)

cycle_A = StrictPartialOrder(
    nodes=[Crop_Monitor, Harvest_Plan, Market_Route]
)
cycle_A.order.add_edge(Crop_Monitor, Harvest_Plan)
cycle_A.order.add_edge(Harvest_Plan, Market_Route)

# We include Pest_Control and Sensor_Deploy and Install_PO dependencies outside loop because those are initial setup

# Define loop with cycle_A and Feedback_Loop
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[cycle_A, Feedback_Loop])

# To place loop_node after Pest_Control and Sensor_Deploy (so after pest_and_sensor_PO)

final_PO = StrictPartialOrder(nodes=[pest_and_sensor_PO, loop_node])
final_PO.order.add_edge(pest_and_sensor_PO, loop_node)

# Preceding everything: feasibility_PO -> Permit_Request -> soil_PO -> install_PO -> pest_and_sensor_PO -> loop_node (cycle with feedback)

# We've modeled feasibility_PO and permit_PO (permit_PO includes feasibility_PO and Permit_Request)
# To unify all, start from feasibility_PO, then permit_PO is just feasibility_PO + Permit_Request

# We'll chain all partial orders:

# feasibility_PO -> Permit_Request (done inside permit_PO)

# permit_PO (feasibility_PO + Permit_Request) -> soil_PO

overall_PO1 = StrictPartialOrder(nodes=[permit_PO, soil_PO])
overall_PO1.order.add_edge(permit_PO, soil_PO)

# soil_PO -> install_PO

overall_PO2 = StrictPartialOrder(nodes=[overall_PO1, install_PO])
overall_PO2.order.add_edge(overall_PO1, install_PO)

# install_PO -> pest_and_sensor_PO

overall_PO3 = StrictPartialOrder(nodes=[overall_PO2, pest_and_sensor_PO])
overall_PO3.order.add_edge(overall_PO2, pest_and_sensor_PO)

# pest_and_sensor_PO -> loop_node (already final_PO)

overall_PO4 = StrictPartialOrder(nodes=[overall_PO3, loop_node])
overall_PO4.order.add_edge(overall_PO3, loop_node)

root = overall_PO4