# Generated from: 0bbc9ec8-bff6-4cb9-baa9-118ec6ec2f40.json
# Description: This process governs the end-to-end authentication and provenance verification of rare cultural artifacts prior to acquisition by private collectors or museums. It involves multidisciplinary collaboration between historians, forensic analysts, digital archivists, and blockchain experts. The workflow begins with preliminary artifact inspection followed by material composition analysis using advanced spectrometry. Concurrently, provenance records are digitized and cross-verified against global registries. Forensic handwriting and signature analysis are performed if applicable. A secure blockchain entry is created to immutably log all findings and ownership history. Finally, a multi-signature digital certificate is issued to confirm authenticity, ensuring traceability and minimizing risks of forgery and illegal trade in cultural heritage items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Basic activities
initial = Transition(label='Initial Inspection')
material_scan = Transition(label='Material Scan')
spectrometry = Transition(label='Spectrometry Test')
provenance_check = Transition(label='Provenance Check')
digital_archive = Transition(label='Digital Archive')
registry_search = Transition(label='Registry Search')
cross_reference = Transition(label='Cross Reference')
handwriting = Transition(label='Handwriting Review')
signature = Transition(label='Signature Verify')
blockchain_entry = Transition(label='Blockchain Entry')
ownership_log = Transition(label='Ownership Log')
expert_panel = Transition(label='Expert Panel')
risk_analysis = Transition(label='Risk Analysis')
certificate_issue = Transition(label='Certificate Issue')
final_approval = Transition(label='Final Approval')

# Material analysis subprocess: Material Scan -> Spectrometry Test
material_PO = StrictPartialOrder(nodes=[material_scan, spectrometry])
material_PO.order.add_edge(material_scan, spectrometry)

# Provenance subprocess:
#   Provenance Check
#      |-> Digital Archive
#      |-> Registry Search -> Cross Reference
provenance_PO = StrictPartialOrder(nodes=[provenance_check,
                                          digital_archive,
                                          registry_search,
                                          cross_reference])
provenance_PO.order.add_edge(provenance_check, digital_archive)
provenance_PO.order.add_edge(provenance_check, registry_search)
provenance_PO.order.add_edge(registry_search, cross_reference)
provenance_PO.order.add_edge(digital_archive, cross_reference)

# Optional handwriting/signature analysis: either do both in sequence or skip
seq_hand = StrictPartialOrder(nodes=[handwriting, signature])
seq_hand.order.add_edge(handwriting, signature)
skip = SilentTransition()
handwriting_xor = OperatorPOWL(operator=Operator.XOR, children=[seq_hand, skip])

# Blockchain logging subprocess: Entry -> Ownership Log
blockchain_PO = StrictPartialOrder(nodes=[blockchain_entry, ownership_log])
blockchain_PO.order.add_edge(blockchain_entry, ownership_log)

# Expert review loop: run Expert Panel -> Risk Analysis, repeat until okay
loop_body = StrictPartialOrder(nodes=[expert_panel, risk_analysis])
loop_body.order.add_edge(expert_panel, risk_analysis)
tau = SilentTransition()
review_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, tau])

# Final issuance: Certificate Issue -> Final Approval
final_seq = StrictPartialOrder(nodes=[certificate_issue, final_approval])
final_seq.order.add_edge(certificate_issue, final_approval)

# Root model: put everything in order
root = StrictPartialOrder(nodes=[initial,
                                 material_PO,
                                 provenance_PO,
                                 handwriting_xor,
                                 blockchain_PO,
                                 review_loop,
                                 final_seq])
root.order.add_edge(initial, material_PO)
root.order.add_edge(initial, provenance_PO)
root.order.add_edge(material_PO, handwriting_xor)
root.order.add_edge(provenance_PO, handwriting_xor)
root.order.add_edge(handwriting_xor, blockchain_PO)
root.order.add_edge(blockchain_PO, review_loop)
root.order.add_edge(review_loop, final_seq)