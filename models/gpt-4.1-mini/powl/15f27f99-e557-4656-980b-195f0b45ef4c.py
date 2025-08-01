# Generated from: 15f27f99-e557-4656-980b-195f0b45ef4c.json
# Description: This process entails the comprehensive evaluation and authentication of ancient artifacts submitted by collectors or museums. It begins with initial intake and documentation, followed by non-invasive imaging techniques and material composition analysis. Specialists conduct provenance research and cross-reference historical databases. Parallel steps include microscopic surface examination and radiocarbon dating. Findings are compiled into a detailed report, which undergoes peer review. Contingent on results, legal and ethical clearance is secured before final certification. The process concludes with secure archival of all data and returning the artifact under controlled conditions, ensuring traceability and authenticity verification for future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition, OperatorPOWL
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Intake_Review = Transition(label='Intake Review')
Image_Capture = Transition(label='Image Capture')
Material_Test = Transition(label='Material Test')
Provenance_Check = Transition(label='Provenance Check')
Database_Search = Transition(label='Database Search')
Surface_Scan = Transition(label='Surface Scan')
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Report_Draft = Transition(label='Report Draft')
Peer_Review = Transition(label='Peer Review')
Legal_Clear = Transition(label='Legal Clear')
Ethical_Audit = Transition(label='Ethical Audit')
Certify_Artifact = Transition(label='Certify Artifact')
Archive_Data = Transition(label='Archive Data')
Return_Artifact = Transition(label='Return Artifact')
Traceability_Log = Transition(label='Traceability Log')

# Parallel steps after initial intake:
# - Image Capture and Material Test happen after Intake Review, no order between them (concurrent)
# Research tasks Provenance_Check and Database_Search run in sequence (Provenance then DB search)
# Also, Surface_Scan and Radiocarbon_Date run in parallel after research tasks

# Create partial order for research steps: Provenance_Check --> Database_Search
research = StrictPartialOrder(nodes=[Provenance_Check, Database_Search])
research.order.add_edge(Provenance_Check, Database_Search)

# Create partial order for parallel research extensions: Surface_Scan and Radiocarbon_Date concurrent after research
# So research tasks then both Surface_Scan and Radiocarbon_Date happen in parallel
research_and_parallel = StrictPartialOrder(
    nodes=[research, Surface_Scan, Radiocarbon_Date]
)
research_and_parallel.order.add_edge(research, Surface_Scan)
research_and_parallel.order.add_edge(research, Radiocarbon_Date)

# Next: Report Draft after Image Capture, Material Test, Surface_Scan and Radiocarbon_Date
# So they must all complete before Report Draft
# To express this, we create partial order with nodes: Image_Capture, Material_Test, research_and_parallel, Report_Draft
pre_report_nodes = [Image_Capture, Material_Test, research_and_parallel, Report_Draft]
pre_report = StrictPartialOrder(nodes=pre_report_nodes)
pre_report.order.add_edge(Image_Capture, Report_Draft)
pre_report.order.add_edge(Material_Test, Report_Draft)
pre_report.order.add_edge(research_and_parallel, Report_Draft)

# Peer Review happens after Report Draft
# Then Legal Clear and Ethical Audit run in parallel
legal_ethic = StrictPartialOrder(nodes=[Legal_Clear, Ethical_Audit])
# no order between Legal_Clear and Ethical_Audit -> concurrent

# Certify Artifact after both Legal Clear and Ethical Audit
certify_phase = StrictPartialOrder(
    nodes=[legal_ethic, Certify_Artifact]
)
certify_phase.order.add_edge(legal_ethic, Certify_Artifact)

# After certification: Archive Data and Return Artifact in sequence
# with Traceability Log concurrent with Return Artifact
arch_return = StrictPartialOrder(
    nodes=[Archive_Data, Return_Artifact, Traceability_Log]
)
arch_return.order.add_edge(Archive_Data, Return_Artifact)
# Traceability_Log is concurrent to Return_Artifact (no edge)

# Build the overall process partial order
# Starting with Intake Review
# Intake Review --> Image Capture and Material Test
# So create PO for Intake Review --> pre_report nodes except Report Draft (Image_Capture, Material_Test, research_and_parallel)
start = StrictPartialOrder(
    nodes=[Intake_Review, Image_Capture, Material_Test, research_and_parallel]
)
start.order.add_edge(Intake_Review, Image_Capture)
start.order.add_edge(Intake_Review, Material_Test)
start.order.add_edge(Intake_Review, research_and_parallel)

# Now overall nodes: start, Report_Draft, Peer_Review, certify_phase, arch_return
# Edges:
# start --> Report_Draft
# Report_Draft --> Peer_Review
# Peer_Review --> certify_phase
# certify_phase --> arch_return

overall_nodes = [
    start, 
    Report_Draft, 
    Peer_Review, 
    certify_phase, 
    arch_return
]
root = StrictPartialOrder(nodes=overall_nodes)
root.order.add_edge(start, Report_Draft)
root.order.add_edge(Report_Draft, Peer_Review)
root.order.add_edge(Peer_Review, certify_phase)
root.order.add_edge(certify_phase, arch_return)