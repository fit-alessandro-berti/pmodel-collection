# Generated from: 05028ada-2daf-488d-9f2d-e52627886b6e.json
# Description: This process involves the detailed authentication of antique artifacts for auction purposes. It starts with initial provenance research, followed by physical inspection using multispectral imaging and material analysis. Experts then perform stylistic comparison and historical context validation. Next, the artifact undergoes chemical composition testing to detect modern materials or restorations. Afterward, 3D scanning and digital reconstruction help in assessing craftsmanship accuracy. A collaborative review session with historians and conservators determines authenticity consensus. Finally, a detailed report is compiled, including risk assessment and valuation recommendations before the artifact is approved for auction listing.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
pc = Transition(label='Provenance Check')
vi = Transition(label='Visual Inspect')
imaging = Transition(label='Imaging Scan')
material = Transition(label='Material Test')
style = Transition(label='Style Compare')
context = Transition(label='Context Validate')
chem = Transition(label='Chemical Analysis')
scan3d = Transition(label='3D Scan')
dmodel = Transition(label='Digital Model')
review = Transition(label='Expert Review')
consensus = Transition(label='Consensus Meet')
risk = Transition(label='Risk Assess')
valuation = Transition(label='Valuation Prep')
report_compile = Transition(label='Report Compile')
auction = Transition(label='Auction Listing')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    pc, vi, imaging, material, style, context, chem,
    scan3d, dmodel, review, consensus, risk,
    valuation, report_compile, auction
])

# Sequential edges
root.order.add_edge(pc, vi)

# After visual inspect, imaging and material tests run in parallel
root.order.add_edge(vi, imaging)
root.order.add_edge(vi, material)

# Both imaging and material must finish before style/context tasks
root.order.add_edge(imaging, style)
root.order.add_edge(material, style)
root.order.add_edge(imaging, context)
root.order.add_edge(material, context)

# Style compare and context validate must finish before chemical analysis
root.order.add_edge(style, chem)
root.order.add_edge(context, chem)

# Then 3D scan → digital model → expert review → consensus meeting
root.order.add_edge(chem, scan3d)
root.order.add_edge(scan3d, dmodel)
root.order.add_edge(dmodel, review)
root.order.add_edge(review, consensus)

# After consensus, risk assessment and valuation prep in parallel
root.order.add_edge(consensus, risk)
root.order.add_edge(consensus, valuation)

# Both feed into report compilation, then auction listing
root.order.add_edge(risk, report_compile)
root.order.add_edge(valuation, report_compile)
root.order.add_edge(report_compile, auction)