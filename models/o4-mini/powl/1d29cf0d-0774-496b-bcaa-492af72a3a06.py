# Generated from: 1d29cf0d-0774-496b-bcaa-492af72a3a06.json
# Description: This process involves the comprehensive examination and validation of historical artifacts to confirm their authenticity prior to acquisition or exhibition. It integrates multidisciplinary expert assessments, including material analysis, provenance research, and forensic imaging. The workflow starts with artifact reception and initial inspection, followed by detailed scientific testing such as radiocarbon dating and pigment analysis. Parallel provenance verification is conducted through archival research and expert interviews. Subsequent steps include digital 3D modeling and comparative stylistic evaluation against known authentic items. Findings are consolidated into a comprehensive report reviewed by a certification board. The final stage involves secure cataloging and preparation for either acquisition, loan, or public display with strict condition monitoring protocols. Throughout the process, data integrity and chain of custody are rigorously maintained to ensure credibility and traceability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_reception   = Transition(label='Artifact Reception')
initial_inspection   = Transition(label='Initial Inspection')
material_sampling    = Transition(label='Material Sampling')
radiocarbon_test     = Transition(label='Radiocarbon Test')
pigment_analysis     = Transition(label='Pigment Analysis')
provenance_check     = Transition(label='Provenance Check')
archive_research     = Transition(label='Archive Research')
expert_interviews    = Transition(label='Expert Interviews')
forensic_imaging     = Transition(label='Forensic Imaging')
modeling             = Transition(label='3D Modeling')
stylistic_review     = Transition(label='Stylistic Review')
report_compilation   = Transition(label='Report Compilation')
certification_review = Transition(label='Certification Review')
catalog_entry        = Transition(label='Catalog Entry')
condition_prep       = Transition(label='Condition Prep')
data_verification    = Transition(label='Data Verification')
chain_custody        = Transition(label='Chain Custody')

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_reception,
    initial_inspection,
    material_sampling,
    radiocarbon_test,
    pigment_analysis,
    provenance_check,
    archive_research,
    expert_interviews,
    forensic_imaging,
    modeling,
    stylistic_review,
    report_compilation,
    certification_review,
    catalog_entry,
    condition_prep,
    data_verification,
    chain_custody
])

# Sequence: reception -> inspection
root.order.add_edge(artifact_reception, initial_inspection)

# After inspection: three parallel branches
root.order.add_edge(initial_inspection, material_sampling)
root.order.add_edge(initial_inspection, provenance_check)
root.order.add_edge(initial_inspection, forensic_imaging)

# Material analysis branch
root.order.add_edge(material_sampling, radiocarbon_test)
root.order.add_edge(material_sampling, pigment_analysis)

# Provenance branch
root.order.add_edge(provenance_check, archive_research)
root.order.add_edge(provenance_check, expert_interviews)

# Join branches into 3D modeling
root.order.add_edge(radiocarbon_test, modeling)
root.order.add_edge(pigment_analysis, modeling)
root.order.add_edge(archive_research, modeling)
root.order.add_edge(expert_interviews, modeling)
root.order.add_edge(forensic_imaging, modeling)

# Downstream sequence
root.order.add_edge(modeling, stylistic_review)
root.order.add_edge(stylistic_review, report_compilation)
root.order.add_edge(report_compilation, certification_review)
root.order.add_edge(certification_review, catalog_entry)
root.order.add_edge(catalog_entry, condition_prep)

# 'Data Verification' and 'Chain Custody' remain concurrent throughout (no edges)