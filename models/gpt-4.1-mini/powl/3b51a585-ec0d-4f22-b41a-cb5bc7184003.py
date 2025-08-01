# Generated from: 3b51a585-ec0d-4f22-b41a-cb5bc7184003.json
# Description: This process describes a complex, iterative cycle where a company integrates emerging technologies from unrelated industries to create novel products. It begins with trend scouting across diverse sectors, followed by cross-disciplinary ideation sessions. Prototypes are rapidly developed using minimal viable concepts, then tested in simulated environments reflecting multiple market conditions. Feedback loops incorporate insights from external experts, regulatory bodies, and potential end-users. Parallel risk assessments and resource reallocations ensure adaptability. The cycle culminates in a phased pilot launch, with continuous data-driven refinement before full-scale commercialization. This atypical approach demands agility, broad expertise, and extensive collaboration beyond conventional boundaries, enabling breakthrough innovations that disrupt traditional markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions with given labels
Trend_Scouting = Transition(label='Trend Scouting')
Idea_Fusion = Transition(label='Idea Fusion')
Rapid_Prototyping = Transition(label='Rapid Prototyping')
Simulated_Testing = Transition(label='Simulated Testing')
Expert_Review = Transition(label='Expert Review')
Risk_Analysis = Transition(label='Risk Analysis')
Resource_Shift = Transition(label='Resource Shift')
User_Feedback = Transition(label='User Feedback')
Regulatory_Check = Transition(label='Regulatory Check')
Concept_Refinement = Transition(label='Concept Refinement')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Monitoring = Transition(label='Data Monitoring')
Market_Simulation = Transition(label='Market Simulation')
Cross_Training = Transition(label='Cross Training')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Iterative_Update = Transition(label='Iterative Update')

# Parallel risk assessments and resource reallocations
risk_resource_PO = StrictPartialOrder(nodes=[Risk_Analysis, Resource_Shift])
# no edges; fully concurrent

# Feedback loop incorporating insights from Expert Review, Regulatory Check, User Feedback
feedback_PO = StrictPartialOrder(nodes=[Expert_Review, Regulatory_Check, User_Feedback])
# all concurrent feedback

# Cross Training and Stakeholder Sync are parallel preparatory activities for ideation
cross_stakeholder_PO = StrictPartialOrder(nodes=[Cross_Training, Stakeholder_Sync])

# Market Simulation is part of simulated testing market conditions (can be concurrent or sequential).
# Assume Market Simulation happens before Simulated Testing to prepare scenarios.

# Construct iteration body:
# Iteration consists of:
# - Rapid Prototyping
# - Simulated Testing (with Market Simulation concurrent)
# - Feedback from Expert Review, Regulatory Check, User Feedback (concurrent)
# - Concept Refinement
# - Iterative Update (to reflect continuous refinements)
iteration_body_PO = StrictPartialOrder(nodes=[
    Rapid_Prototyping,
    Market_Simulation,
    Simulated_Testing,
    feedback_PO,
    Concept_Refinement,
    Iterative_Update
])
# Market Simulation before Simulated Testing
iteration_body_PO.order.add_edge(Market_Simulation, Simulated_Testing)
# Rapid Prototyping before Simulated Testing
iteration_body_PO.order.add_edge(Rapid_Prototyping, Simulated_Testing)
# Simulated Testing before feedback
iteration_body_PO.order.add_edge(Simulated_Testing, feedback_PO)
# Feedback before Concept Refinement
iteration_body_PO.order.add_edge(feedback_PO, Concept_Refinement)
# Concept Refinement before Iterative Update
iteration_body_PO.order.add_edge(Concept_Refinement, Iterative_Update)

# The loop includes:
# - body: iteration_body_PO
# - condition: Iterative_Update (decides to loop or exit)
loop = OperatorPOWL(operator=Operator.LOOP, children=[iteration_body_PO, Iterative_Update])

# Top-level process order:
# Start with Trend Scouting,
# then cross-disciplinary ideation preparation (Cross Training and Stakeholder Sync in parallel),
# then Idea Fusion,
# then loop with the iteration body,
# in parallel with Risk Analysis and Resource Shift,
# finally Pilot Launch and Data Monitoring in sequence.

# Partial order for initial phase: Trend Scouting --> Cross Training & Stakeholder Sync --> Idea Fusion
init_phase_PO = StrictPartialOrder(nodes=[Trend_Scouting, cross_stakeholder_PO, Idea_Fusion])
init_phase_PO.order.add_edge(Trend_Scouting, cross_stakeholder_PO)
init_phase_PO.order.add_edge(cross_stakeholder_PO, Idea_Fusion)

# Pilot launch refinement phase: Pilot Launch --> Data Monitoring
pilot_phase_PO = StrictPartialOrder(nodes=[Pilot_Launch, Data_Monitoring])
pilot_phase_PO.order.add_edge(Pilot_Launch, Data_Monitoring)

# To integrate everything:
# Nodes at top level:
#   init_phase_PO, loop, risk_resource_PO, pilot_phase_PO
# Orders:
#   init_phase_PO --> loop
#   init_phase_PO --> risk_resource_PO
#   loop --> pilot_phase_PO
#   risk_resource_PO --> pilot_phase_PO

root = StrictPartialOrder(nodes=[init_phase_PO, loop, risk_resource_PO, pilot_phase_PO])
root.order.add_edge(init_phase_PO, loop)
root.order.add_edge(init_phase_PO, risk_resource_PO)
root.order.add_edge(loop, pilot_phase_PO)
root.order.add_edge(risk_resource_PO, pilot_phase_PO)