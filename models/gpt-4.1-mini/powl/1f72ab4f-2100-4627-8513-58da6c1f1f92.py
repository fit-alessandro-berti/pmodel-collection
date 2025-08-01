# Generated from: 1f72ab4f-2100-4627-8513-58da6c1f1f92.json
# Description: This process involves the intricate steps required to authenticate and verify the provenance of rare cultural artifacts. Beginning with initial artifact intake and preliminary condition assessment, it includes multi-layered historical research and provenance tracing through archival databases. Following this, scientific material analysis and radiocarbon dating are performed to validate period authenticity. Concurrently, expert panel reviews and comparative stylistic analysis ensure contextual accuracy. The process also incorporates digital fingerprinting and 3D scanning to create a secure, immutable record. Final stages involve legal documentation, insurance appraisal, and secure archival storage planning. This atypical but realistic process ensures thorough verification, safeguarding cultural heritage and providing confidence to collectors and institutions alike.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')

history_research = Transition(label='History Research')
provenance_trace = Transition(label='Provenance Trace')

material_testing = Transition(label='Material Testing')
radiocarbon_date = Transition(label='Radiocarbon Date')

expert_review = Transition(label='Expert Review')
stylistic_compare = Transition(label='Stylistic Compare')

digital_scan = Transition(label='Digital Scan')
fingerprinting = Transition(label='Fingerprinting')

legal_review = Transition(label='Legal Review')
insurance_appraise = Transition(label='Insurance Appraise')
archival_plan = Transition(label='Archival Plan')

record_secure = Transition(label='Record Secure')
final_approval = Transition(label='Final Approval')

# Build partial orders respecting concurrency and ordering

# Initial sequential part: Artifact Intake --> Condition Check
initial_po = StrictPartialOrder(nodes=[artifact_intake, condition_check])
initial_po.order.add_edge(artifact_intake, condition_check)

# Historical research and provenance tracing in sequence:
history_po = StrictPartialOrder(nodes=[history_research, provenance_trace])
history_po.order.add_edge(history_research, provenance_trace)

# Scientific tests in sequence:
scientific_po = StrictPartialOrder(nodes=[material_testing, radiocarbon_date])
scientific_po.order.add_edge(material_testing, radiocarbon_date)

# Expert panel review and stylistic compare run concurrently:
expert_po = StrictPartialOrder(nodes=[expert_review, stylistic_compare])
# No order edges = concurrent

# Digital fingerprinting and 3D scanning also concurrent:
digital_po = StrictPartialOrder(nodes=[digital_scan, fingerprinting])
# No order edges = concurrent

# Final legal/insurance/archival sequential:
final_docs_po = StrictPartialOrder(nodes=[legal_review, insurance_appraise, archival_plan])
final_docs_po.order.add_edge(legal_review, insurance_appraise)
final_docs_po.order.add_edge(insurance_appraise, archival_plan)

# Record secure and final approval sequential:
final_securing_po = StrictPartialOrder(nodes=[record_secure, final_approval])
final_securing_po.order.add_edge(record_secure, final_approval)

# Combine concurrency branches after provenance and scientific testing:
# The concurrency is among:
# 1) expert_po
# 2) digital_po
# 3) final_docs_po + final_securing_po sequence

# Final docs and securing are sequential, so combine them first:
final_docs_and_sec = StrictPartialOrder(
    nodes=[legal_review, insurance_appraise, archival_plan, record_secure, final_approval]
)
final_docs_and_sec.order.add_edge(legal_review, insurance_appraise)
final_docs_and_sec.order.add_edge(insurance_appraise, archival_plan)
final_docs_and_sec.order.add_edge(archival_plan, record_secure)
final_docs_and_sec.order.add_edge(record_secure, final_approval)

# Now after provenance_trace and radiocarbon_date these three run concurrently:
# Nodes: expert_review, stylistic_compare (expert_po)
#        digital_scan, fingerprinting (digital_po)
#        legal_review ... final_approval (final_docs_and_sec)

concurrent_after_scientific = StrictPartialOrder(
    nodes=[expert_review, stylistic_compare,
           digital_scan, fingerprinting,
           legal_review, insurance_appraise, archival_plan,
           record_secure, final_approval]
)
# Add edges from final_docs_and_sec:
concurrent_after_scientific.order.add_edge(legal_review, insurance_appraise)
concurrent_after_scientific.order.add_edge(insurance_appraise, archival_plan)
concurrent_after_scientific.order.add_edge(archival_plan, record_secure)
concurrent_after_scientific.order.add_edge(record_secure, final_approval)

# expert and digital nodes remain unordered with each other and with final_docs_and_sec nodes (except inside final_docs_and_sec)
# So no edges between those sets, just concurrency

# Now combine historical and scientific testing sequences followed by concurrency
# First combine history_po and scientific_po in parallel:
history_scientific = StrictPartialOrder(
    nodes=[history_research, provenance_trace,
           material_testing, radiocarbon_date]
)
history_scientific.order.add_edge(history_research, provenance_trace)
history_scientific.order.add_edge(material_testing, radiocarbon_date)
# No edges between history_po nodes and scientific_po nodes --> concurrent

# Now define the full middle part: after initial_po (artifact intake -> condition check),
# the next activities are these history_scientific first, then concurrency_after_scientific.

# So create a top-level PO with nodes:
# initial_po nodes: artifact_intake, condition_check
# history_scientific nodes: history_research, provenance_trace, material_testing, radiocarbon_date
# concurrent_after_scientific nodes: expert_review, stylistic_compare, digital_scan, fingerprinting,
#                                   legal_review, insurance_appraise, archival_plan, record_secure, final_approval

all_nodes = [
    artifact_intake, condition_check,
    history_research, provenance_trace,
    material_testing, radiocarbon_date,
    expert_review, stylistic_compare,
    digital_scan, fingerprinting,
    legal_review, insurance_appraise, archival_plan,
    record_secure, final_approval
]

root = StrictPartialOrder(nodes=all_nodes)

# Add initial ordering
root.order.add_edge(artifact_intake, condition_check)

# Condition Check precedes history_research and material_testing (both start after prelim conditions)
root.order.add_edge(condition_check, history_research)
root.order.add_edge(condition_check, material_testing)

# History research precedes provenance trace
root.order.add_edge(history_research, provenance_trace)

# Material testing precedes radiocarbon date
root.order.add_edge(material_testing, radiocarbon_date)

# Provenance trace and radiocarbon date precede all concurrency nodes (expert, digital, final docs)
for n in [expert_review, stylistic_compare,
          digital_scan, fingerprinting,
          legal_review]:
    root.order.add_edge(provenance_trace, n)
    root.order.add_edge(radiocarbon_date, n)

# Legal review precedes insurance appraisal etc inside final docs chain
root.order.add_edge(legal_review, insurance_appraise)
root.order.add_edge(insurance_appraise, archival_plan)
root.order.add_edge(archival_plan, record_secure)
root.order.add_edge(record_secure, final_approval)

# No edges between expert_review, stylistic_compare, digital_scan, fingerprinting (concurrent)

# So concurrency between these four sets:
# expert_review & stylistic_compare
# digital_scan & fingerprinting
# legal_review ... final_approval chain

# No order edges between expert/digital and final docs chains

# Final 'root' variable contains the entire modeled process