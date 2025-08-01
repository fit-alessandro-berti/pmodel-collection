# Generated from: 123751a7-ed99-4282-a93c-a954326eb58c.json
# Description: This process involves the detailed examination and verification of antique artifacts to establish provenance and authenticity before acquisition or sale. It integrates multidisciplinary expertise including historical research, scientific analysis, and expert appraisal. Initial steps include preliminary inspection and documentation, followed by provenance tracing through archives and previous ownership records. Scientific testing such as radiocarbon dating, spectroscopy, and material composition analysis are conducted to verify age and origin. Parallel to technical evaluation, stylistic comparison is performed against known authentic pieces. The process requires collaboration with legal teams to confirm ownership legitimacy and compliance with cultural heritage laws. Finally, a comprehensive authentication report is compiled, including visual documentation and certification, before the artifact is approved for market entry or museum acquisition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Prelim_Inspect = Transition(label='Prelim Inspect')
Document_Item = Transition(label='Document Item')

Trace_Provenance = Transition(label='Trace Provenance')
Archive_Search = Transition(label='Archive Search')
Ownership_Check = Transition(label='Ownership Check')

Radiocarbon_Test = Transition(label='Radiocarbon Test')
Spectroscopy_Scan = Transition(label='Spectroscopy Scan')
Material_Analysis = Transition(label='Material Analysis')

Style_Compare = Transition(label='Style Compare')
Expert_Appraise = Transition(label='Expert Appraise')

Legal_Review = Transition(label='Legal Review')
Heritage_Compliance = Transition(label='Heritage Compliance')

Compile_Report = Transition(label='Compile Report')
Visual_Document = Transition(label='Visual Document')
Certification_Issue = Transition(label='Certification Issue')

Market_Approval = Transition(label='Market Approval')

# Build sub partial orders and operators according to description

# 1. Preliminary inspection and documentation in sequence
prelim_po = StrictPartialOrder(nodes=[Prelim_Inspect, Document_Item])
prelim_po.order.add_edge(Prelim_Inspect, Document_Item)

# 2. Provenance tracing: Trace Provenance with Archive Search and Ownership Check in parallel
trace_prov_po = StrictPartialOrder(nodes=[Trace_Provenance, Archive_Search, Ownership_Check])
trace_prov_po.order.add_edge(Trace_Provenance, Archive_Search)
trace_prov_po.order.add_edge(Trace_Provenance, Ownership_Check)

# 3. Scientific testing: Radiocarbon_Test, Spectroscopy_Scan, Material_Analysis in parallel
scientific_po = StrictPartialOrder(nodes=[Radiocarbon_Test, Spectroscopy_Scan, Material_Analysis])

# 4. Stylistic comparison and expert appraisal in sequence
style_exp_po = StrictPartialOrder(nodes=[Style_Compare, Expert_Appraise])
style_exp_po.order.add_edge(Style_Compare, Expert_Appraise)

# 5. Technical evaluation = scientific testing and stylistic comparison/expert appraisal in parallel
tech_eval_po = StrictPartialOrder(nodes=[scientific_po, style_exp_po])
# no order edges between scientific_po and style_exp_po means concurrent

# 6. Legal collaboration: Legal Review and Heritage Compliance in parallel
legal_po = StrictPartialOrder(nodes=[Legal_Review, Heritage_Compliance])

# 7. Compile report including visual document and certification issue
compile_report_po = StrictPartialOrder(nodes=[Compile_Report, Visual_Document, Certification_Issue])
compile_report_po.order.add_edge(Compile_Report, Visual_Document)
compile_report_po.order.add_edge(Compile_Report, Certification_Issue)

# 8. Final approval: Market Approval

# Now combine all in correct partial order

# Whole process partial order nodes:
# prelim_po --> trace_prov_po --> tech_eval_po --> legal_po --> compile_report_po --> Market_Approval

root = StrictPartialOrder(
    nodes=[
        prelim_po,
        trace_prov_po,
        tech_eval_po,
        legal_po,
        compile_report_po,
        Market_Approval
    ]
)

root.order.add_edge(prelim_po, trace_prov_po)
root.order.add_edge(trace_prov_po, tech_eval_po)
root.order.add_edge(tech_eval_po, legal_po)
root.order.add_edge(legal_po, compile_report_po)
root.order.add_edge(compile_report_po, Market_Approval)