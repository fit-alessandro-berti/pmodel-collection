# Generated from: 552e4f15-100d-45e7-9da1-51306badc3a5.json
# Description: This process outlines the comprehensive steps involved in authenticating rare historical artifacts for a museum acquisition. It begins with preliminary research and provenance verification, followed by scientific testing and expert consultations. The workflow includes digital documentation, condition assessment, fraud detection using advanced imaging, and legal clearance. Each stage involves collaborative decision-making between historians, scientists, and legal advisors to ensure the artifact's authenticity and legal compliance before final acquisition and exhibition planning. The process concludes with secure storage and periodic re-evaluation to maintain integrity over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
initial_research      = Transition(label='Initial Research')
provenance_check      = Transition(label='Provenance Check')
material_testing      = Transition(label='Material Testing')
expert_review         = Transition(label='Expert Review')
digital_catalog       = Transition(label='Digital Catalog')
condition_report      = Transition(label='Condition Report')
imaging_scan          = Transition(label='Imaging Scan')
fraud_analysis        = Transition(label='Fraud Analysis')
legal_review          = Transition(label='Legal Review')
stakeholder_meeting   = Transition(label='Stakeholder Meeting')
acquisition_approval  = Transition(label='Acquisition Approval')
secure_storage        = Transition(label='Secure Storage')
exhibit_planning      = Transition(label='Exhibit Planning')
reevaluation          = Transition(label='Reevaluation')
documentation_update  = Transition(label='Documentation Update')

# Define the loop for periodic re-evaluation and documentation update
# LOOP(children=[A, B]) means: do A, then either exit or do B and repeat A again.
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[reevaluation, documentation_update]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    initial_research,
    provenance_check,
    material_testing,
    expert_review,
    digital_catalog,
    condition_report,
    imaging_scan,
    fraud_analysis,
    legal_review,
    stakeholder_meeting,
    acquisition_approval,
    secure_storage,
    exhibit_planning,
    loop
])

# Add the control-flow order edges
o = root.order
o.add_edge(initial_research, provenance_check)
o.add_edge(provenance_check, material_testing)
o.add_edge(material_testing, expert_review)
o.add_edge(expert_review, digital_catalog)
o.add_edge(digital_catalog, condition_report)
o.add_edge(condition_report, imaging_scan)
o.add_edge(imaging_scan, fraud_analysis)
o.add_edge(fraud_analysis, legal_review)
o.add_edge(legal_review, stakeholder_meeting)
o.add_edge(stakeholder_meeting, acquisition_approval)

# After approval, storage and exhibit planning can proceed in parallel
o.add_edge(acquisition_approval, secure_storage)
o.add_edge(acquisition_approval, exhibit_planning)

# After both storage and planning, enter the periodic re-evaluation loop
o.add_edge(secure_storage, loop)
o.add_edge(exhibit_planning, loop)