# Generated from: bfef7b84-0706-4623-a695-f621bf2cdfad.json
# Description: This process involves the comprehensive verification of an artifact's authenticity and provenance by integrating multidisciplinary data sources including historical records, material analysis, expert consultations, and blockchain-based ownership tracking. The workflow begins with initial artifact intake, followed by surface and chemical scans, detailed archival research, cross-referencing ownership documents, and consulting domain specialists. Next, the process incorporates advanced AI pattern recognition to detect anomalies, compares findings with known databases, and consolidates all evidence into a digital dossier. Finally, the process concludes with certification issuance or rejection, ensuring traceability and transparency in the art and antiquities market while mitigating forgery risks and enhancing collector confidence.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition, OperatorPOWL
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_intake   = Transition(label='Artifact Intake')
surface_scan      = Transition(label='Surface Scan')
material_analysis = Transition(label='Material Analysis')
historical_search = Transition(label='Historical Search')
document_check    = Transition(label='Document Check')
ownership_trace   = Transition(label='Ownership Trace')
provenance_map    = Transition(label='Provenance Map')
expert_review     = Transition(label='Expert Review')
ai_pattern        = Transition(label='AI Pattern')
anomaly_flag      = Transition(label='Anomaly Flag')
database_match    = Transition(label='Database Match')
evidence_compile  = Transition(label='Evidence Compile')
digital_dossier   = Transition(label='Digital Dossier')
certification     = Transition(label='Certification')
final_report      = Transition(label='Final Report')

# Define the exclusive choice between certification and final report
end_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[certification, final_report]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    surface_scan,
    material_analysis,
    historical_search,
    document_check,
    ownership_trace,
    provenance_map,
    expert_review,
    ai_pattern,
    anomaly_flag,
    database_match,
    evidence_compile,
    digital_dossier,
    end_choice
])

# Define the control-flow (partial order) edges
root.order.add_edge(artifact_intake, surface_scan)
root.order.add_edge(artifact_intake, material_analysis)

root.order.add_edge(surface_scan, historical_search)
root.order.add_edge(material_analysis, historical_search)

root.order.add_edge(historical_search, document_check)
root.order.add_edge(document_check, ownership_trace)
root.order.add_edge(ownership_trace, provenance_map)
root.order.add_edge(provenance_map, expert_review)

root.order.add_edge(expert_review, ai_pattern)
root.order.add_edge(ai_pattern, anomaly_flag)
root.order.add_edge(anomaly_flag, database_match)

root.order.add_edge(database_match, evidence_compile)
root.order.add_edge(evidence_compile, digital_dossier)

root.order.add_edge(digital_dossier, end_choice)