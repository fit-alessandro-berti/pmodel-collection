# Generated from: 4cd4be3a-04e0-446a-9455-e20a5076841f.json
# Description: This process outlines the complex workflow involved in authenticating historical artifacts for museum acquisitions. It begins with preliminary provenance research, followed by detailed scientific analysis including radiocarbon dating and material composition studies. Expert consultations from historians, chemists, and art conservators occur in parallel to evaluate authenticity claims. Findings are compiled into a comprehensive report, which then undergoes peer review. Legal verification ensures compliance with international cultural heritage laws. Finally, a risk assessment on acquisition impact is performed before the artifact is approved for purchase. Post-acquisition protocols include secure transport arrangements and documentation archiving to maintain chain of custody and future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
provenance_check = Transition(label='Provenance Check')
initial_survey = Transition(label='Initial Survey')
radiocarbon_test = Transition(label='Radiocarbon Test')
material_analysis = Transition(label='Material Analysis')
expert_review = Transition(label='Expert Review')
historical_consult = Transition(label='Historical Consult')
art_conservator = Transition(label='Art Conservator')
report_draft = Transition(label='Report Draft')
peer_review = Transition(label='Peer Review')
legal_verify = Transition(label='Legal Verify')
compliance_check = Transition(label='Compliance Check')
risk_assess = Transition(label='Risk Assess')
acquisition_vote = Transition(label='Acquisition Vote')
transport_plan = Transition(label='Transport Plan')
documentation = Transition(label='Documentation')

# Step 1 and 2: Provenance Check then Initial Survey
step1_2 = StrictPartialOrder(nodes=[provenance_check, initial_survey])
step1_2.order.add_edge(provenance_check, initial_survey)

# Step 3: Scientific analysis includes Radiocarbon Test and Material Analysis concurrently
scientific_analysis = StrictPartialOrder(nodes=[radiocarbon_test, material_analysis])
# no order edges, concurrent

# Step 4: Expert consultations happen in parallel: Historical Consult, Art Conservator, and Expert Review
# Expert Review depends on both Historical Consult and Art Conservator (assuming so to merge parallel)
expert_consult_parallel = StrictPartialOrder(nodes=[historical_consult, art_conservator, expert_review])
expert_consult_parallel.order.add_edge(historical_consult, expert_review)
expert_consult_parallel.order.add_edge(art_conservator, expert_review)

# Step 5: Compile findings into Report Draft
report_compile = StrictPartialOrder(
    nodes=[report_draft],
)

# Step 6: Peer Review
peer_review_node = StrictPartialOrder(
    nodes=[peer_review],
)

# Step 7 and 8: Legal Verify followed by Compliance Check
legal_compliance = StrictPartialOrder(nodes=[legal_verify, compliance_check])
legal_compliance.order.add_edge(legal_verify, compliance_check)

# Step 9: Risk Assessment
risk_assess_node = StrictPartialOrder(nodes=[risk_assess])

# Step 10: Acquisition Vote
acquisition_vote_node = StrictPartialOrder(nodes=[acquisition_vote])

# Step 11: Post acquisition protocols in parallel: Transport Plan and Documentation
post_acquisition = StrictPartialOrder(nodes=[transport_plan, documentation])
# concurrent, no order edges

# Now connect all steps respecting order:
# Provenance Check -> Initial Survey -> Scientific Analysis
partial1 = StrictPartialOrder(nodes=[step1_2, scientific_analysis])
partial1.order.add_edge(step1_2, scientific_analysis)

# Scientific Analysis -> Expert Consultations
partial2 = StrictPartialOrder(nodes=[partial1, expert_consult_parallel])
partial2.order.add_edge(partial1, expert_consult_parallel)

# Expert Consultations -> Report Draft
partial3 = StrictPartialOrder(nodes=[partial2, report_compile])
partial3.order.add_edge(partial2, report_compile)

# Report Draft -> Peer Review
partial4 = StrictPartialOrder(nodes=[partial3, peer_review_node])
partial4.order.add_edge(partial3, peer_review_node)

# Peer Review -> Legal Verify and Compliance Check
partial5 = StrictPartialOrder(nodes=[partial4, legal_compliance])
partial5.order.add_edge(partial4, legal_compliance)

# Legal Compliance -> Risk Assessment -> Acquisition Vote
partial6 = StrictPartialOrder(nodes=[partial5, risk_assess_node, acquisition_vote_node])
partial6.order.add_edge(partial5, risk_assess_node)
partial6.order.add_edge(risk_assess_node, acquisition_vote_node)

# Acquisition Vote -> Post Acquisition parallel tasks
root = StrictPartialOrder(nodes=[partial6, post_acquisition])
root.order.add_edge(partial6, post_acquisition)