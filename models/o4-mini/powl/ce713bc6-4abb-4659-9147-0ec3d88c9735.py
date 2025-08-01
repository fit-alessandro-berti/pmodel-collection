# Generated from: ce713bc6-4abb-4659-9147-0ec3d88c9735.json
# Description: This process involves the detailed verification and authentication of cultural artifacts before acquisition by a museum or private collector. It includes multi-layered historical research, forensic material analysis, legal ownership tracing, and ethical compliance checks. The process ensures that each artifact's origin is accurately documented to prevent illicit trade and to uphold provenance integrity. Activities consist of interdisciplinary collaboration among historians, scientists, legal experts, and conservators, culminating in a comprehensive provenance report and approval for acquisition or repatriation decisions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
initial_inquiry       = Transition(label='Initial Inquiry')
document_review       = Transition(label='Document Review')
historical_research   = Transition(label='Historical Research')
material_sampling     = Transition(label='Material Sampling')
forensic_testing      = Transition(label='Forensic Testing')
ownership_audit       = Transition(label='Ownership Audit')
legal_verification    = Transition(label='Legal Verification')
ethical_screening     = Transition(label='Ethical Screening')
expert_consultation   = Transition(label='Expert Consultation')
cultural_assessment   = Transition(label='Cultural Assessment')
condition_survey      = Transition(label='Condition Survey')
risk_analysis         = Transition(label='Risk Analysis')
provenance_mapping    = Transition(label='Provenance Mapping')
report_compilation    = Transition(label='Report Compilation')
acquisition_approval  = Transition(label='Acquisition Approval')
repatriation_review   = Transition(label='Repatriation Review')
archival_storage      = Transition(label='Archival Storage')

# Exclusive choice between acquisition and repatriation
approval_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[acquisition_approval, repatriation_review]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    initial_inquiry,
    document_review,
    historical_research,
    material_sampling,
    forensic_testing,
    ownership_audit,
    legal_verification,
    ethical_screening,
    expert_consultation,
    cultural_assessment,
    condition_survey,
    risk_analysis,
    provenance_mapping,
    report_compilation,
    approval_choice,
    archival_storage
])

# Define the control-flow dependencies
o = root.order
o.add_edge(initial_inquiry,     document_review)
o.add_edge(document_review,     historical_research)
o.add_edge(historical_research, material_sampling)
o.add_edge(material_sampling,   forensic_testing)
o.add_edge(forensic_testing,    ownership_audit)
o.add_edge(ownership_audit,     legal_verification)
o.add_edge(legal_verification,  ethical_screening)

# After ethical screening, three concurrent expert activities:
o.add_edge(ethical_screening,   expert_consultation)
o.add_edge(ethical_screening,   cultural_assessment)
o.add_edge(ethical_screening,   condition_survey)

# Consolidate the expert inputs into risk analysis
o.add_edge(expert_consultation,  risk_analysis)
o.add_edge(cultural_assessment,  risk_analysis)
o.add_edge(condition_survey,     risk_analysis)

# Final sequencing through mapping and reporting
o.add_edge(risk_analysis,       provenance_mapping)
o.add_edge(provenance_mapping,  report_compilation)

# Decision and archival storage
o.add_edge(report_compilation,  approval_choice)
o.add_edge(approval_choice,     archival_storage)