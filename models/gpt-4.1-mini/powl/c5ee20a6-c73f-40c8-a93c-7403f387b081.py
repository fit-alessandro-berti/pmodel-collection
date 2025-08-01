# Generated from: c5ee20a6-c73f-40c8-a93c-7403f387b081.json
# Description: This process outlines the detailed workflow for restoring antique items, combining delicate physical restoration techniques with historical research and provenance verification. It involves initial assessment, condition documentation, material analysis, sourcing authentic replacement parts, gentle cleaning, stabilization, repair, and finishing. The process integrates expert consultations, archival referencing, and conservation ethics to ensure the item's historical integrity is maintained. Post-restoration, the item undergoes quality inspection, photographic documentation, and packaging for safe delivery, accompanied by a detailed restoration report and provenance certification to enhance value and authenticity verification.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Initial_Assess = Transition(label='Initial Assess')
Condition_Scan = Transition(label='Condition Scan')
Material_Test = Transition(label='Material Test')

Historical_Check = Transition(label='Historical Check')
Provenance_Verify = Transition(label='Provenance Verify')

Parts_Sourcing = Transition(label='Parts Sourcing')

Gentle_Clean = Transition(label='Gentle Clean')
Stabilize_Item = Transition(label='Stabilize Item')
Structural_Repair = Transition(label='Structural Repair')
Surface_Finish = Transition(label='Surface Finish')

Expert_Consult = Transition(label='Expert Consult')
Archival_Review = Transition(label='Archival Review')
Ethics_Audit = Transition(label='Ethics Audit')

Quality_Inspect = Transition(label='Quality Inspect')
Photo_Document = Transition(label='Photo Document')
Packaging_Prep = Transition(label='Packaging Prep')

Report_Generate = Transition(label='Report Generate')
Certify_Provenance = Transition(label='Certify Provenance')

# Partial order for Initial assessment branch
assess_nodes = [Initial_Assess, Condition_Scan, Material_Test]
assess_po = StrictPartialOrder(nodes=assess_nodes)
assess_po.order.add_edge(Initial_Assess, Condition_Scan)
assess_po.order.add_edge(Condition_Scan, Material_Test)

# Partial order for Historical research branch
hist_nodes = [Historical_Check, Provenance_Verify]
hist_po = StrictPartialOrder(nodes=hist_nodes)
hist_po.order.add_edge(Historical_Check, Provenance_Verify)

# Partial order for post historical check - parts sourcing (dependent on Provenance Verify)
post_hist_po = StrictPartialOrder(nodes=[hist_po, Parts_Sourcing])
post_hist_po.order.add_edge(hist_po, Parts_Sourcing)

# Partial order for restoration steps
restoration_nodes = [Gentle_Clean, Stabilize_Item, Structural_Repair, Surface_Finish]
restoration_po = StrictPartialOrder(nodes=restoration_nodes)
restoration_po.order.add_edge(Gentle_Clean, Stabilize_Item)
restoration_po.order.add_edge(Stabilize_Item, Structural_Repair)
restoration_po.order.add_edge(Structural_Repair, Surface_Finish)

# Partial order for ethics & expert consultations (likely concurrent but prerequisite for finishing)
consult_nodes = [Expert_Consult, Archival_Review, Ethics_Audit]
consult_po = StrictPartialOrder(nodes=consult_nodes)
consult_po.order.add_edge(Expert_Consult, Archival_Review)
consult_po.order.add_edge(Archival_Review, Ethics_Audit)

# Combine ethics & restoration as concurrent branches, since ethics supports conservation integrity
restor_and_consult_po = StrictPartialOrder(nodes=[restoration_po, consult_po])
# No order edges => concurrent

# Combine sourcing with restoration+consultation
sourcing_restor_consult_po = StrictPartialOrder(nodes=[post_hist_po, restor_and_consult_po])
sourcing_restor_consult_po.order.add_edge(post_hist_po, restor_and_consult_po)

# Combine initial assessment branch and historical+sourcing+restoration
initial_hist_rest_po = StrictPartialOrder(nodes=[assess_po, sourcing_restor_consult_po])
initial_hist_rest_po.order.add_edge(assess_po, sourcing_restor_consult_po)

# Final inspection and documentation branch
final_docs_nodes = [Quality_Inspect, Photo_Document, Packaging_Prep]
final_docs_po = StrictPartialOrder(nodes=final_docs_nodes)
final_docs_po.order.add_edge(Quality_Inspect, Photo_Document)
final_docs_po.order.add_edge(Photo_Document, Packaging_Prep)

# Final report and provenance certification (concurrent with final inspection docs)
report_cert_po = StrictPartialOrder(nodes=[Report_Generate, Certify_Provenance])
# no order edges - concurrent

final_wrap_po = StrictPartialOrder(nodes=[final_docs_po, report_cert_po])
# no order edges between these two - concurrent

# Compose whole process
root = StrictPartialOrder(nodes=[initial_hist_rest_po, final_wrap_po])
root.order.add_edge(initial_hist_rest_po, final_wrap_po)