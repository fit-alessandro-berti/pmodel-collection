# Generated from: 71374d89-c500-40c5-a0c3-b3afc15f790e.json
# Description: This process involves the intricate steps of crafting bespoke artisan perfumes tailored to individual client preferences. Starting from scent profiling and raw material sourcing, the process continues with small-batch formulation, iterative scent testing, and refinement cycles. It includes blending natural and synthetic essences, aging mixtures for maturation, and quality evaluation through expert panels. Packaging design aligns with brand philosophy, and limited edition numbering ensures exclusivity. Final steps include regulatory compliance checks, marketing collateral development, and personalized client delivery with feedback collection for continuous improvement. The process requires coordination across creative, technical, and logistical teams to ensure a unique olfactory experience for each customer.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
sp = Transition(label="Scent Profiling")
ms = Transition(label="Material Sourcing")
ia = Transition(label="Inventory Audit")
sn = Transition(label="Supplier Negotiation")
bf = Transition(label="Batch Formulation")
st = Transition(label="Scent Testing")
br = Transition(label="Blend Refinement")
ea = Transition(label="Essence Aging")
qe = Transition(label="Quality Evaluation")
pd = Transition(label="Packaging Design")
cr = Transition(label="Creative Review")
en = Transition(label="Edition Numbering")
cc = Transition(label="Compliance Check")
mp = Transition(label="Marketing Prep")
lp = Transition(label="Logistics Planning")
cd = Transition(label="Client Delivery")
fc = Transition(label="Feedback Collection")

# Loop for iterative scent testing and blend refinement
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[st, br])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    sp, ms, ia, sn, bf, testing_loop,
    ea, qe, pd, cr, en, cc, mp, lp, cd, fc
])

# Define the control-flow dependencies (partial order edges)
o = root.order
o.add_edge(sp, ms)
o.add_edge(ms, ia)
o.add_edge(ms, sn)
o.add_edge(ia, bf)
o.add_edge(sn, bf)

o.add_edge(bf, testing_loop)
o.add_edge(testing_loop, ea)
o.add_edge(ea, qe)

# Packaging design and creative review in parallel after quality evaluation
o.add_edge(qe, pd)
o.add_edge(qe, cr)
o.add_edge(pd, en)
o.add_edge(cr, en)

# Edition numbering before compliance and marketing prep
o.add_edge(en, cc)
o.add_edge(en, mp)

# Compliance check and marketing prep must complete before logistics planning
o.add_edge(cc, lp)
o.add_edge(mp, lp)

# Logistics planning before client delivery and feedback
o.add_edge(lp, cd)
o.add_edge(cd, fc)