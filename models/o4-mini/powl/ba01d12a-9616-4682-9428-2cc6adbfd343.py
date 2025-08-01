# Generated from: ba01d12a-9616-4682-9428-2cc6adbfd343.json
# Description: This process manages the end-to-end supply chain for handcrafted artisan goods, integrating unique sourcing methods, bespoke quality checks, and personalized logistics. It begins with raw material scouting in remote locations, followed by artisan selection based on skill and style alignment. Materials undergo custom treatment before distribution to workshops. Each artisan crafts unique pieces verified through multi-stage quality audits involving both automated sensors and expert appraisal. Finished goods are then personalized with client-specific branding and packed using eco-friendly methods. Finally, logistics coordination ensures delivery via specialty carriers that maintain product integrity and cultural authenticity, while gathering consumer feedback for continuous process refinement. This atypical supply chain blends traditional craftsmanship with modern technology and sustainability principles, requiring careful coordination of diverse activities to maintain product uniqueness and market appeal.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label="Material Scout")
artisan_select = Transition(label="Artisan Select")
mt = Transition(label="Material Treat")
wa = Transition(label="Workshop Assign")
cm = Transition(label="Craft Monitor")
qa = Transition(label="Quality Audit")
sc = Transition(label="Sensor Check")
er = Transition(label="Expert Review")
bp = Transition(label="Brand Personalize")
ep = Transition(label="Eco Pack")
cs = Transition(label="Carrier Select")
ds = Transition(label="Delivery Schedule")
ic = Transition(label="Integrity Check")
fg = Transition(label="Feedback Gather")
pr = Transition(label="Process Refine")
ma = Transition(label="Market Align")

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ms, artisan_select, mt, wa, cm,
    qa, sc, er,
    bp, ep, cs, ds,
    ic, fg, pr, ma
])

# Sequential dependencies
root.order.add_edge(ms, artisan_select)
root.order.add_edge(artisan_select, mt)
root.order.add_edge(mt, wa)
root.order.add_edge(wa, cm)
root.order.add_edge(cm, qa)

# Quality‐audit sub‐flow: Sensor Check and Expert Review in parallel after Quality Audit
root.order.add_edge(qa, sc)
root.order.add_edge(qa, er)

# After both checks, continue with branding
root.order.add_edge(sc, bp)
root.order.add_edge(er, bp)

# Continue the rest of the sequence
root.order.add_edge(bp, ep)
root.order.add_edge(ep, cs)
root.order.add_edge(cs, ds)
root.order.add_edge(ds, ic)
root.order.add_edge(ic, fg)
root.order.add_edge(fg, pr)
root.order.add_edge(pr, ma)