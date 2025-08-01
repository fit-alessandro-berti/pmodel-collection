# Generated from: 81b65346-785a-45c2-9b40-0d99786551e3.json
# Description: This process outlines the comprehensive steps required to establish an urban drone delivery service that integrates regulatory compliance, advanced route optimization, dynamic weather adaptation, and stakeholder coordination. It begins with market analysis and regulatory approval, followed by drone fleet customization and software integration. The process includes real-time data monitoring, emergency protocol design, and customer feedback integration to ensure efficient, safe, and scalable operations within complex urban environments. Continuous improvement cycles based on performance metrics and evolving technology standards complete the framework.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Market_Survey = Transition(label='Market Survey')
Regulatory_Check = Transition(label='Regulatory Check')
Fleet_Design = Transition(label='Fleet Design')
Route_Mapping = Transition(label='Route Mapping')
Software_Setup = Transition(label='Software Setup')
Pilot_Training = Transition(label='Pilot Training')
Safety_Audit = Transition(label='Safety Audit')
Weather_Sync = Transition(label='Weather Sync')
Test_Flights = Transition(label='Test Flights')
Emergency_Drill = Transition(label='Emergency Drill')
Customer_Onboard = Transition(label='Customer Onboard')
Data_Tracking = Transition(label='Data Tracking')
Feedback_Loop = Transition(label='Feedback Loop')
Performance_Review = Transition(label='Performance Review')
Tech_Upgrade = Transition(label='Tech Upgrade')
Stakeholder_Meet = Transition(label='Stakeholder Meet')

# First phase: Market Survey --> Regulatory Check
phase1 = StrictPartialOrder(nodes=[Market_Survey, Regulatory_Check])
phase1.order.add_edge(Market_Survey, Regulatory_Check)

# Second phase: Fleet Design and Route Mapping are concurrent, both precede Software Setup
fleet_route = StrictPartialOrder(nodes=[Fleet_Design, Route_Mapping])
# No edges, so concurrent

phase2 = StrictPartialOrder(nodes=[fleet_route, Software_Setup])
# Since fleet_route is a PO, we need to keep nodes flat in POWL StrictPartialOrder
# So better to model fleet_route nodes + Software_Setup flat with edges:
phase2 = StrictPartialOrder(
    nodes=[Fleet_Design, Route_Mapping, Software_Setup]
)
phase2.order.add_edge(Fleet_Design, Software_Setup)
phase2.order.add_edge(Route_Mapping, Software_Setup)
# Fleet_Design and Route_Mapping concurrent (no order between them)

# Third phase: Pilot Training --> Safety Audit
phase3 = StrictPartialOrder(nodes=[Pilot_Training, Safety_Audit])
phase3.order.add_edge(Pilot_Training, Safety_Audit)

# Fourth phase: Weather Sync --> Test Flights
phase4 = StrictPartialOrder(nodes=[Weather_Sync, Test_Flights])
phase4.order.add_edge(Weather_Sync, Test_Flights)

# Fifth phase: Emergency Drill and Customer Onboard parallel
phase5 = StrictPartialOrder(nodes=[Emergency_Drill, Customer_Onboard])
# no order, concurrent

# Sixth phase: Data Tracking concurrent with Feedback Loop (which is in a loop with Performance Review and Tech Upgrade)
# Define loop: loop body A = Performance Review ; loop B = Tech Upgrade + Feedback Loop sequence
# But as per definition: * (A, B): execute A, then choose exit or execute B then A again

# We interpret loop as:
# Loop node: * (Performance Review, Sequence(Tech Upgrade --> Feedback Loop))
feedback_seq = StrictPartialOrder(nodes=[Tech_Upgrade, Feedback_Loop])
feedback_seq.order.add_edge(Tech_Upgrade, Feedback_Loop)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Performance_Review, feedback_seq])

# Stakeholder Meet is after loop and after concurrent Data Tracking and loop

# Data Tracking concurrent with Stakeholder Meet and loop

# Organize final assembly as partial orders

# Phase 6: Data Tracking and Stakeholder Meet concurrent with loop
phase6 = StrictPartialOrder(nodes=[Data_Tracking, Stakeholder_Meet, loop])
# No ordering among Data Tracking, Stakeholder Meet, and loop, so all concurrent

# Now assemble the whole process by defining ordering between phases:

# Phase1 (Market Survey --> Regulatory Check) --> Phase2 (Fleet Design & Route Mapping --> Software Setup)
root1 = StrictPartialOrder(nodes=[phase1, phase2])
root1.order.add_edge(phase1, phase2)

# Phase2 --> Phase3 (Pilot Training --> Safety Audit)
root2 = StrictPartialOrder(nodes=[root1, phase3])
root2.order.add_edge(root1, phase3)

# Phase3 --> Phase4 (Weather Sync --> Test Flights)
root3 = StrictPartialOrder(nodes=[root2, phase4])
root3.order.add_edge(root2, phase4)

# Phase4 --> Phase5 (Emergency Drill and Customer Onboard concurrent)
root4 = StrictPartialOrder(nodes=[root3, phase5])
root4.order.add_edge(root3, phase5)

# Phase5 --> Phase6 (Data Tracking, Stakeholder Meet, loop)
root = StrictPartialOrder(nodes=[root4, phase6])
root.order.add_edge(root4, phase6)