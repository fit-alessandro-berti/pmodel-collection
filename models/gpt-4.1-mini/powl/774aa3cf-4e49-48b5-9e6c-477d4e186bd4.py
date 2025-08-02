# Generated from: 774aa3cf-4e49-48b5-9e6c-477d4e186bd4.json
# Description: This process outlines the complex steps involved in establishing an urban drone delivery network for last-mile logistics. It includes regulatory compliance checks, airspace mapping, drone fleet configuration, dynamic route optimization, real-time weather integration, package security protocols, multi-tiered stakeholder coordination, and continuous system feedback loops to ensure safe, efficient, and scalable drone deliveries within densely populated city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Regulatory_Review = Transition(label='Regulatory Review')
Airspace_Mapping = Transition(label='Airspace Mapping')
Fleet_Setup = Transition(label='Fleet Setup')
Route_Planning = Transition(label='Route Planning')
Weather_Sync = Transition(label='Weather Sync')
Security_Check = Transition(label='Security Check')
Package_Prep = Transition(label='Package Prep')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Pilot_Training = Transition(label='Pilot Training')
System_Testing = Transition(label='System Testing')
Live_Tracking = Transition(label='Live Tracking')
Data_Analysis = Transition(label='Data Analysis')
Incident_Report = Transition(label='Incident Report')
Maintenance_Ops = Transition(label='Maintenance Ops')
Feedback_Loop = Transition(label='Feedback Loop')
Compliance_Audit = Transition(label='Compliance Audit')
Capacity_Scale = Transition(label='Capacity Scale')

# Build partial orders for main process parts
# Initial regulatory and mapping setup sequence with compliance audit loop

# Compliance audit loop: * (Compliance_Audit, Regulatory_Review)
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Audit, Regulatory_Review])

# After Regulatory Review and Airspace Mapping (regulated flow, audit loop before Fleet setup)
prep_PO = StrictPartialOrder(nodes=[audit_loop, Airspace_Mapping, Fleet_Setup])
prep_PO.order.add_edge(audit_loop, Airspace_Mapping)
prep_PO.order.add_edge(Airspace_Mapping, Fleet_Setup)

# Route and weather merge partial order (concurrent)
route_weather_PO = StrictPartialOrder(nodes=[Route_Planning, Weather_Sync])

# Security and package preparation partial order
sec_pack_PO = StrictPartialOrder(nodes=[Security_Check, Package_Prep])
sec_pack_PO.order.add_edge(Security_Check, Package_Prep)

# Stakeholder meeting and pilot training parallel activities before system testing
stakeholder_pilot_PO = StrictPartialOrder(nodes=[Stakeholder_Meet, Pilot_Training])

# System testing after pilot training and stakeholder meet (both must finish)
pre_test_PO = StrictPartialOrder(nodes=[stakeholder_pilot_PO, System_Testing])
pre_test_PO.order.add_edge(stakeholder_pilot_PO, System_Testing)

# Live tracking and data analysis partial order (concurrent)
live_data_PO = StrictPartialOrder(nodes=[Live_Tracking, Data_Analysis])

# Incident report and maintenance ops partial order, maintenance loops with feedback
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Maintenance_Ops])

incident_maint_PO = StrictPartialOrder(nodes=[Incident_Report, feedback_loop])
incident_maint_PO.order.add_edge(Incident_Report, feedback_loop)

# Capacity scaling after data analysis (adaptability)
scaling_PO = Capacity_Scale

# Compose the overall process partial order
# Start: prep_PO --> (route_weather_PO & sec_pack_PO) --> pre_test_PO --> live_data_PO --> incident_maint_PO --> scaling_PO

# To combine concurrency, we nest StrictPartialOrders with concurrency by having nodes concurrent if no edges

# Combine route_weather_PO and sec_pack_PO in parallel
routes_sec_PO = StrictPartialOrder(nodes=[route_weather_PO, sec_pack_PO])

# Combine next stages sequentially prep_PO-->routes_sec_PO
seq1 = StrictPartialOrder(nodes=[prep_PO, routes_sec_PO])
seq1.order.add_edge(prep_PO, routes_sec_PO)

# Then routes_sec_PO --> pre_test_PO
seq2 = StrictPartialOrder(nodes=[seq1, pre_test_PO])
seq2.order.add_edge(seq1, pre_test_PO)

# pre_test_PO --> live_data_PO
seq3 = StrictPartialOrder(nodes=[seq2, live_data_PO])
seq3.order.add_edge(seq2, live_data_PO)

# live_data_PO --> incident_maint_PO
seq4 = StrictPartialOrder(nodes=[seq3, incident_maint_PO])
seq4.order.add_edge(seq3, incident_maint_PO)

# incident_maint_PO --> Capacity_Scale
root = StrictPartialOrder(nodes=[seq4, scaling_PO])
root.order.add_edge(seq4, scaling_PO)