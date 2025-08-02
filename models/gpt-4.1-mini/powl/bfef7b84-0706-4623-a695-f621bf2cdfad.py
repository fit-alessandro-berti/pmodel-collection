# Generated from: bfef7b84-0706-4623-a695-f621bf2cdfad.json
# Description: This process involves the comprehensive verification of an artifact's authenticity and provenance by integrating multidisciplinary data sources including historical records, material analysis, expert consultations, and blockchain-based ownership tracking. The workflow begins with initial artifact intake, followed by surface and chemical scans, detailed archival research, cross-referencing ownership documents, and consulting domain specialists. Next, the process incorporates advanced AI pattern recognition to detect anomalies, compares findings with known databases, and consolidates all evidence into a digital dossier. Finally, the process concludes with certification issuance or rejection, ensuring traceability and transparency in the art and antiquities market while mitigating forgery risks and enhancing collector confidence.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions with exact labels
ArtifactIntake = Transition(label='Artifact Intake')

SurfaceScan = Transition(label='Surface Scan')
MaterialAnalysis = Transition(label='Material Analysis')

HistoricalSearch = Transition(label='Historical Search')
DocumentCheck = Transition(label='Document Check')
ExpertReview = Transition(label='Expert Review')

AIpattern = Transition(label='AI Pattern')
DatabaseMatch = Transition(label='Database Match')

OwnershipTrace = Transition(label='Ownership Trace')
ProvenanceMap = Transition(label='Provenance Map')

AnomalyFlag = Transition(label='Anomaly Flag')

EvidenceCompile = Transition(label='Evidence Compile')
DigitalDossier = Transition(label='Digital Dossier')

Certification = Transition(label='Certification')
FinalReport = Transition(label='Final Report')

# Step 2: Surface scan and Material analysis are concurrent
step2 = StrictPartialOrder(nodes=[SurfaceScan, MaterialAnalysis])

# Step 3: Historical Search, Document Check and Expert Review are concurrent
step3 = StrictPartialOrder(nodes=[HistoricalSearch, DocumentCheck, ExpertReview])

# Step 4: Ownership Trace and Provenance Map concurrent 
step4 = StrictPartialOrder(nodes=[OwnershipTrace, ProvenanceMap])

# Step 5: AI Pattern then Database Match sequentially
step5 = StrictPartialOrder(nodes=[AIpattern, DatabaseMatch])
step5.order.add_edge(AIpattern, DatabaseMatch)

# Step 6: Anomaly Flag alone

# Step 7: Evidence Compile then Digital Dossier sequentially
step7 = StrictPartialOrder(nodes=[EvidenceCompile, DigitalDossier])
step7.order.add_edge(EvidenceCompile, DigitalDossier)

# Step 8: Certification or Final Report choice (certification issuance or rejection)
choice_end = OperatorPOWL(operator=Operator.XOR, children=[Certification, FinalReport])

# Build overall partial order

# Nodes:
# 1: Artifact Intake (A)
# 2: step2 (Surface Scan & Material Analysis) (B)
# 3: step3 (Historical Search, Document Check, Expert Review) (C)
# 4: step4 (Ownership Trace & Provenance Map) (D)
# 5: step5 (AI Pattern + Database Match) (E)
# 6: Anomaly Flag (F)
# 7: step7 (Evidence Compile + Digital Dossier) (G)
# 8: choice_end (Certification or Final Report) (H)

nodes = [
    ArtifactIntake,
    step2,
    step3,
    step4,
    step5,
    AnomalyFlag,
    step7,
    choice_end
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to represent the sequence / control flow

# Artifact Intake --> step2
root.order.add_edge(ArtifactIntake, step2)

# step2 --> step3
root.order.add_edge(step2, step3)

# step3 --> step4
root.order.add_edge(step3, step4)

# step4 --> step5
root.order.add_edge(step4, step5)

# step5 --> Anomaly Flag
root.order.add_edge(step5, AnomalyFlag)

# Anomaly Flag --> step7
root.order.add_edge(AnomalyFlag, step7)

# step7 --> Certification or Final Report choice
root.order.add_edge(step7, choice_end)