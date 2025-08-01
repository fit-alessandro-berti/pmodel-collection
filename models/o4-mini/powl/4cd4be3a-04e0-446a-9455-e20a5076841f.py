# Generated from: 4cd4be3a-04e0-446a-9455-e20a5076841f.json
# Description: This process outlines the complex workflow involved in authenticating historical artifacts for museum acquisitions. It begins with preliminary provenance research, followed by detailed scientific analysis including radiocarbon dating and material composition studies. Expert consultations from historians, chemists, and art conservators occur in parallel to evaluate authenticity claims. Findings are compiled into a comprehensive report, which then undergoes peer review. Legal verification ensures compliance with international cultural heritage laws. Finally, a risk assessment on acquisition impact is performed before the artifact is approved for purchase. Post-acquisition protocols include secure transport arrangements and documentation archiving to maintain chain of custody and future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
provenance_check = Transition(label='Provenance Check')
initial_survey   = Transition(label='Initial Survey')
radiocarbon_test = Transition(label='Radiocarbon Test')
material_analysis= Transition(label='Material Analysis')
historical_consult = Transition(label='Historical Consult')
art_conservator    = Transition(label='Art Conservator')
expert_review      = Transition(label='Expert Review')
report_draft       = Transition(label='Report Draft')
peer_review        = Transition(label='Peer Review')
legal_verify       = Transition(label='Legal Verify')
compliance_check   = Transition(label='Compliance Check')
risk_assess        = Transition(label='Risk Assess')
acquisition_vote   = Transition(label='Acquisition Vote')
transport_plan     = Transition(label='Transport Plan')
documentation      = Transition(label='Documentation')

# Create the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    provenance_check,
    initial_survey,
    radiocarbon_test,
    material_analysis,
    historical_consult,
    art_conservator,
    expert_review,
    report_draft,
    peer_review,
    legal_verify,
    compliance_check,
    risk_assess,
    acquisition_vote,
    transport_plan,
    documentation
])

# Sequence: Provenance Check -> Initial Survey
root.order.add_edge(provenance_check, initial_survey)

# After Initial Survey, radiocarbon & material analysis in parallel
root.order.add_edge(initial_survey, radiocarbon_test)
root.order.add_edge(initial_survey, material_analysis)

# After both scientific tests, expert consultations in parallel
for test in [radiocarbon_test, material_analysis]:
    root.order.add_edge(test, historical_consult)
    root.order.add_edge(test, art_conservator)
    root.order.add_edge(test, expert_review)

# After all consultations, compile the report
for consult in [historical_consult, art_conservator, expert_review]:
    root.order.add_edge(consult, report_draft)

# Peer review, then legal & compliance, then risk assessment, then vote
root.order.add_edge(report_draft, peer_review)
root.order.add_edge(peer_review, legal_verify)
root.order.add_edge(legal_verify, compliance_check)
root.order.add_edge(compliance_check, risk_assess)
root.order.add_edge(risk_assess, acquisition_vote)

# Post-acquisition: transport plan and documentation in parallel
root.order.add_edge(acquisition_vote, transport_plan)
root.order.add_edge(acquisition_vote, documentation)