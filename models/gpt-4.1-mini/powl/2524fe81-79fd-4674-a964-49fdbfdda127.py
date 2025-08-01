# Generated from: 2524fe81-79fd-4674-a964-49fdbfdda127.json
# Description: This process outlines the end-to-end setup and execution of custom drone delivery services for specialized clients. It involves initial client consultation to understand unique delivery requirements, drone customization to meet payload and navigation needs, regulatory compliance checks including airspace permissions, route optimization considering weather and obstacles, pilot training and certification for specific drone models, real-time monitoring during delivery, incident response planning, and post-delivery analytics. The process ensures tailored solutions while maintaining safety, efficiency, and regulatory adherence in an emerging logistics sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Client_Consult = Transition(label='Client Consult')
Needs_Analysis = Transition(label='Needs Analysis')
Drone_Design = Transition(label='Drone Design')
Payload_Setup = Transition(label='Payload Setup')
Software_Config = Transition(label='Software Config')
Regulatory_Check = Transition(label='Regulatory Check')
Route_Planning = Transition(label='Route Planning')
Pilot_Assign = Transition(label='Pilot Assign')
Training_Session = Transition(label='Training Session')
Preflight_Check = Transition(label='Preflight Check')
Launch_Drone = Transition(label='Launch Drone')
Monitor_Flight = Transition(label='Monitor Flight')
Incident_Response = Transition(label='Incident Response')
Delivery_Confirm = Transition(label='Delivery Confirm')
Data_Review = Transition(label='Data Review')
Maintenance_Log = Transition(label='Maintenance Log')

# Define partial orders describing the process flow

# Initial client consultation and analysis order
initial_PO = StrictPartialOrder(nodes=[Client_Consult, Needs_Analysis])
initial_PO.order.add_edge(Client_Consult, Needs_Analysis)

# Drone customization: design and then two partial concurrent setups (Payload and Software)
customization_PO = StrictPartialOrder(nodes=[Drone_Design, Payload_Setup, Software_Config])
customization_PO.order.add_edge(Drone_Design, Payload_Setup)
customization_PO.order.add_edge(Drone_Design, Software_Config)

# Regulatory and route planning sequential
reg_route_PO = StrictPartialOrder(nodes=[Regulatory_Check, Route_Planning])
reg_route_PO.order.add_edge(Regulatory_Check, Route_Planning)

# Pilot related: assign pilot, training, preflight check sequential
pilot_PO = StrictPartialOrder(nodes=[Pilot_Assign, Training_Session, Preflight_Check])
pilot_PO.order.add_edge(Pilot_Assign, Training_Session)
pilot_PO.order.add_edge(Training_Session, Preflight_Check)

# Drone launch and monitor, with incident response parallel
monitor_PO = StrictPartialOrder(nodes=[Launch_Drone, Monitor_Flight, Incident_Response])
monitor_PO.order.add_edge(Launch_Drone, Monitor_Flight)
# Incident_Response can happen anytime after Launch_Drone (concurrent with Monitor_Flight)
monitor_PO.order.add_edge(Launch_Drone, Incident_Response)

# Delivery confirm, data review, maintenance log sequential
final_PO = StrictPartialOrder(nodes=[Delivery_Confirm, Data_Review, Maintenance_Log])
final_PO.order.add_edge(Delivery_Confirm, Data_Review)
final_PO.order.add_edge(Data_Review, Maintenance_Log)

# Combine the major phases in order:
# initial_PO -> customization_PO -> reg_route_PO -> pilot_PO -> monitor_PO -> final_PO
root = StrictPartialOrder(nodes=[
    initial_PO, 
    customization_PO, 
    reg_route_PO, 
    pilot_PO, 
    monitor_PO, 
    final_PO
])
root.order.add_edge(initial_PO, customization_PO)
root.order.add_edge(customization_PO, reg_route_PO)
root.order.add_edge(reg_route_PO, pilot_PO)
root.order.add_edge(pilot_PO, monitor_PO)
root.order.add_edge(monitor_PO, final_PO)