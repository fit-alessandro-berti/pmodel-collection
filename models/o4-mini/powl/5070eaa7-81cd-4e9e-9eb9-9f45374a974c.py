# Generated from: 5070eaa7-81cd-4e9e-9eb9-9f45374a974c.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a constrained city environment. It begins with site analysis and zoning approval, followed by modular infrastructure assembly and environmental control calibration. The process includes nutrient solution formulation, crop selection tailored to vertical layers, and integration of AI-driven monitoring systems. Waste recycling loops and energy optimization are implemented to ensure sustainability. Continuous data analysis guides adaptive growth protocols, while supply chain synchronization ensures timely distribution to local markets. The entire operation demands coordination between agricultural scientists, engineers, local authorities, and logistics teams to achieve efficient urban agriculture that maximizes yield and minimizes ecological footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
sa = Transition(label="Site Analysis")
za = Transition(label="Zoning Approval")
ma = Transition(label="Modular Assembly")
ec = Transition(label="Env Control")
nm = Transition(label="Nutrient Mix")
cs = Transition(label="Crop Selection")
ai = Transition(label="AI Monitoring")
wr = Transition(label="Waste Recycling")
ea = Transition(label="Energy Audit")
da = Transition(label="Data Analysis")
gt = Transition(label="Growth Tuning")
ss = Transition(label="Supply Sync")
mo = Transition(label="Market Outreach")
st = Transition(label="Staff Training")
qc = Transition(label="Quality Check")
hp = Transition(label="Harvest Plan")

# Build the waste-energy loop: do Waste Recycling then Energy Audit repeatedly
we_po = StrictPartialOrder(nodes=[wr, ea])
we_po.order.add_edge(wr, ea)
waste_energy_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[SilentTransition(), we_po]
)

# Assemble the main process as a strict partial order
root = StrictPartialOrder(
    nodes=[sa, za, ma, ec, nm, cs, ai,
           waste_energy_loop,
           da, gt, ss, mo, st, qc, hp]
)

# Define the control-flow edges
root.order.add_edge(sa, za)
root.order.add_edge(za, ma)
root.order.add_edge(ma, ec)
root.order.add_edge(ec, nm)
root.order.add_edge(nm, cs)
root.order.add_edge(cs, ai)
root.order.add_edge(ai, waste_energy_loop)
root.order.add_edge(waste_energy_loop, da)
root.order.add_edge(da, gt)
root.order.add_edge(gt, ss)
root.order.add_edge(ss, mo)

# After Market Outreach, Staff Training and Quality Check can proceed in parallel
root.order.add_edge(mo, st)
root.order.add_edge(mo, qc)

# Both must complete before Harvest Plan
root.order.add_edge(st, hp)
root.order.add_edge(qc, hp)