# Generated from: e989a21a-4800-401e-ac00-a64f68c733fd.json
# Description: This complex process involves verifying the authenticity of rare and valuable artworks through a multi-disciplinary approach combining scientific analysis, provenance research, expert consultation, and advanced imaging technologies. It begins with initial visual inspection and historical documentation gathering, followed by pigment and material composition testing using spectroscopy. Next, experts analyze stylistic elements and compare them against known artist techniques. Provenance chains are meticulously traced to identify any gaps or suspicious transfers. Digital imaging techniques such as infrared reflectography and X-ray fluorescence are employed to reveal underdrawings and alterations. A cross-functional team then consolidates findings to assess authenticity, with a final report generated for stakeholders. This process helps prevent forgery circulation and ensures cultural heritage preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Visual_Inspect = Transition(label='Visual Inspect')
Document_Gather = Transition(label='Document Gather')

Material_Test = Transition(label='Material Test')
Pigment_Analyze = Transition(label='Pigment Analyze')

Style_Compare = Transition(label='Style Compare')
Provenance_Trace = Transition(label='Provenance Trace')

Infrared_Scan = Transition(label='Infrared Scan')
Xray_Fluoresce = Transition(label='Xray Fluoresce')

Expert_Consult = Transition(label='Expert Consult')

Data_Crosscheck = Transition(label='Data Crosscheck')

Forgery_Detect = Transition(label='Forgery Detect')

Report_Draft = Transition(label='Report Draft')
Stakeholder_Review = Transition(label='Stakeholder Review')
Final_Approval = Transition(label='Final Approval')
Archive_Store = Transition(label='Archive Store')

# Initial parallel part: Visual Inspect and Document Gather concurrent
init_PO = StrictPartialOrder(nodes=[Visual_Inspect, Document_Gather])

# Material Test concurrent with Pigment Analyze as a small partial order (syntax says unconnected are concurrent)
# But "pigment and material composition testing using spectroscopy" is described sequentially, so test then analyze:
mat_PO = StrictPartialOrder(nodes=[Material_Test, Pigment_Analyze])
mat_PO.order.add_edge(Material_Test, Pigment_Analyze)

# Experts analyze stylistic elements and compare with known artist techniques
# Style Compare and Provenance Trace are described as next steps, presumably sequential,
# but the provenance tracing and style comparison can be concurrent or a partial order if description allows.
# Text says: Next experts analyze stylistic elements, then provenance chains traced.

style_prov_PO = StrictPartialOrder(nodes=[Style_Compare, Provenance_Trace])
style_prov_PO.order.add_edge(Style_Compare, Provenance_Trace)

# Digital imaging techniques Infrared Scan and Xray Fluoresce are employed to reveal details
# They seem to be concurrent methods used
img_PO = StrictPartialOrder(nodes=[Infrared_Scan, Xray_Fluoresce])

# Expert Consult after imaging and research steps:
# Assume Expert Consult follows completion of Style/Prov and imaging steps, so those two partial orders precede Expert Consult
# We'll create one partial order for research and imaging converging on Expert Consult

research_imaging_PO = StrictPartialOrder(
    nodes=[style_prov_PO, img_PO, Expert_Consult]
)
# Order: style_prov_PO and img_PO --> Expert_Consult
research_imaging_PO.order.add_edge(style_prov_PO, Expert_Consult)
research_imaging_PO.order.add_edge(img_PO, Expert_Consult)

# Data Crosscheck occurs after Expert Consult
data_PO = StrictPartialOrder(nodes=[Expert_Consult, Data_Crosscheck])
data_PO.order.add_edge(Expert_Consult, Data_Crosscheck)

# Forgery Detect after Data Crosscheck
forgery_PO = StrictPartialOrder(nodes=[Data_Crosscheck, Forgery_Detect])
forgery_PO.order.add_edge(Data_Crosscheck, Forgery_Detect)

# Final report generation steps: Report Draft, Stakeholder Review, Final Approval, Archive Store
# Presumably sequential
report_PO = StrictPartialOrder(
    nodes=[Report_Draft, Stakeholder_Review, Final_Approval, Archive_Store]
)
report_PO.order.add_edge(Report_Draft, Stakeholder_Review)
report_PO.order.add_edge(Stakeholder_Review, Final_Approval)
report_PO.order.add_edge(Final_Approval, Archive_Store)

# Now combine all phases into a complete partial order according to process description order:
# initial_PO -> mat_PO -> research_imaging_PO -> data_PO -> forgery_PO -> report_PO

root = StrictPartialOrder(nodes=[init_PO, mat_PO, research_imaging_PO, data_PO, forgery_PO, report_PO])
root.order.add_edge(init_PO, mat_PO)
root.order.add_edge(mat_PO, research_imaging_PO)
root.order.add_edge(research_imaging_PO, data_PO)
root.order.add_edge(data_PO, forgery_PO)
root.order.add_edge(forgery_PO, report_PO)