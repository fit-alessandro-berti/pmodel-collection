# Generated from: 545c9233-2234-410a-b32b-f6e570dc8e64.json
# Description: This process involves coordinating a network of independent artisans and small-scale suppliers to produce bespoke handcrafted products. It starts with raw material sourcing from sustainable local farms, followed by quality vetting and batch allocation to different artisan groups. Each artisan customizes components based on unique client orders, integrating traditional techniques with modern design inputs. The process includes iterative feedback loops between artisans and design coordinators, logistics planning for staggered deliveries, and dynamic inventory adjustments. Final assembly is conducted in a centralized atelier where quality assurance and packaging are tailored to individual client specifications, culminating in a personalized delivery experience that emphasizes craftsmanship and sustainability throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ms = Transition(label='Material Sourcing')
qv = Transition(label='Quality Vetting')
ba = Transition(label='Batch Allocation')
oc = Transition(label='Order Customizing')
df = Transition(label='Design Feedback')
ac = Transition(label='Artisan Coordination')
ct = Transition(label='Component Tracking')
ia = Transition(label='Inventory Adjusting')
lp = Transition(label='Logistics Planning')
ds = Transition(label='Delivery Scheduling')
ap = Transition(label='Assembly Prep')
fa = Transition(label='Final Assembly')
qr = Transition(label='Quality Review')
pt = Transition(label='Packaging Tailoring')
cd = Transition(label='Client Delivery')

# Build the feedback/coordination partial order for the loop
feedback_coor = StrictPartialOrder(nodes=[df, ac])
feedback_coor.order.add_edge(df, ac)

# Loop: Order Customizing <-> (Design Feedback then Artisan Coordination)
loop_custom = OperatorPOWL(operator=Operator.LOOP, children=[oc, feedback_coor])

# Build the root model as a strict partial order
root = StrictPartialOrder(nodes=[
    ms, qv, ba,
    ct, loop_custom,
    ia, lp, ds,
    ap, fa, qr, pt, cd
])

# Define the sequencing and concurrency
root.order.add_edge(ms, qv)
root.order.add_edge(qv, ba)

# After batch allocation, component tracking and the customization loop run in parallel
root.order.add_edge(ba, ct)
root.order.add_edge(ba, loop_custom)

# After both component tracking and the loop, inventory adjusting and logistics planning start
root.order.add_edge(ct, ia)
root.order.add_edge(loop_custom, ia)
root.order.add_edge(ct, lp)
root.order.add_edge(loop_custom, lp)

# Delivery scheduling depends on logistics planning
root.order.add_edge(lp, ds)

# Final assembly line
root.order.add_edge(ds, ap)
root.order.add_edge(ap, fa)
root.order.add_edge(fa, qr)
root.order.add_edge(qr, pt)
root.order.add_edge(pt, cd)