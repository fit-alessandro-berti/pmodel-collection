# Generated from: ba10c964-d8ba-4cc0-bf55-b049daa2ca6a.json
# Description: This process outlines the end-to-end supply chain for artisan cheese, beginning with milk sourcing from local farms, quality testing, and fermentation monitoring. It includes unique steps such as microbial culture selection, aging environment control, and flavor profiling. The process also covers packaging with sustainable materials, direct-to-consumer marketing, and inventory rotation based on sensory evaluation. Additionally, it handles regulatory compliance specific to dairy and organic certifications, coordinates seasonal production variations, and integrates customer feedback for continuous recipe refinement, ensuring a premium product that balances tradition and innovation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms  = Transition(label='Milk Sourcing')
qt  = Transition(label='Quality Testing')
cs  = Transition(label='Culture Selection')
mp  = Transition(label='Milk Pasteurize')
cf  = Transition(label='Curd Formation')
pc  = Transition(label='Pressing Cheese')
spc = Transition(label='Salting Process')
fc  = Transition(label='Fermentation Check')
ac  = Transition(label='Aging Control')
fp  = Transition(label='Flavor Profiling')
cr  = Transition(label='Compliance Review')

pp  = Transition(label='Packaging Prep')
sw  = Transition(label='Sustainable Wrap')

mi  = Transition(label='Marketing Launch')
ir  = Transition(label='Inventory Rotate')

cfb = Transition(label='Customer Feedback')
ru  = Transition(label='Recipe Update')

sa  = Transition(label='Seasonal Adjust')

# 1) Production & Compliance branch
production_pre = StrictPartialOrder(nodes=[ms, qt, cs, mp, cf, pc, spc, fc, ac, fp, cr])
production_pre.order.add_edge(ms,  qt)
production_pre.order.add_edge(qt,  cs)
production_pre.order.add_edge(cs,  mp)
production_pre.order.add_edge(mp,  cf)
production_pre.order.add_edge(cf,  pc)
production_pre.order.add_edge(pc,  spc)
production_pre.order.add_edge(spc, fc)
production_pre.order.add_edge(fc,  ac)
production_pre.order.add_edge(ac,  fp)
production_pre.order.add_edge(fp,  cr)

# 2) Packaging sequence
packaging_seq = StrictPartialOrder(nodes=[pp, sw])
packaging_seq.order.add_edge(pp, sw)

# 3) Marketing & Inventory in parallel
mk_inv_PO = StrictPartialOrder(nodes=[mi, ir])
# (no edge => they are concurrent)

# 4) Feedback loop body
feedback_body = StrictPartialOrder(nodes=[cfb, ru])
feedback_body.order.add_edge(cfb, ru)

# 5) Feedback loop: do marketing/inventory, then optionally feedback->repeat
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[mk_inv_PO, feedback_body])

# 6) Inner workflow: production → packaging → feedback_loop
inner = StrictPartialOrder(nodes=[production_pre, packaging_seq, feedback_loop])
inner.order.add_edge(production_pre, packaging_seq)
inner.order.add_edge(packaging_seq, feedback_loop)

# 7) Seasonal outer loop: do inner workflow, then seasonal adjust, repeat until exit
root = OperatorPOWL(operator=Operator.LOOP, children=[inner, sa])