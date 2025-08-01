# Generated from: d37634ed-0fff-47d1-aa9a-cbfe21293011.json
# Description: This process governs the end-to-end operations of an urban vertical farm that integrates hydroponic crop production with local distribution and waste recycling. Starting from seed selection, the process includes nutrient solution preparation, environmental monitoring, automated harvesting, quality inspection, packaging, and delivery to local markets. Additionally, it incorporates waste biomass processing for compost generation and energy recovery, ensuring a closed-loop sustainable system. Coordination with city regulations and community engagement programs also plays a vital role in optimizing farm output while minimizing ecological footprint and promoting urban food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ts     = Transition(label='Seed Selection')
nm     = Transition(label='Nutrient Mix')
ec     = Transition(label='Environment Check')
ps     = Transition(label='Planting Setup')
gm     = Transition(label='Growth Monitoring')
pest   = Transition(label='Pest Control')
ah     = Transition(label='Automated Harvest')
qi     = Transition(label='Quality Inspect')
pp     = Transition(label='Packaging Prep')
of     = Transition(label='Order Fulfill')
ld     = Transition(label='Local Delivery')
wc     = Transition(label='Waste Collect')
bp     = Transition(label='Biomass Process')
cc     = Transition(label='Compost Create')
er     = Transition(label='Energy Recover')
rr     = Transition(label='Regulation Review')
comm   = Transition(label='Community Engage')

# Loop for repeated Growth Monitoring and Pest Control
mon_pest = StrictPartialOrder(nodes=[gm, pest])
skip     = SilentTransition()
loop_mon  = OperatorPOWL(operator=Operator.LOOP, children=[mon_pest, skip])

# Concurrent Compost Creation and Energy Recovery
comp_en = StrictPartialOrder(nodes=[cc, er])

# Waste processing flow: Waste Collect -> Biomass Process -> {Compost, Energy} concurrently
waste_flow = StrictPartialOrder(nodes=[wc, bp, comp_en])
waste_flow.order.add_edge(wc, bp)
waste_flow.order.add_edge(bp, comp_en)

# Main sequential flow
main_flow = StrictPartialOrder(nodes=[
    ts, nm, ec, ps,
    loop_mon,
    ah, qi, pp, of, ld,
    waste_flow
])
main_flow.order.add_edge(ts,     nm)
main_flow.order.add_edge(nm,     ec)
main_flow.order.add_edge(ec,     ps)
main_flow.order.add_edge(ps,     loop_mon)
main_flow.order.add_edge(loop_mon, ah)
main_flow.order.add_edge(ah,     qi)
main_flow.order.add_edge(qi,     pp)
main_flow.order.add_edge(pp,     of)
main_flow.order.add_edge(of,     ld)
main_flow.order.add_edge(ld,     waste_flow)

# Root POWL: main process runs concurrently with regulation review and community engagement
root = StrictPartialOrder(nodes=[main_flow, rr, comm])