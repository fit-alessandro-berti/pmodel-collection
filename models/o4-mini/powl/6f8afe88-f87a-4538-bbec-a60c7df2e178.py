# Generated from: 6f8afe88-f87a-4538-bbec-a60c7df2e178.json
# Description: This process outlines the intricate steps involved in authenticating antique artifacts for auction houses and private collectors. It begins with initial artifact intake and digital cataloging, followed by multi-disciplinary scientific analysis including carbon dating and metallurgical tests. Expert consultations are conducted with historians and provenance researchers to verify historical context and ownership lineage. Parallel to verification, legal compliance checks ensure no cultural heritage laws are violated. Post-validation, restoration assessment determines any necessary conservation work. The final phase involves preparing detailed certification reports, archiving findings, and coordinating secure transportation logistics to auction or display venues. This atypical yet realistic process requires tight coordination between scientists, legal experts, historians, and logistics teams to maintain artifact integrity and authenticity throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
artifact_intake      = Transition(label='Artifact Intake')
digital_catalog      = Transition(label='Digital Catalog')
carbon_dating        = Transition(label='Carbon Dating')
metal_testing        = Transition(label='Metal Testing')
expert_consult       = Transition(label='Expert Consult')
provenance_check     = Transition(label='Provenance Check')
legal_review         = Transition(label='Legal Review')
heritage_compliance  = Transition(label='Heritage Compliance')
restoration_assess   = Transition(label='Restoration Assess')
conservation_plan    = Transition(label='Conservation Plan')
certification_prep   = Transition(label='Certification Prep')
report_generation    = Transition(label='Report Generation')
findings_archive     = Transition(label='Findings Archive')
transport_arrange    = Transition(label='Transport Arrange')
venue_coordination   = Transition(label='Venue Coordination')

# Build the partially ordered workflow
root = StrictPartialOrder(
    nodes=[
        artifact_intake, digital_catalog,
        carbon_dating, metal_testing,
        expert_consult, provenance_check,
        legal_review, heritage_compliance,
        restoration_assess, conservation_plan,
        certification_prep, report_generation,
        findings_archive, transport_arrange,
        venue_coordination
    ]
)

# 1. Intake → Catalog
root.order.add_edge(artifact_intake, digital_catalog)

# 2. Scientific analysis in parallel (after catalog)
root.order.add_edge(digital_catalog, carbon_dating)
root.order.add_edge(digital_catalog, metal_testing)

# 3. Expert consultations (after both analyses)
root.order.add_edge(carbon_dating, expert_consult)
root.order.add_edge(metal_testing, expert_consult)
root.order.add_edge(carbon_dating, provenance_check)
root.order.add_edge(metal_testing, provenance_check)

# 4. Legal compliance (in parallel to expert consultations, after analyses)
root.order.add_edge(carbon_dating, legal_review)
root.order.add_edge(metal_testing, legal_review)
root.order.add_edge(legal_review, heritage_compliance)

# 5. Post-validation join → Restoration assessment
root.order.add_edge(expert_consult, restoration_assess)
root.order.add_edge(provenance_check, restoration_assess)
root.order.add_edge(heritage_compliance, restoration_assess)

# 6. Conservation planning
root.order.add_edge(restoration_assess, conservation_plan)

# 7. Certification/reporting sequence
root.order.add_edge(conservation_plan, certification_prep)
root.order.add_edge(certification_prep, report_generation)
root.order.add_edge(report_generation, findings_archive)

# 8. Logistics in parallel (after archiving findings)
root.order.add_edge(findings_archive, transport_arrange)
root.order.add_edge(findings_archive, venue_coordination)