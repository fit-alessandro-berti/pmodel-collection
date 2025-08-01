# Generated from: 60bbe6af-fa6b-42df-b068-965c78b0551d.json
# Description: This process outlines the establishment of an urban drone delivery network, involving regulatory compliance, fleet acquisition, route optimization, and community engagement. It begins with legal clearance and airspace mapping, followed by drone procurement and pilot training. Next, it integrates real-time traffic data and weather analytics for dynamic route planning. The process also involves establishing secure package handling protocols, customer notification systems, and emergency response strategies. Continuous monitoring and feedback loops ensure service optimization and safety adherence, making it a complex yet efficient urban logistics solution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Legal_Clearance = Transition(label='Legal Clearance')
Airspace_Map = Transition(label='Airspace Map')
Drone_Purchase = Transition(label='Drone Purchase')
Pilot_Training = Transition(label='Pilot Training')
Route_Design = Transition(label='Route Design')
Traffic_Sync = Transition(label='Traffic Sync')
Weather_Check = Transition(label='Weather Check')
Package_Prep = Transition(label='Package Prep')
Secure_Loading = Transition(label='Secure Loading')
Customer_Alert = Transition(label='Customer Alert')
Flight_Launch = Transition(label='Flight Launch')
In_Flight_Track = Transition(label='In-Flight Track')
Delivery_Confirm = Transition(label='Delivery Confirm')
Emergency_Plan = Transition(label='Emergency Plan')
Feedback_Review = Transition(label='Feedback Review')
Fleet_Maintenance = Transition(label='Fleet Maintenance')
Data_Analysis = Transition(label='Data Analysis')

# 1) Initial partial order: Legal Clearance --> Airspace Map
init_po = StrictPartialOrder(nodes=[Legal_Clearance, Airspace_Map])
init_po.order.add_edge(Legal_Clearance, Airspace_Map)

# 2) Procurement and Training in parallel (Drone Purchase, Pilot Training)
procure_and_train = StrictPartialOrder(nodes=[Drone_Purchase, Pilot_Training])

# 3) Dynamic route planning as partial order:
# Route Design --> (Traffic Sync and Weather Check concurrent)
route_planning = StrictPartialOrder(nodes=[Route_Design, Traffic_Sync, Weather_Check])
route_planning.order.add_edge(Route_Design, Traffic_Sync)
route_planning.order.add_edge(Route_Design, Weather_Check)

# 4) Secure package handling protocols (Package Prep --> Secure Loading)
package_handling = StrictPartialOrder(nodes=[Package_Prep, Secure_Loading])
package_handling.order.add_edge(Package_Prep, Secure_Loading)

# 5) Customer notification system (Customer Alert)
# single node

# 6) Flight operations: Flight Launch --> In-Flight Track --> Delivery Confirm
flight_ops = StrictPartialOrder(nodes=[Flight_Launch, In_Flight_Track, Delivery_Confirm])
flight_ops.order.add_edge(Flight_Launch, In_Flight_Track)
flight_ops.order.add_edge(In_Flight_Track, Delivery_Confirm)

# 7) Emergency response strategy (Emergency Plan)
# single node

# 8) Continuous monitoring and feedback loops implemented as a LOOP:
# loop body A: Feedback Review
# loop body B: Fleet Maintenance and Data Analysis in parallel (partial order with no order edges)
fleet_and_data = StrictPartialOrder(nodes=[Fleet_Maintenance, Data_Analysis])
# loop is * (Feedback Review, fleet_and_data)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Review, fleet_and_data])

# Now, combine these major blocks into the overall partial order

# Group the complex concurrent sets:
# Step2 (procure_and_train), Step3(route_planning), Step4(package_handling), Customer Alert, flight_ops, Emergency Plan, loop

# Create a top-level StrictPartialOrder to connect them all

nodes = [
    init_po,                   # Legal Clearance -> Airspace Map
    procure_and_train,         # Drone Purchase, Pilot Training parallel
    route_planning,            # Route Design -> Traffic Sync & Weather Check
    package_handling,          # Package Prep -> Secure Loading
    Customer_Alert,            # Customer Alert (single)
    flight_ops,                # Flight Launch -> In-Flight Track -> Delivery Confirm
    Emergency_Plan,            # Emergency Plan (single)
    loop                      # feedback loop
]

root = StrictPartialOrder(nodes=nodes)

# Define edges for the high-level sequence implied by description:
# After Airspace Map, proceed to procurement and training
root.order.add_edge(init_po, procure_and_train)
# Then after procurement and training, do route planning
root.order.add_edge(procure_and_train, route_planning)
# Then package handling protocols
root.order.add_edge(route_planning, package_handling)
# Then customer notification
root.order.add_edge(package_handling, Customer_Alert)
# Then flight operations
root.order.add_edge(Customer_Alert, flight_ops)
# Emergency planning happens concurrently with flight ops? 
# The description is not explicit, but emergency plan logically ties with flight ops; let's add edge from flight_ops to Emergency Plan
root.order.add_edge(flight_ops, Emergency_Plan)
# Emergency plan leads to feedback loop for continuous monitoring
root.order.add_edge(Emergency_Plan, loop)