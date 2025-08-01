# Generated from: e55b647a-caea-4357-b293-11c638134e4e.json
# Description: This process outlines the complex workflow involved in authenticating historical artifacts prior to acquisition or exhibition. It integrates multidisciplinary expertise including provenance research, material analysis, and legal verification. The process begins with initial artifact intake and proceeds through detailed scientific testing, expert consultations, and provenance tracing in international archives. Concurrently, legal teams verify ownership rights and ensure compliance with cultural heritage laws. Throughout the process, findings are documented and reviewed iteratively to build a comprehensive authentication report. Final approval requires consensus from multiple departments before the artifact is accepted or rejected. This atypical yet realistic process is critical to prevent fraud, protect cultural heritage, and maintain institutional credibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ai      = Transition(label='Artifact Intake')
pc      = Transition(label='Provenance Check')
ms      = Transition(label='Material Sampling')
st      = Transition(label='Scientific Test')
er      = Transition(label='Expert Review')
archive = Transition(label='Archive Search')
lv      = Transition(label='Legal Verify')
oc      = Transition(label='Ownership Confirm')
ca      = Transition(label='Compliance Audit')
dd      = Transition(label='Data Documentation')
ir      = Transition(label='Interim Report')
dr      = Transition(label='Department Review')
cm      = Transition(label='Consensus Meeting')
fa      = Transition(label='Final Approval')
ar      = Transition(label='Artifact Release')
skip    = SilentTransition()

# 1) Research & analysis branch: Provenance → ArchiveSearch → ExpertReview
#                              Sampling → ScientificTest → ExpertReview
research_po = StrictPartialOrder(nodes=[pc, archive, ms, st, er])
research_po.order.add_edge(pc,      archive)
research_po.order.add_edge(ms,      st)
research_po.order.add_edge(archive, er)
research_po.order.add_edge(st,      er)

# 2) Legal verification branch: LegalVerify → OwnershipConfirm → ComplianceAudit
legal_po = StrictPartialOrder(nodes=[lv, oc, ca])
legal_po.order.add_edge(lv, oc)
legal_po.order.add_edge(oc, ca)

# 3) Iterative documentation & interim‐reporting loop
doc_review = StrictPartialOrder(nodes=[dd, ir, dr])
doc_review.order.add_edge(dd, ir)
doc_review.order.add_edge(ir, dr)
loop = OperatorPOWL(operator=Operator.LOOP, children=[doc_review, skip])

# 4) Final consensus & release
# Build the overall partial‐order model
root = StrictPartialOrder(nodes=[ai, research_po, legal_po, loop, cm, fa, ar])

# After intake, research & legal proceed in parallel
root.order.add_edge(ai, research_po)
root.order.add_edge(ai, legal_po)

# Join both branches into the documentation loop
root.order.add_edge(research_po, loop)
root.order.add_edge(legal_po,    loop)

# After loop, go to consensus, final approval, then release
root.order.add_edge(loop, cm)
root.order.add_edge(cm,   fa)
root.order.add_edge(fa,   ar)