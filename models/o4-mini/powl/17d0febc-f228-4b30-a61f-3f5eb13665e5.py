# Generated from: 17d0febc-f228-4b30-a61f-3f5eb13665e5.json
# Description: This process involves the intricate authentication of rare artifacts sourced from various undisclosed locations. It begins with preliminary provenance verification, followed by multi-spectral imaging and chemical analysis. Expert consultations and comparative historical research further validate authenticity. The process ensures secure transportation, condition reporting, and final certification before cataloging and archival storage. Each step requires meticulous documentation to prevent forgery and maintain chain of custody. The complexity is heightened by interdisciplinary collaboration, evolving technologies, and legal compliance with international cultural property laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
provenance = Transition(label='Provenance Check')
imaging = Transition(label='Imaging Scan')
chemical = Transition(label='Chemical Test')
expert = Transition(label='Expert Review')
historical = Transition(label='Historical Compare')
transport = Transition(label='Transport Prep')
condition = Transition(label='Condition Report')
forgery = Transition(label='Forgery Analysis')
chain = Transition(label='Chain Verify')
certification = Transition(label='Certification')
legal_audit = Transition(label='Legal Audit')
tech_update = Transition(label='Tech Update')
final_approval = Transition(label='Final Approval')
catalog = Transition(label='Catalog Entry')
archive = Transition(label='Archival Store')

# Parallel analyses: imaging & chemical
po_analysis = StrictPartialOrder(nodes=[imaging, chemical])

# Parallel validation: expert review & historical compare
po_validation = StrictPartialOrder(nodes=[expert, historical])

# Parallel custody checks: forgery analysis & chain verification
po_custody = StrictPartialOrder(nodes=[forgery, chain])

# Loop for legal compliance and technology updates
loop_compliance = OperatorPOWL(
    operator=Operator.LOOP,
    children=[legal_audit, tech_update]
)

# Build the full partial order
root = StrictPartialOrder(nodes=[
    provenance,
    po_analysis,
    po_validation,
    transport,
    condition,
    po_custody,
    certification,
    loop_compliance,
    final_approval,
    catalog,
    archive
])

# Define the control-flow dependencies
root.order.add_edge(provenance, po_analysis)
root.order.add_edge(po_analysis, po_validation)
root.order.add_edge(po_validation, transport)
root.order.add_edge(transport, condition)
root.order.add_edge(condition, po_custody)
root.order.add_edge(po_custody, certification)
root.order.add_edge(certification, loop_compliance)
root.order.add_edge(loop_compliance, final_approval)
root.order.add_edge(final_approval, catalog)
root.order.add_edge(catalog, archive)