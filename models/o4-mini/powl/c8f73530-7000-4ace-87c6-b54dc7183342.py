# Generated from: c8f73530-7000-4ace-87c6-b54dc7183342.json
# Description: This process describes the complex supply chain of artisan cheese production, starting from sourcing rare milk varieties from remote farms, followed by controlled fermentation, artisanal aging, quality sensory evaluation, bespoke packaging design, and finally customized distribution to niche gourmet markets. Each step involves detailed coordination with local farmers, microbiologists, master cheesemakers, packaging designers, and logistics partners to maintain quality and authenticity. The process also includes managing seasonal variations, regulatory compliance, and customer feedback integration to continuously refine product offerings and meet evolving market demands, ensuring a unique and premium cheese experience for connoisseurs worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
mp = Transition(label='Milk Pasteurize')
ci = Transition(label='Culture Inoculate')
co = Transition(label='Coagulation')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Drain')
pr = Transition(label='Pressing')
sa = Transition(label='Salting')
ac = Transition(label='Aging Control')
saud = Transition(label='Sensory Audit')
pd = Transition(label='Packaging Design')
la = Transition(label='Label Approval')
oc = Transition(label='Order Customization')
lp = Transition(label='Logistics Plan')
md = Transition(label='Market Delivery')
cf = Transition(label='Customer Feedback')
rc = Transition(label='Regulatory Check')

# Main supply‐chain sequence (from sourcing to delivery)
main = StrictPartialOrder(nodes=[
    ms, qt, mp, ci, co, cc, wd, pr, sa, ac, saud, pd, la, oc, lp, md
])
edges_main = [
    (ms, qt), (qt, mp), (mp, ci), (ci, co), (co, cc), (cc, wd),
    (wd, pr), (pr, sa), (sa, ac), (ac, saud), (saud, pd),
    (pd, la), (la, oc), (oc, lp), (lp, md)
]
for src, tgt in edges_main:
    main.order.add_edge(src, tgt)

# Feedback and compliance subprocess
feedback = StrictPartialOrder(nodes=[cf, rc])
feedback.order.add_edge(cf, rc)

# Loop: run the main process, then either exit or handle feedback/compliance and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main, feedback]
)