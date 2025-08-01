# Generated from: 36a071f5-d3b1-4d94-af8b-560b64847f46.json
# Description: This process involves the complex orchestration of sourcing rare milk varieties, aging cheese in controlled microclimates, and managing artisanal packaging to preserve flavor integrity. It includes farm inspections, microbial testing, seasonal variation adjustments, and bespoke logistics coordination to ensure freshness and compliance with gourmet food regulations. The process also incorporates consumer feedback loops and limited edition releases to maintain exclusivity and market demand, requiring tight collaboration between dairy farmers, microbiologists, logistics teams, and marketing units.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Milk Sourcing')
fi = Transition(label='Farm Inspection')
mt = Transition(label='Microbial Test')
mp = Transition(label='Milk Pasteurize')
cf = Transition(label='Curd Formation')
ws = Transition(label='Whey Separation')
cm = Transition(label='Cheese Molding')
ss = Transition(label='Salting Stage')
ac = Transition(label='Aging Control')
cl = Transition(label='Climate Adjust')
qc = Transition(label='Quality Check')
pd = Transition(label='Packaging Design')
lp = Transition(label='Label Printing')
lg = Transition(label='Logistics Plan')
rd = Transition(label='Retail Dispatch')
cfb = Transition(label='Customer Feedback')
ma = Transition(label='Market Analysis')

# SubPO: Milk sourcing and inspection flow
ms_inspection = StrictPartialOrder(nodes=[ms, fi, mt])
ms_inspection.order.add_edge(ms, fi)
ms_inspection.order.add_edge(fi, mt)

# SubPO: Milk processing partial order (pasteurize in parallel with microbial test finish)
milk_proc = StrictPartialOrder(nodes=[mp, cf, ws, cm, ss])
milk_proc.order.add_edge(mp, cf)
milk_proc.order.add_edge(cf, ws)
milk_proc.order.add_edge(ws, cm)
milk_proc.order.add_edge(cm, ss)

# SubPO: Aging control with climate adjustment loop
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[ac, cl])

# Quality check after aging
qc_after_aging = qc

# Packaging design and label printing (can be concurrent)
packaging = StrictPartialOrder(nodes=[pd, lp])

# Logistics plan and retail dispatch (sequential)
logistics = StrictPartialOrder(nodes=[lg, rd])
logistics.order.add_edge(lg, rd)

# Market and feedback loop: customer feedback and market analysis in loop
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[cfb, ma])

# Combine packaging and logistics concurrently
pack_and_logistics = StrictPartialOrder(nodes=[packaging, logistics])
pack_and_logistics.order.add_edge(packaging, logistics)  # Packaging before logistics

# Combine all main flows with partial ordering
root = StrictPartialOrder(
    nodes=[ms_inspection, milk_proc, aging_loop, qc_after_aging, pack_and_logistics, feedback_loop]
)

# Add ordering between phases
root.order.add_edge(ms_inspection, milk_proc)      # sourcing before processing
root.order.add_edge(milk_proc, aging_loop)         # processing before aging
root.order.add_edge(aging_loop, qc_after_aging)    # aging before quality check
root.order.add_edge(qc_after_aging, pack_and_logistics)  # quality check before packaging/logistics
root.order.add_edge(pack_and_logistics, feedback_loop)   # after dispatch feedback loop starts