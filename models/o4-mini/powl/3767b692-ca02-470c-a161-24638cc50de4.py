# Generated from: 3767b692-ca02-470c-a161-24638cc50de4.json
# Description: This process involves the complex authentication and provenance verification of historical artifacts sourced from multiple regions worldwide. The process begins with initial artifact receipt and condition logging, followed by multi-expert physical inspection, advanced material composition analysis, and cross-referencing with global artifact databases. Subsequent activities include digital 3D modeling, provenance chain reconstruction through archival research, and authentication report drafting. Additionally, the process integrates blockchain registration for provenance transparency, stakeholder consultation for disputed origins, and final certification issuance. Parallel steps encompass conservation recommendations, replication authorization, and secure artifact storage planning. The entire workflow demands coordination between historians, scientists, legal experts, and technology specialists to ensure authenticity, legal compliance, and preservation of cultural heritage assets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
artifact_receipt      = Transition(label='Artifact Receipt')
condition_log         = Transition(label='Condition Log')
expert_inspection     = Transition(label='Expert Inspection')
material_analysis     = Transition(label='Material Analysis')
database_check        = Transition(label='Database Check')
three_d_modeling      = Transition(label='3D Modeling')
provenance_research   = Transition(label='Provenance Research')
report_draft          = Transition(label='Report Draft')
blockchain_register   = Transition(label='Blockchain Register')
stakeholder_consult   = Transition(label='Stakeholder Consult')
legal_compliance      = Transition(label='Legal Compliance')
conservation_plan     = Transition(label='Conservation Plan')
replication_review    = Transition(label='Replication Review')
storage_design        = Transition(label='Storage Design')
certification_issue   = Transition(label='Certification Issue')

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_receipt,
    condition_log,
    expert_inspection,
    material_analysis,
    database_check,
    three_d_modeling,
    provenance_research,
    report_draft,
    blockchain_register,
    stakeholder_consult,
    legal_compliance,
    conservation_plan,
    replication_review,
    storage_design,
    certification_issue
])

# Define the control-flow dependencies
root.order.add_edge(artifact_receipt,   condition_log)
root.order.add_edge(condition_log,      expert_inspection)
root.order.add_edge(expert_inspection,  material_analysis)
root.order.add_edge(material_analysis,  database_check)
root.order.add_edge(database_check,     three_d_modeling)
root.order.add_edge(three_d_modeling,   provenance_research)
root.order.add_edge(provenance_research, report_draft)
root.order.add_edge(report_draft,       blockchain_register)
root.order.add_edge(blockchain_register, stakeholder_consult)

# From stakeholder consultation, branch to legal compliance and three parallel planning steps
root.order.add_edge(stakeholder_consult, legal_compliance)
root.order.add_edge(stakeholder_consult, conservation_plan)
root.order.add_edge(stakeholder_consult, replication_review)
root.order.add_edge(stakeholder_consult, storage_design)

# All branches must complete before final certification
root.order.add_edge(legal_compliance,    certification_issue)
root.order.add_edge(conservation_plan,   certification_issue)
root.order.add_edge(replication_review,  certification_issue)
root.order.add_edge(storage_design,      certification_issue)