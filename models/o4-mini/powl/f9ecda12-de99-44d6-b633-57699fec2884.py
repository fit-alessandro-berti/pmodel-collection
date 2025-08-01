# Generated from: f9ecda12-de99-44d6-b633-57699fec2884.json
# Description: This process details the complex and highly customized workflow for planning, designing, fabricating, and installing large-scale art installations in public spaces. It involves multiple stakeholders including artists, engineers, city planners, and logistics teams. The process begins with concept approval and budget alignment, followed by iterative design reviews and structural simulations. Procurement of unique materials and specialized fabrication techniques are coordinated with artisans and vendors. Permitting requires coordination with municipal authorities and compliance with safety regulations. Installation involves precise scheduling, site preparation, and on-site assembly with contingency plans for weather or technical setbacks. Post-installation includes inspections, maintenance planning, and public unveiling events, ensuring the artwork remains sustainable and engaging for the community over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ca = Transition(label='Concept Approve')
ba = Transition(label='Budget Align')
dr = Transition(label='Design Review')
ss = Transition(label='Structure Simulate')
sm = Transition(label='Stakeholder Meet')
mp = Transition(label='Material Procure')
vs = Transition(label='Vendor Select')
pa = Transition(label='Permit Apply')
sc = Transition(label='Safety Check')
lp = Transition(label='Logistics Plan')
sp = Transition(label='Site Prep')
wm = Transition(label='Weather Monitor')
fp = Transition(label='Fabricate Parts')
ao = Transition(label='Assemble Onsite')
qi = Transition(label='Quality Inspect')
mpl = Transition(label='Maintenance Plan')
pu = Transition(label='Public Unveil')

# Silent transition for loop exit
skip = SilentTransition()

# 1) Iterative design loop: Design Review -> Structure Simulate, then optionally Stakeholder Meet and repeat
po_design = StrictPartialOrder(nodes=[dr, ss])
po_design.order.add_edge(dr, ss)
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[po_design, sm])

# 2) Weather-monitoring loop before fabrication
loop_weather = OperatorPOWL(operator=Operator.LOOP, children=[wm, skip])

# 3) Procurement: Material Procure -> Vendor Select
po_proc = StrictPartialOrder(nodes=[mp, vs])
po_proc.order.add_edge(mp, vs)

# 4) Permitting: Permit Apply -> Safety Check
po_permit = StrictPartialOrder(nodes=[pa, sc])
po_permit.order.add_edge(pa, sc)

# 5) Installation: Logistics Plan -> Site Prep -> (Weather Monitor loop) -> Fabricate Parts -> Assemble Onsite
po_install = StrictPartialOrder(nodes=[lp, sp, loop_weather, fp, ao])
po_install.order.add_edge(lp, sp)
po_install.order.add_edge(sp, loop_weather)
po_install.order.add_edge(loop_weather, fp)
po_install.order.add_edge(fp, ao)

# 6) Post-installation: Quality Inspect -> Maintenance Plan -> Public Unveil
po_post = StrictPartialOrder(nodes=[qi, mpl, pu])
po_post.order.add_edge(qi, mpl)
po_post.order.add_edge(mpl, pu)

# Root partial order stitching all phases
root = StrictPartialOrder(
    nodes=[ca, ba, loop_design, po_proc, po_permit, po_install, po_post]
)
root.order.add_edge(ca, ba)
root.order.add_edge(ba, loop_design)
root.order.add_edge(loop_design, po_proc)
root.order.add_edge(po_proc, po_permit)
root.order.add_edge(po_permit, po_install)
root.order.add_edge(po_install, po_post)