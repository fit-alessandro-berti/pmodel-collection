# Generated from: 8a7ec494-47d6-4209-a0b7-b341c12d124d.json
# Description: This process involves the detailed verification and authentication of rare cultural artifacts acquired from private collectors before integration into a museum's permanent collection. It includes provenance research, chemical composition analysis, expert consultation, legal clearance, and digital archiving. Each step ensures the artifact's authenticity, legal ownership, and preservation readiness. The process also entails coordinating with international agencies for cross-border compliance, preparing detailed reports, and managing secure transportation logistics. Finally, the artifact is digitally cataloged with 3D imaging and metadata tagging for future research and public accessibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
prov_check       = Transition(label='Provenance Check')
cross_db         = Transition(label='Crosscheck Database')
mat_test         = Transition(label='Material Testing')
restoration      = Transition(label='Restoration Plan')
expert_review    = Transition(label='Expert Review')
cond_report      = Transition(label='Condition Report')
legal_clearance  = Transition(label='Legal Clearance')
customs_filing   = Transition(label='Customs Filing')
insurance_setup  = Transition(label='Insurance Setup')
transport_book   = Transition(label='Transport Booking')
security_audit   = Transition(label='Security Audit')
stakeholder_brief= Transition(label='Stakeholder Brief')
digital_scan     = Transition(label='Digital Scan')
metadata_tag     = Transition(label='Metadata Tagging')
archive_upload   = Transition(label='Archive Upload')

# Loop: if material testing reveals issues, perform restoration then re-test
loop_test = OperatorPOWL(operator=Operator.LOOP, children=[mat_test, restoration])

# Assemble the partial order
root = StrictPartialOrder(nodes=[
    prov_check, cross_db, loop_test, expert_review, cond_report,
    legal_clearance, customs_filing, insurance_setup,
    transport_book, security_audit, stakeholder_brief,
    digital_scan, metadata_tag, archive_upload
])

# Define ordering constraints
root.order.add_edge(prov_check, cross_db)
root.order.add_edge(cross_db, loop_test)
root.order.add_edge(loop_test, expert_review)
root.order.add_edge(expert_review, cond_report)
root.order.add_edge(loop_test, cond_report)
root.order.add_edge(cond_report, legal_clearance)
root.order.add_edge(legal_clearance, customs_filing)
root.order.add_edge(legal_clearance, insurance_setup)
root.order.add_edge(customs_filing, transport_book)
root.order.add_edge(insurance_setup, transport_book)
root.order.add_edge(transport_book, security_audit)
root.order.add_edge(security_audit, stakeholder_brief)
root.order.add_edge(stakeholder_brief, digital_scan)
root.order.add_edge(digital_scan, metadata_tag)
root.order.add_edge(metadata_tag, archive_upload)