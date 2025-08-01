# Generated from: ffaa5781-9487-4807-b144-bc3bb26f149b.json
# Description: This process involves the comprehensive verification and authentication of historical artifacts prior to acquisition or display in a museum. It begins with initial provenance research followed by multidisciplinary scientific analysis including radiocarbon dating, material composition tests, and microscopic examination. Concurrently, expert consultations with historians and archaeologists are conducted to validate contextual accuracy. Legal ownership and export documentation are scrutinized to ensure compliance with international cultural heritage laws. The workflow also incorporates digital imaging and 3D modeling for record-keeping and virtual exhibition purposes. Final approval requires a consensus meeting among curators, legal advisors, and scientific analysts before formal acquisition and cataloging into the museum's database.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
prov_check      = Transition(label='Provenance Check')
rad_test        = Transition(label='Radiocarbon Test')
mat_analysis    = Transition(label='Material Analysis')
micro_scan      = Transition(label='Microscopic Scan')
expert_review   = Transition(label='Expert Review')
context_val     = Transition(label='Context Validation')
legal_audit     = Transition(label='Legal Audit')
export_verify   = Transition(label='Export Verify')
digital_imaging = Transition(label='Digital Imaging')
model_3d        = Transition(label='3D Modeling')
consensus       = Transition(label='Consensus Meeting')
final_approval  = Transition(label='Final Approval')
catalog_entry   = Transition(label='Catalog Entry')
virtual_setup   = Transition(label='Virtual Setup')
archival_backup = Transition(label='Archival Backup')

# Construct the partial‐order workflow
root = StrictPartialOrder(nodes=[
    prov_check,
    rad_test, mat_analysis, micro_scan,
    expert_review, context_val,
    legal_audit, export_verify,
    digital_imaging, model_3d,
    consensus, final_approval,
    catalog_entry, virtual_setup, archival_backup
])

# 1. After Provenance Check, start scientific analyses and expert consultations
for nxt in [rad_test, mat_analysis, micro_scan, expert_review, context_val]:
    root.order.add_edge(prov_check, nxt)

# 2. After all analyses & consultations, perform legal & export verifications
for src in [rad_test, mat_analysis, micro_scan, expert_review, context_val]:
    for tgt in [legal_audit, export_verify]:
        root.order.add_edge(src, tgt)

# 3. After legal & export, do digital imaging and 3D modeling
for src in [legal_audit, export_verify]:
    for tgt in [digital_imaging, model_3d]:
        root.order.add_edge(src, tgt)

# 4. After digital work, hold the consensus meeting
for src in [digital_imaging, model_3d]:
    root.order.add_edge(src, consensus)

# 5. Consensus meeting leads to final approval
root.order.add_edge(consensus, final_approval)

# 6. Upon final approval, do cataloging, virtual setup, and archival backup
for tgt in [catalog_entry, virtual_setup, archival_backup]:
    root.order.add_edge(final_approval, tgt)