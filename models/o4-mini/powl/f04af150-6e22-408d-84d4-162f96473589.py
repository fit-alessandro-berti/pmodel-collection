# Generated from: f04af150-6e22-408d-84d4-162f96473589.json
# Description: This process describes a complex supply chain tailored for artisan goods involving multiple small-scale producers, quality verification steps, custom packaging, and niche distribution channels. It integrates bespoke material sourcing, handcrafted production timelines, and direct consumer engagement through curated marketplaces. The process also incorporates sustainability audits, adaptive inventory management based on seasonal demand, and collaborative marketing strategies among stakeholders to maintain brand authenticity and exclusivity while scaling operations within limited production capacities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ms   = Transition(label="Material Sourcing")
sv   = Transition(label="Supplier Vetting")
dr   = Transition(label="Design Review")
pb   = Transition(label="Prototype Build")
qa   = Transition(label="Quality Audit")
bs   = Transition(label="Batch Scheduling")
hc   = Transition(label="Handcrafting")
pd   = Transition(label="Packaging Design")
cl   = Transition(label="Custom Labeling")
sc   = Transition(label="Sustainability Check")
isyn = Transition(label="Inventory Sync")
ma   = Transition(label="Market Analysis")
oa   = Transition(label="Order Aggregation")
dp   = Transition(label="Distribution Plan")
cf   = Transition(label="Customer Feedback")

# A silent transition to serve as the 'redo' part of the loop
skip = SilentTransition()

# Build the main production partial order
prod_po = StrictPartialOrder(nodes=[
    ms, sv, dr, pb, qa, bs, hc, pd, cl, sc, isyn, ma, oa, dp, cf
])
# Material sourcing feeds into supplier vetting and design review in parallel
prod_po.order.add_edge(ms, sv)
prod_po.order.add_edge(ms, dr)
# Both vetting and design must finish before prototype build
prod_po.order.add_edge(sv, pb)
prod_po.order.add_edge(dr, pb)
# Prototype → quality audit
prod_po.order.add_edge(pb, qa)
# Quality audit → batch scheduling → handcrafting
prod_po.order.add_edge(qa, bs)
prod_po.order.add_edge(bs, hc)
# Handcrafting → packaging design → custom labeling
prod_po.order.add_edge(hc, pd)
prod_po.order.add_edge(pd, cl)
# After audit also run sustainability check and inventory sync in parallel
prod_po.order.add_edge(qa, sc)
prod_po.order.add_edge(qa, isyn)
# Once labeling, sustainability and inventory are done, do market analysis
prod_po.order.add_edge(cl, ma)
prod_po.order.add_edge(sc, ma)
prod_po.order.add_edge(isyn, ma)
# Then aggregate orders, plan distribution, and collect feedback
prod_po.order.add_edge(ma, oa)
prod_po.order.add_edge(oa, dp)
prod_po.order.add_edge(dp, cf)

# Wrap the entire production cycle in a loop to model scaling/adaptive repeats
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[prod_po, skip]
)