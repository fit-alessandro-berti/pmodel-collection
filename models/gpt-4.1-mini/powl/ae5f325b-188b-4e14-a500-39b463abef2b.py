# Generated from: ae5f325b-188b-4e14-a500-39b463abef2b.json
# Description: This process governs the loaning of rare artworks between international museums involving complex logistics, legal compliance, condition verification, and insurance arrangements. It begins with curator selection, followed by provenance validation and conservation assessment. Customs clearance and specialized packaging are coordinated alongside climate-controlled transport planning. Upon arrival, condition re-verification, installation setup, and security calibration occur. The process concludes with public unveiling, ongoing condition monitoring during display, and final repatriation with detailed reporting to all stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Curator_Select = Transition(label='Curator Select')
Provenance_Check = Transition(label='Provenance Check')
Condition_Assess = Transition(label='Condition Assess')
Legal_Review = Transition(label='Legal Review')
Insurance_Setup = Transition(label='Insurance Setup')
Packaging_Plan = Transition(label='Packaging Plan')
Customs_Clear = Transition(label='Customs Clear')
Transport_Book = Transition(label='Transport Book')
Climate_Control = Transition(label='Climate Control')
Arrival_Inspect = Transition(label='Arrival Inspect')
Install_Setup = Transition(label='Install Setup')
Security_Calibrate = Transition(label='Security Calibrate')
Public_Unveil = Transition(label='Public Unveil')
Condition_Monitor = Transition(label='Condition Monitor')
Return_Arrange = Transition(label='Return Arrange')
Final_Report = Transition(label='Final Report')


# Step 1: Curator_Select, then Provenance_Check and Condition_Assess in parallel,
# but Condition_Assess depends on Provenance_Check (Condition Assess after Provenance Check)

# So Provenance_Check --> Condition_Assess
# Both depend on Curator_Select: Curator_Select --> Provenance_Check (then --> Condition_Assess)

# Step 2: Then Legal_Review and Insurance_Setup in parallel, independent from each other,
# but both after Condition_Assess

# Step 3: Customs_Clear and Packaging_Plan in parallel, both after Legal_Review and Insurance_Setup
# So edges:
# Condition_Assess --> Legal_Review
# Condition_Assess --> Insurance_Setup
# Legal_Review --> Customs_Clear
# Insurance_Setup --> Customs_Clear (both must complete before Customs_Clear? It's partial order, so having both edges make Customs_Clear after both)
# Similarly for Packaging_Plan: after Legal_Review and Insurance_Setup
# So Legal_Review --> Packaging_Plan
# Insurance_Setup --> Packaging_Plan

# Step 4: Transport_Book and Climate_Control occur in parallel after Packaging_Plan and Customs_Clear
# So Packaging_Plan --> Transport_Book
# Customs_Clear --> Transport_Book
# Packaging_Plan --> Climate_Control
# Customs_Clear --> Climate_Control

# Step 5: Arrival_Inspect then Install_Setup then Security_Calibrate (sequential)
# All depend on Transport_Book and Climate_Control finishing (Transport_Book and Climate_Control must complete before Arrival_Inspect)

# So edges:
# Transport_Book --> Arrival_Inspect
# Climate_Control --> Arrival_Inspect
# Arrival_Inspect --> Install_Setup
# Install_Setup --> Security_Calibrate

# Step 6: Public_Unveil after Security_Calibrate

# Step 7: Condition_Monitor follows Public_Unveil

# Step 8: Return_Arrange and Final_Report in parallel after Condition_Monitor

# Summarize nodes
nodes = [
    Curator_Select,
    Provenance_Check,
    Condition_Assess,
    Legal_Review,
    Insurance_Setup,
    Packaging_Plan,
    Customs_Clear,
    Transport_Book,
    Climate_Control,
    Arrival_Inspect,
    Install_Setup,
    Security_Calibrate,
    Public_Unveil,
    Condition_Monitor,
    Return_Arrange,
    Final_Report
]

root = StrictPartialOrder(nodes=nodes)

# Add edges as per above reasoning:

# Step 1
root.order.add_edge(Curator_Select, Provenance_Check)
root.order.add_edge(Provenance_Check, Condition_Assess)

# Step 2
root.order.add_edge(Condition_Assess, Legal_Review)
root.order.add_edge(Condition_Assess, Insurance_Setup)

# Step 3
root.order.add_edge(Legal_Review, Customs_Clear)
root.order.add_edge(Insurance_Setup, Customs_Clear)
root.order.add_edge(Legal_Review, Packaging_Plan)
root.order.add_edge(Insurance_Setup, Packaging_Plan)

# Step 4
root.order.add_edge(Packaging_Plan, Transport_Book)
root.order.add_edge(Customs_Clear, Transport_Book)
root.order.add_edge(Packaging_Plan, Climate_Control)
root.order.add_edge(Customs_Clear, Climate_Control)

# Step 5
root.order.add_edge(Transport_Book, Arrival_Inspect)
root.order.add_edge(Climate_Control, Arrival_Inspect)
root.order.add_edge(Arrival_Inspect, Install_Setup)
root.order.add_edge(Install_Setup, Security_Calibrate)

# Step 6
root.order.add_edge(Security_Calibrate, Public_Unveil)

# Step 7
root.order.add_edge(Public_Unveil, Condition_Monitor)

# Step 8
root.order.add_edge(Condition_Monitor, Return_Arrange)
root.order.add_edge(Condition_Monitor, Final_Report)