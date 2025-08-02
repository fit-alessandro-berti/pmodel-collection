# Generated from: 0bbc9ec8-bff6-4cb9-baa9-118ec6ec2f40.json
# Description: This process governs the end-to-end authentication and provenance verification of rare cultural artifacts prior to acquisition by private collectors or museums. It involves multidisciplinary collaboration between historians, forensic analysts, digital archivists, and blockchain experts. The workflow begins with preliminary artifact inspection followed by material composition analysis using advanced spectrometry. Concurrently, provenance records are digitized and cross-verified against global registries. Forensic handwriting and signature analysis are performed if applicable. A secure blockchain entry is created to immutably log all findings and ownership history. Finally, a multi-signature digital certificate is issued to confirm authenticity, ensuring traceability and minimizing risks of forgery and illegal trade in cultural heritage items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Initial_Inspection = Transition(label='Initial Inspection')
Material_Scan = Transition(label='Material Scan')

Provenance_Check = Transition(label='Provenance Check')
Registry_Search = Transition(label='Registry Search')

Handwriting_Review = Transition(label='Handwriting Review')
Signature_Verify = Transition(label='Signature Verify')

Digital_Archive = Transition(label='Digital Archive')
Spectrometry_Test = Transition(label='Spectrometry Test')
Cross_Reference = Transition(label='Cross Reference')

Blockchain_Entry = Transition(label='Blockchain Entry')
Expert_Panel = Transition(label='Expert Panel')
Risk_Analysis = Transition(label='Risk Analysis')

Certificate_Issue = Transition(label='Certificate Issue')
Ownership_Log = Transition(label='Ownership Log')
Final_Approval = Transition(label='Final Approval')

# Model concurrent provenance digitization and verification: Provenance Check and Registry Search in parallel
provenance_parallel = StrictPartialOrder(nodes=[Provenance_Check, Registry_Search])

# Forensic handwriting and signature analysis: presumably sequential if both apply, model as choice
# The description says "if applicable" for handwriting and signature analysis, which suggests choice:
hand_sig_choice = OperatorPOWL(operator=Operator.XOR, children=[Handwriting_Review, Signature_Verify])

# Secure blockchain entry logs all findings
# The blockchain entry comes after the parallel provenance scans and forensic analysis, also after Material Scan

# Digital archivists do Digital Archive, Spectrometry Test, Cross Reference
digital_archive_po = StrictPartialOrder(nodes=[Digital_Archive, Spectrometry_Test, Cross_Reference])
digital_archive_po.order.add_edge(Digital_Archive, Spectrometry_Test)
digital_archive_po.order.add_edge(Digital_Archive, Cross_Reference)

# Expert panel and risk analysis likely after blockchain entry
expert_risk_po = StrictPartialOrder(nodes=[Expert_Panel, Risk_Analysis])
# Assume they run in parallel (no order edge)

# Ownership log presumably after expert panel and risk analysis
# Final approval after ownership log and certificate issue
certificate_and_ownership = StrictPartialOrder(nodes=[Certificate_Issue, Ownership_Log])
certificate_and_ownership.order.add_edge(Certificate_Issue, Ownership_Log)

# Final approval last
final_po = StrictPartialOrder(nodes=[certificate_and_ownership, Final_Approval])
final_po.order.add_edge(certificate_and_ownership, Final_Approval)

# Now start constructing full PO with order edges

# Initial Inspection --> Material Scan
# Material Scan --> provenance_parallel and digital_archive_po run in parallel
# provenance_parallel --> hand_sig_choice
# hand_sig_choice and digital_archive_po run in parallel before blockchain entry
# blockchain entry --> expert_risk_po --> certificate_and_ownership --> final approval

root = StrictPartialOrder(nodes=[
    Initial_Inspection,
    Material_Scan,
    provenance_parallel,
    hand_sig_choice,
    digital_archive_po,
    Blockchain_Entry,
    expert_risk_po,
    certificate_and_ownership,
    final_po  # final_po wraps final approval after certificate_and_ownership
])

# Add partial order edges

# Initial inspection --> Material scan
root.order.add_edge(Initial_Inspection, Material_Scan)

# Material scan --> provenance_parallel and digital_archive_po
root.order.add_edge(Material_Scan, provenance_parallel)
root.order.add_edge(Material_Scan, digital_archive_po)

# provenance_parallel --> hand_sig_choice
root.order.add_edge(provenance_parallel, hand_sig_choice)

# hand_sig_choice and digital_archive_po --> blockchain entry
root.order.add_edge(hand_sig_choice, Blockchain_Entry)
root.order.add_edge(digital_archive_po, Blockchain_Entry)

# blockchain entry --> expert_risk_po
root.order.add_edge(Blockchain_Entry, expert_risk_po)

# expert_risk_po --> certificate_and_ownership
root.order.add_edge(expert_risk_po, certificate_and_ownership)

# certificate_and_ownership --> final approval (final_po includes final approval, so we link certificate_and_ownership to final_po)
root.order.add_edge(certificate_and_ownership, final_po)