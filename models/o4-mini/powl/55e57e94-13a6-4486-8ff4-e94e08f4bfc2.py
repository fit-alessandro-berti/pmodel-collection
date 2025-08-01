# Generated from: 55e57e94-13a6-4486-8ff4-e94e08f4bfc2.json
# Description: This process outlines the steps involved in establishing an urban vertical farming system within a repurposed warehouse. It encompasses site evaluation, structural modification, installation of hydroponic systems, climate control setup, nutrient cycling design, crop selection, automation integration, labor training, and ongoing maintenance protocols. The process aims to optimize space utilization, maximize yield per square meter, and ensure sustainable resource management while meeting urban agricultural demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss = Transition(label='Site Survey')
sa = Transition(label='Structure Audit')
ld = Transition(label='Layout Design')
hi = Transition(label='Hydroponic Install')
csu = Transition(label='Climate Setup')
lc = Transition(label='Lighting Config')
np = Transition(label='Nutrient Plan')
csel = Transition(label='Crop Selection')
ai = Transition(label='Automation Install')
wr = Transition(label='Water Recycling')
pc = Transition(label='Pest Control')
st = Transition(label='Staff Training')
tc = Transition(label='Trial Cultivation')
sc = Transition(label='System Calibration')
ym = Transition(label='Yield Monitoring')
mc = Transition(label='Maintenance Check')
wd = Transition(label='Waste Disposal')

# 1) Initial sequence: Site Survey -> Structure Audit -> Layout Design
seq1 = StrictPartialOrder(nodes=[ss, sa, ld])
seq1.order.add_edge(ss, sa)
seq1.order.add_edge(sa, ld)

# 2) Parallel installation tasks after layout design
install_po = StrictPartialOrder(nodes=[hi, csu, lc, np])
# no edges => all concurrent

# 3) Parallel post‐selection tasks
atc_po = StrictPartialOrder(nodes=[ai, wr, pc, st])
# no edges => all concurrent

# 4) Cultivation sequence
cultivation_po = StrictPartialOrder(nodes=[tc, sc, ym])
cultivation_po.order.add_edge(tc, sc)
cultivation_po.order.add_edge(sc, ym)

# 5) Maintenance subprocess for the loop
maintenance_po = StrictPartialOrder(nodes=[mc, wd])
maintenance_po.order.add_edge(mc, wd)

# 6) Loop: run initial cultivation, then optionally repeat maintenance & re‐calibration
loop = OperatorPOWL(operator=Operator.LOOP, children=[cultivation_po, maintenance_po])

# 7) Assemble full process as a partial order of the five major blocks
root = StrictPartialOrder(nodes=[seq1, install_po, csel, atc_po, loop])
root.order.add_edge(seq1, install_po)    # after layout design install systems
root.order.add_edge(install_po, csel)    # then select crops
root.order.add_edge(csel, atc_po)        # then install automation, set up recycling & pest control, train staff
root.order.add_edge(atc_po, loop)        # then trial cultivation and enter maintenance loop