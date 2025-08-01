# Generated from: 3cfbfe1d-d8f9-414b-a761-f536beb86881.json
# Description: This process manages the end-to-end supply chain for handcrafted luxury goods, integrating rare material sourcing, artisan allocation, quality assurance through traditional methods, custom order management, and dynamic pricing strategies based on market trends. It involves coordination between remote workshops, seasonal artisan availability, and bespoke packaging tailored to client preferences, ensuring authenticity and sustainability are maintained throughout the production and distribution lifecycle. The process also includes feedback loops for continuous artisan skill development and selective retailer partnerships to preserve brand exclusivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Material Sourcing')
vv = Transition(label='Vendor Vetting')
mi = Transition(label='Material Inspection')
asel = Transition(label='Artisan Selection')
oc = Transition(label='Order Customization')
da = Transition(label='Design Approval')
ws = Transition(label='Workshop Scheduling')
hc = Transition(label='Handcrafting')
sf = Transition(label='Skill Feedback')
qc = Transition(label='Quality Checking')
pd = Transition(label='Packaging Design')
sa = Transition(label='Sustainability Audit')
pu = Transition(label='Pricing Update')
inv = Transition(label='Inventory Sync')
ro = Transition(label='Retailer Onboarding')

# 1. Preparation: sourcing through artisan selection
prepare = StrictPartialOrder(nodes=[ms, vv, mi, asel])
prepare.order.add_edge(ms, vv)
prepare.order.add_edge(vv, mi)
prepare.order.add_edge(mi, asel)

# 2. Order management: customization and approval
order_mgmt = StrictPartialOrder(nodes=[oc, da])
order_mgmt.order.add_edge(oc, da)

# 3. Handcrafting with continuous skill feedback loop
handcraft_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[hc, sf]
)

# 4. Packaging and sustainability audit in parallel
pack_sust = StrictPartialOrder(nodes=[pd, sa])
# no edges => concurrent

# 5. Dynamic pricing/inventory sync loop
pricing_seq = StrictPartialOrder(nodes=[pu, inv])
pricing_seq.order.add_edge(pu, inv)
skip_pricing = SilentTransition()
pricing_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pricing_seq, skip_pricing]
)

# 6. Retailer onboarding choice (or skip)
skip_retail = SilentTransition()
retailer_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[ro, skip_retail]
)

# 7. Build the root partial order
root = StrictPartialOrder(nodes=[
    prepare,
    order_mgmt,
    ws,
    handcraft_loop,
    qc,
    pack_sust,
    pricing_loop,
    retailer_choice
])

# Define the control-flow dependencies
root.order.add_edge(prepare, ws)
root.order.add_edge(order_mgmt, ws)
root.order.add_edge(ws, handcraft_loop)
root.order.add_edge(handcraft_loop, qc)
root.order.add_edge(qc, pack_sust)
root.order.add_edge(pack_sust, pricing_loop)
root.order.add_edge(pricing_loop, retailer_choice)