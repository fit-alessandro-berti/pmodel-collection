# Generated from: 6f8afe88-f87a-4538-bbec-a60c7df2e178.json
# Description: This process outlines the intricate steps involved in authenticating antique artifacts for auction houses and private collectors. It begins with initial artifact intake and digital cataloging, followed by multi-disciplinary scientific analysis including carbon dating and metallurgical tests. Expert consultations are conducted with historians and provenance researchers to verify historical context and ownership lineage. Parallel to verification, legal compliance checks ensure no cultural heritage laws are violated. Post-validation, restoration assessment determines any necessary conservation work. The final phase involves preparing detailed certification reports, archiving findings, and coordinating secure transportation logistics to auction or display venues. This atypical yet realistic process requires tight coordination between scientists, legal experts, historians, and logistics teams to maintain artifact integrity and authenticity throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Artifact_Intake = Transition(label='Artifact Intake')
Digital_Catalog = Transition(label='Digital Catalog')

Carbon_Dating = Transition(label='Carbon Dating')
Metal_Testing = Transition(label='Metal Testing')

Expert_Consult = Transition(label='Expert Consult')
Provenance_Check = Transition(label='Provenance Check')

Legal_Review = Transition(label='Legal Review')
Heritage_Compliance = Transition(label='Heritage Compliance')

Restoration_Assess = Transition(label='Restoration Assess')
Conservation_Plan = Transition(label='Conservation Plan')

Certification_Prep = Transition(label='Certification Prep')
Report_Generation = Transition(label='Report Generation')
Findings_Archive = Transition(label='Findings Archive')

Transport_Arrange = Transition(label='Transport Arrange')
Venue_Coordination = Transition(label='Venue Coordination')

# Scientific Analysis parallel activities (carbon dating & metal testing)
scientific_analysis = StrictPartialOrder(nodes=[Carbon_Dating, Metal_Testing])
# no order edges, they run in parallel

# Expert consultations parallel activities (historian & provenance)
expert_consultations = StrictPartialOrder(nodes=[Expert_Consult, Provenance_Check])
# no order edges, run in parallel

# Legal compliance checks parallel activities
legal_checks = StrictPartialOrder(nodes=[Legal_Review, Heritage_Compliance])
# no order edges, run in parallel

# Post-validation restoration loop: (Restoration_Assess, then loop on Conservation_Plan and Restoration_Assess)
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[Restoration_Assess, Conservation_Plan])

# Final phase is sequential: Certification_Prep -> Report_Generation -> Findings_Archive -> (Transport_Arrange and Venue_Coordination in parallel)

final_parallel = StrictPartialOrder(nodes=[Transport_Arrange, Venue_Coordination])

final_phase = StrictPartialOrder(
    nodes=[Certification_Prep, Report_Generation, Findings_Archive, final_parallel]
)
final_phase.order.add_edge(Certification_Prep, Report_Generation)
final_phase.order.add_edge(Report_Generation, Findings_Archive)
final_phase.order.add_edge(Findings_Archive, final_parallel)

# Build the main partial order
root = StrictPartialOrder(
    nodes=[
        Artifact_Intake,
        Digital_Catalog,
        scientific_analysis,
        expert_consultations,
        legal_checks,
        restoration_loop,
        final_phase,
    ]
)

# Set edges according to description
# Initial step: Artifact Intake -> Digital Catalog
root.order.add_edge(Artifact_Intake, Digital_Catalog)

# Digital Catalog -> scientific_analysis (carbon & metal)
root.order.add_edge(Digital_Catalog, scientific_analysis)

# scientific_analysis -> expert_consultations and legal_checks run in parallel after scientific analysis
root.order.add_edge(scientific_analysis, expert_consultations)
root.order.add_edge(scientific_analysis, legal_checks)

# expert_consultations and legal_checks both must complete before restoration_loop
root.order.add_edge(expert_consultations, restoration_loop)
root.order.add_edge(legal_checks, restoration_loop)

# restoration_loop -> final_phase
root.order.add_edge(restoration_loop, final_phase)