# Generated from: d6b18480-e9ee-4493-ada4-a1f7ab522c2f.json
# Description: This process involves coordinating a decentralized network of artisan producers, raw material foragers, quality inspectors, and niche market distributors to deliver bespoke craft products. It includes sourcing rare materials, verifying authenticity through blockchain, managing seasonal production cycles, synchronizing handmade assembly timelines, and adapting logistics due to fluctuating artisan availability and handcrafted batch variability. The process also incorporates dynamic pricing based on demand insights and artisan reputation, ensures compliance with local cultural heritage laws, and integrates direct customer feedback loops for continuous product refinement. This atypical supply chain balances traditional craftsmanship with modern digital tools to maintain unique product integrity while scaling niche artisan markets internationally.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# define activities
ms = Transition(label='Material Sourcing')
fd = Transition(label='Forager Dispatch')
ac = Transition(label='Authenticity Check')
bu = Transition(label='Blockchain Update')
bs = Transition(label='Batch Scheduling')
aa = Transition(label='Artisan Allocation')
ca = Transition(label='Craft Assembly')
qi = Transition(label='Quality Inspection')
df = Transition(label='Demand Forecast')
pa = Transition(label='Price Adjustment')
ra = Transition(label='Reputation Audit')
cr = Transition(label='Compliance Review')
lp = Transition(label='Logistics Planning')
ds = Transition(label='Distributor Sync')
cf = Transition(label='Customer Feedback')
pr = Transition(label='Product Refinement')
sr = Transition(label='Seasonal Review')

# body of one seasonal cycle
body = StrictPartialOrder(nodes=[ms, fd, ac, bu,
                                 bs, aa, ca, qi,
                                 df, pa, ra, cr, lp,
                                 ds, cf, pr])

# sequencing for supply & verification
body.order.add_edge(ms, fd)
body.order.add_edge(fd, ac)
body.order.add_edge(ac, bu)
# fork into production and business branches
body.order.add_edge(bu, bs)
body.order.add_edge(bu, df)
# production branch
body.order.add_edge(bs, aa)
body.order.add_edge(aa, ca)
body.order.add_edge(ca, qi)
# business branch
body.order.add_edge(df, pa)
body.order.add_edge(pa, ra)
body.order.add_edge(ra, cr)
body.order.add_edge(cr, lp)
# join at distribution
body.order.add_edge(qi, ds)
body.order.add_edge(lp, ds)
# feedback and refinement
body.order.add_edge(ds, cf)
body.order.add_edge(cf, pr)

# loop over seasonal cycles
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, sr])

# root of the POWL model
root = loop