# Generated from: 2107561f-77cf-4c8f-bfa5-4a05bc072194.json
# Description: This process outlines the detailed steps involved in authenticating historical artifacts for museums and private collectors. It begins with preliminary provenance research and physical inspection, followed by advanced scientific analysis such as isotope dating and material composition tests. Experts then cross-reference findings with historical records and consult with specialized historians. The artifact undergoes condition assessment, restoration feasibility study, and ethical clearance review. Documentation is compiled into a comprehensive report, which is then verified by a peer review panel. Finally, authentication certification is issued, and the artifact is logged into a centralized registry for future reference and insurance purposes. Throughout the process, secure chain-of-custody protocols and confidentiality agreements are strictly maintained to ensure integrity and trustworthiness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Provenance_Check = Transition(label='Provenance Check')
Visual_Inspect = Transition(label='Visual Inspect')
Material_Test = Transition(label='Material Test')
Isotope_Dating = Transition(label='Isotope Dating')
Historical_Cross = Transition(label='Historical Cross')
Expert_Consult = Transition(label='Expert Consult')
Condition_Assess = Transition(label='Condition Assess')
Restoration_Plan = Transition(label='Restoration Plan')
Ethics_Review = Transition(label='Ethics Review')
Report_Compile = Transition(label='Report Compile')
Peer_Review = Transition(label='Peer Review')
Certify_Authentic = Transition(label='Certify Authentic')
Registry_Log = Transition(label='Registry Log')
Custody_Secure = Transition(label='Custody Secure')
Confidentiality = Transition(label='Confidentiality')

# Advanced scientific analysis partial order: Material Test and Isotope Dating concurrent
advanced_scientific_analysis = StrictPartialOrder(
    nodes=[Material_Test, Isotope_Dating],
)
# No order between these two, so they are concurrent.

# Experts cross-reference and consult sequential
experts = StrictPartialOrder(
    nodes=[Historical_Cross, Expert_Consult],
)
experts.order.add_edge(Historical_Cross, Expert_Consult)

# Condition related activities sequential
condition_activities = StrictPartialOrder(
    nodes=[Condition_Assess, Restoration_Plan, Ethics_Review],
)
condition_activities.order.add_edge(Condition_Assess, Restoration_Plan)
condition_activities.order.add_edge(Restoration_Plan, Ethics_Review)

# Documentation and verification sequential
documentation = StrictPartialOrder(
    nodes=[Report_Compile, Peer_Review],
)
documentation.order.add_edge(Report_Compile, Peer_Review)

# Certification and logging sequential
final_steps = StrictPartialOrder(
    nodes=[Certify_Authentic, Registry_Log],
)
final_steps.order.add_edge(Certify_Authentic, Registry_Log)

# Secure protocols partial order concurrent nodes Custody Secure and Confidentiality
protocols = StrictPartialOrder(
    nodes=[Custody_Secure, Confidentiality],
)
# No order edges, concurrent

# Start partial order sequence for provenance check and visual inspect
initial_checks = StrictPartialOrder(
    nodes=[Provenance_Check, Visual_Inspect],
)
initial_checks.order.add_edge(Provenance_Check, Visual_Inspect)

# Combine all main sequential parts:

# Step 1: initial_checks
# Step 2: advanced_scientific_analysis (concurrent Material Test & Isotope Dating)
# Step 3: experts (Historical Cross then Expert Consult)
# Step 4: condition_activities (Condition Assess -> Restoration Plan -> Ethics Review)
# Step 5: documentation (Report Compile -> Peer Review)
# Step 6: final_steps (Certify Authentic -> Registry Log)
# protocols (Custody Secure and Confidentiality) run concurrently with the entire process

# Build partial order of process steps (without protocols):
process_sequence_nodes = [
    initial_checks,                 # Step 1
    advanced_scientific_analysis,  # Step 2
    experts,                       # Step 3
    condition_activities,          # Step 4
    documentation,                 # Step 5
    final_steps                   # Step 6
]
process_sequence = StrictPartialOrder(
    nodes=process_sequence_nodes
)

# Add edges for sequential execution among these steps
process_sequence.order.add_edge(initial_checks, advanced_scientific_analysis)
process_sequence.order.add_edge(advanced_scientific_analysis, experts)
process_sequence.order.add_edge(experts, condition_activities)
process_sequence.order.add_edge(condition_activities, documentation)
process_sequence.order.add_edge(documentation, final_steps)

# Now combine process_sequence with protocols (concurrent)
root = StrictPartialOrder(
    nodes=[process_sequence, protocols]
)
# No order edges between protocols and process_sequence (concurrent)
