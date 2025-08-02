# Generated from: 86af993e-1edb-4002-9a03-52cf98b3d58c.json
# Description: This process facilitates the integration of emerging technologies from disparate industries into a unified innovation pipeline. It begins with trend scanning across sectors, followed by cross-functional ideation sessions to identify transferable solutions. After initial concept validation, the process moves into prototype adaptation, where technology is customized for new applications. Concurrently, regulatory and compliance checks are conducted to ensure feasibility. The next phase involves pilot deployments in controlled environments, capturing performance data and user feedback. Iterative refinement cycles address technical and operational challenges, supported by cross-industry mentorship programs. Finally, scalable rollout strategies are developed, incorporating market entry tactics and continuous improvement plans, creating a sustainable innovation ecosystem that leverages unconventional synergies for competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Trend_Scan = Transition(label='Trend Scan')
Idea_Merge = Transition(label='Idea Merge')
Concept_Vetting = Transition(label='Concept Vetting')
Prototype_Adapt = Transition(label='Prototype Adapt')
Compliance_Check = Transition(label='Compliance Check')
Pilot_Deploy = Transition(label='Pilot Deploy')
Data_Capture = Transition(label='Data Capture')
User_Feedback = Transition(label='User Feedback')
Iterate_Design = Transition(label='Iterate Design')
Mentor_Align = Transition(label='Mentor Align')
Risk_Assess = Transition(label='Risk Assess')
Market_Study = Transition(label='Market Study')
Strategy_Draft = Transition(label='Strategy Draft')
Scale_Plan = Transition(label='Scale Plan')
Launch_Sync = Transition(label='Launch Sync')
Performance_Review = Transition(label='Performance Review')

# Construct the loop: loop over (Iterate Design, Mentor Align)
# Perform Iterate_Design then choose to exit or do Mentor_Align then Iterate_Design again
iteration_loop = OperatorPOWL(operator=Operator.LOOP, children=[Iterate_Design, Mentor_Align])

# After Pilot Deploy, Data Capture and User Feedback occur concurrently,
# then iteration loop (Iterate Design + Mentor Align) happens
post_pilot_PO = StrictPartialOrder(
    nodes=[Data_Capture, User_Feedback, iteration_loop]
)
# no order edges between Data_Capture and User_Feedback -> concurrent
# both must precede iteration loop
post_pilot_PO.order.add_edge(Data_Capture, iteration_loop)
post_pilot_PO.order.add_edge(User_Feedback, iteration_loop)

# Concurrent Regulatory and Compliance nodes: Compliance Check and Risk Assess
# They both precede Pilot Deploy
compliance_PO = StrictPartialOrder(
    nodes=[Compliance_Check, Risk_Assess]
)
# no edges -> concurrent

# After concept vetting, sequence prototype adaptation and compliance checks in parallel
# prototype adapts before pilot deploy, pilot deploy after both compliance and prototype adapt
# So Concept Vetting -> Prototype Adapt and Concept Vetting -> Compliance Check+Risk Assess (concurrent)
# Then Compliance/Risk and Prototype Adapt -> Pilot Deploy

# Build the partial order for concept vetting phase
concept_phase_PO = StrictPartialOrder(
    nodes=[Concept_Vetting, Prototype_Adapt, compliance_PO, Pilot_Deploy]
)
# Concept Vetting before Prototype Adapt and compliance_PO (both)
concept_phase_PO.order.add_edge(Concept_Vetting, Prototype_Adapt)
concept_phase_PO.order.add_edge(Concept_Vetting, compliance_PO)
# compliance_PO nodes precede Pilot Deploy
concept_phase_PO.order.add_edge(compliance_PO, Pilot_Deploy)
# Prototype Adapt precedes Pilot Deploy
concept_phase_PO.order.add_edge(Prototype_Adapt, Pilot_Deploy)

# Combine post pilot deploy phase (post_pilot_PO) after Pilot Deploy
# So Pilot Deploy precedes post_pilot_PO
pilot_and_after_PO = StrictPartialOrder(
    nodes=[Pilot_Deploy, post_pilot_PO]
)
pilot_and_after_PO.order.add_edge(Pilot_Deploy, post_pilot_PO)

# After final iteration loop, sequence market study, strategy draft, scale plan, launch sync, and performance review
# with some partial orders:
# Market Study -> Strategy Draft -> Scale Plan -> Launch Sync
# Performance Review can be done concurrently after Launch Sync

final_phase_PO = StrictPartialOrder(
    nodes=[Market_Study, Strategy_Draft, Scale_Plan, Launch_Sync, Performance_Review]
)
final_phase_PO.order.add_edge(Market_Study, Strategy_Draft)
final_phase_PO.order.add_edge(Strategy_Draft, Scale_Plan)
final_phase_PO.order.add_edge(Scale_Plan, Launch_Sync)
final_phase_PO.order.add_edge(Launch_Sync, Performance_Review)

# Mentor Align can be viewed as running concurrently with final phase preparation
# Parallel between iteration loop (which includes Mentor Align) and final phase does not appear in text
# Instead, final phase happens after iterations (loop ends)

# After iteration loop finishes, perform Risk Assess, then final phase 
# But Risk Assess was done concurrently with Compliance Check earlier
# The text mentions cross-industry mentorship programs as support for iterative refinement cycles,
# so Mentor Align is inside the loop with Iterate Design already - covered.

# Transition from iteration_loop to market study phase (final phase)
# So iteration_loop precedes Market Study
final_section_PO = StrictPartialOrder(
    nodes=[iteration_loop, final_phase_PO]
)
final_section_PO.order.add_edge(iteration_loop, final_phase_PO)

# Starting phases: Trend Scan -> Idea Merge -> Concept Vetting -> concept_phase_PO -> pilot_and_after_PO -> final_section_PO
# For concept_phase_PO, pilot_and_after_PO and final_section_PO, need to ensure order connections

# Compose all phases in sequence:
# Trend Scan -> Idea Merge -> Concept Vetting -> concept_phase_PO -> pilot_and_after_PO -> final_section_PO

# Idea Merge after Trend Scan
# Concept Vetting after Idea Merge

start_PO = StrictPartialOrder(
    nodes=[Trend_Scan, Idea_Merge, Concept_Vetting]
)
start_PO.order.add_edge(Trend_Scan, Idea_Merge)
start_PO.order.add_edge(Idea_Merge, Concept_Vetting)

# Combine Start and concept_phase_PO
start_and_concept_PO = StrictPartialOrder(
    nodes=[start_PO, concept_phase_PO]
)
start_and_concept_PO.order.add_edge(start_PO, concept_phase_PO)

# Combine concept_phase_PO and pilot_and_after_PO
concept_and_pilot_PO = StrictPartialOrder(
    nodes=[start_and_concept_PO, pilot_and_after_PO]
)
concept_and_pilot_PO.order.add_edge(start_and_concept_PO, pilot_and_after_PO)

# Finally combine with final_section_PO
root = StrictPartialOrder(
    nodes=[concept_and_pilot_PO, final_section_PO]
)
root.order.add_edge(concept_and_pilot_PO, final_section_PO)