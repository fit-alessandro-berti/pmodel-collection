# Generated from: c25b7783-f083-483b-a95f-1b6c7cae2787.json
# Description: This process involves the meticulous authentication of antique artifacts for auction houses and private collectors. It begins with preliminary visual inspection followed by scientific material analysis including spectroscopy and radiocarbon dating. Experts then cross-reference the artifact's provenance with historical records and databases. If discrepancies arise, forensic imaging and microscopic surface analysis are conducted. The process also includes consultation with historians and artisans familiar with the era and style of the artifact. After comprehensive evaluation, a detailed authentication report is prepared, including possible restoration suggestions, risk assessment, and market valuation. Finally, the artifact undergoes secure packaging and certification before being released for sale or exhibition. This atypical process ensures both scientific rigor and historical accuracy, minimizing forgeries and preserving cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
vi = Transition(label="Visual Inspect")
mt = Transition(label="Material Test")
sa = Transition(label="Spectro Analyze")
rd = Transition(label="Radiocarbon Date")
pc = Transition(label="Provenance Check")
db = Transition(label="Database Search")
dr = Transition(label="Discrepancy Review")
fi = Transition(label="Forensic Imaging")
sm = Transition(label="Surface Microscopy")
ec = Transition(label="Expert Consult")
hc = Transition(label="Historical Crossref")
rdraft = Transition(label="Report Draft")
rp = Transition(label="Restoration Plan")
ra = Transition(label="Risk Assess")
mv = Transition(label="Market Valuate")
sp = Transition(label="Secure Package")
ci = Transition(label="Certification Issue")

# Silent skip for the no‐discrepancy branch
skip = SilentTransition()

# 1) Material analysis splits in parallel: Spectro Analyze || Radiocarbon Date after Material Test
po_material = StrictPartialOrder(nodes=[mt, sa, rd])
po_material.order.add_edge(mt, sa)
po_material.order.add_edge(mt, rd)

# 2) Provenance cross‐checks in parallel after material analysis
po_provenance = StrictPartialOrder(nodes=[pc, db])
# ordering from the material‐analysis operator will be added at the root level

# 3) If discrepancy: run Forensic Imaging || Surface Microscopy, else skip
po_imaging = StrictPartialOrder(nodes=[fi, sm])
xor_discrepancy = OperatorPOWL(operator=Operator.XOR, children=[skip, po_imaging])

# 4) Consultation in parallel
po_consult = StrictPartialOrder(nodes=[ec, hc])

# 5) Report drafting then parallel sub‐tasks
po_report = StrictPartialOrder(nodes=[rdraft, rp, ra, mv])
po_report.order.add_edge(rdraft, rp)
po_report.order.add_edge(rdraft, ra)
po_report.order.add_edge(rdraft, mv)

# 6) Packaging then certification
po_pack = StrictPartialOrder(nodes=[sp, ci])
po_pack.order.add_edge(sp, ci)

# Build the root partial order, sequencing the major steps
root = StrictPartialOrder(
    nodes=[
        vi,
        po_material,
        po_provenance,
        dr,
        xor_discrepancy,
        po_consult,
        po_report,
        po_pack,
    ]
)
# 1 → 2
root.order.add_edge(vi, po_material)
# 2 → 3
root.order.add_edge(po_material, po_provenance)
# 3 → discrepancy review
root.order.add_edge(po_provenance, dr)
# after review, either skip or imaging
root.order.add_edge(dr, xor_discrepancy)
# then consultation
root.order.add_edge(xor_discrepancy, po_consult)
# then report
root.order.add_edge(po_consult, po_report)
# then packaging & certification
root.order.add_edge(po_report, po_pack)