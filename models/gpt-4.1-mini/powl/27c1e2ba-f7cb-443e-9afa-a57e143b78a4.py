# Generated from: 27c1e2ba-f7cb-443e-9afa-a57e143b78a4.json
# Description: This process outlines the comprehensive steps involved in authenticating antique artifacts for auction purposes. It begins with initial artifact intake and provenance verification, followed by detailed material composition analysis using advanced spectroscopy. Next, stylistic and historical context assessments are performed by experts, complemented by digital imaging and 3D scanning to detect restoration or forgery. The process involves cross-referencing with global artifact databases and consultation with external historians. A risk evaluation is then conducted to estimate potential market value and legal considerations. Finally, a certification report is generated and archived, with recommendations for preservation or restoration. The process ensures thorough validation to maintain auction integrity and client trust.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
ProvenanceCheck = Transition(label='Provenance Check')

MaterialScan = Transition(label='Material Scan')
SpectralAnalysis = Transition(label='Spectral Analysis')

StylisticReview = Transition(label='Stylistic Review')
HistoricalContext = Transition(label='Historical Context')

Imaging3D = Transition(label='3D Imaging')
ForgeryDetection = Transition(label='Forgery Detection')

DatabaseCrossref = Transition(label='Database Crossref')
ExpertConsult = Transition(label='Expert Consult')

RiskAssessment = Transition(label='Risk Assessment')
ValueEstimation = Transition(label='Value Estimation')
LegalReview = Transition(label='Legal Review')

ReportGeneration = Transition(label='Report Generation')
ArchiveStorage = Transition(label='Archive Storage')

PreservationPlan = Transition(label='Preservation Plan')

# Structure the model

# Initial part: Artifact Intake --> Provenance Check
start_po = StrictPartialOrder(nodes=[ArtifactIntake, ProvenanceCheck])
start_po.order.add_edge(ArtifactIntake, ProvenanceCheck)

# Material analysis parallel tasks: Material Scan and Spectral Analysis
material_analysis = StrictPartialOrder(nodes=[MaterialScan, SpectralAnalysis])
# These occur concurrently, no order edges

# Stylistic and historical assessments in parallel: Stylistic Review and Historical Context
style_history = StrictPartialOrder(nodes=[StylisticReview, HistoricalContext])
# no order edges (concurrent)

# Imaging and forgery detection in parallel: 3D Imaging and Forgery Detection
imaging_forgery = StrictPartialOrder(nodes=[Imaging3D, ForgeryDetection])
# concurrent

# Cross-referencing and expert consultation concurrently
crossref_expert = StrictPartialOrder(nodes=[DatabaseCrossref, ExpertConsult])
# concurrent

# Combine the four above groups (material_analysis, style_history, imaging_forgery, crossref_expert) in parallel
middle_parallel = StrictPartialOrder(
    nodes=[material_analysis, style_history, imaging_forgery, crossref_expert]
)
# no ordering edges, fully concurrent groups

# Risk evaluation sequence: Risk Assessment --> Value Estimation --> Legal Review
risk_po = StrictPartialOrder(nodes=[RiskAssessment, ValueEstimation, LegalReview])
risk_po.order.add_edge(RiskAssessment, ValueEstimation)
risk_po.order.add_edge(ValueEstimation, LegalReview)

# Final sequence: Report Generation --> Archive Storage --> Preservation Plan
final_po = StrictPartialOrder(nodes=[ReportGeneration, ArchiveStorage, PreservationPlan])
final_po.order.add_edge(ReportGeneration, ArchiveStorage)
final_po.order.add_edge(ArchiveStorage, PreservationPlan)

# Combine all parts in order:
# start_po --> middle_parallel --> risk_po --> final_po

root = StrictPartialOrder(
    nodes=[start_po, middle_parallel, risk_po, final_po]
)
root.order.add_edge(start_po, middle_parallel)
root.order.add_edge(middle_parallel, risk_po)
root.order.add_edge(risk_po, final_po)