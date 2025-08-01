# Generated from: 9cf1a7bc-3df4-4a3a-8de4-f1776343f834.json
# Description: This process outlines the complex supply chain of artisanal cheese production, from sourcing rare milk varieties to aging cheese in controlled environments. It involves selecting heritage breeds, managing microflora cultures, monitoring environmental conditions, coordinating with local farmers, ensuring quality through sensory evaluation, packaging in sustainable materials, handling customs for international export, and managing direct-to-consumer logistics. The process requires intricate coordination between agricultural practices, microbial science, artisan craftsmanship, and niche marketing strategies to ensure the final product maintains its unique flavor profile and meets regulatory standards across different markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL Transitions
bs = Transition(label='Breed Selection')
mh = Transition(label='Milk Harvest')
cp = Transition(label='Culture Prep')
mp = Transition(label='Milk Pasteurize')
cf = Transition(label='Curd Formation')
wd = Transition(label='Whey Drain')
mi = Transition(label='Mold Inoculate')
pc = Transition(label='Press Cheese')
sa = Transition(label='Salt Application')
ca = Transition(label='Cave Aging')
qt = Transition(label='Quality Test')
pp = Transition(label='Packaging Prep')
ld = Transition(label='Label Design')
cc = Transition(label='Customs Clear')
od = Transition(label='Order Dispatch')
fb = Transition(label='Customer Feedback')

# Build the partial order
root = StrictPartialOrder(nodes=[
    bs, mh, cp, mp, cf, wd, mi, pc, sa, ca, qt, pp, ld, cc, od, fb
])

# Add the ordering constraints
# 1. Breed Selection -> Milk Harvest, Culture Prep
root.order.add_edge(bs, mh)
root.order.add_edge(bs, cp)
# 2. Milk Harvest -> Milk Pasteurize -> Curd Formation -> Whey Drain
root.order.add_edge(mh, mp)
root.order.add_edge(mp, cf)
root.order.add_edge(cf, wd)
# 3. Culture Prep -> Mold Inoculate (needs culture)
root.order.add_edge(cp, mi)
# 4. Whey Drain -> Mold Inoculate
root.order.add_edge(wd, mi)
# 5. Mold Inoculate -> Press Cheese -> Salt Application -> Cave Aging -> Quality Test
root.order.add_edge(mi, pc)
root.order.add_edge(pc, sa)
root.order.add_edge(sa, ca)
root.order.add_edge(ca, qt)
# 6. After Quality Test: Packaging Prep and Label Design in parallel
root.order.add_edge(qt, pp)
root.order.add_edge(qt, ld)
# 7. Packaging Prep & Label Design -> Customs Clear -> Order Dispatch -> Customer Feedback
root.order.add_edge(pp, cc)
root.order.add_edge(ld, cc)
root.order.add_edge(cc, od)
root.order.add_edge(od, fb)