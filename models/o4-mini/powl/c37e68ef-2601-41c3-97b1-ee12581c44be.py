# Generated from: c37e68ef-2601-41c3-97b1-ee12581c44be.json
# Description: This process covers the end-to-end supply chain for artisan cheese production, starting from raw milk sourcing through quality verification, fermentation control, and aging management. It includes packaging design customization, niche market distribution, and feedback integration for continuous product refinement. The process also involves regulatory compliance checks, seasonal inventory adjustments, and collaborative marketing campaigns to strengthen brand presence in specialty food markets. Stakeholder coordination ensures timely deliveries while maintaining product integrity throughout transit and storage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
ms    = Transition(label='Milk Sourcing')
qt    = Transition(label='Quality Testing')
cc    = Transition(label='Compliance Check')
sp    = Transition(label='Starter Prep')
curd  = Transition(label='Curd Cutting')
wd    = Transition(label='Whey Draining')
mp    = Transition(label='Molding Press')
fc    = Transition(label='Fermentation Control')
age   = Transition(label='Aging Setup')
hc    = Transition(label='Humidity Check')
pd    = Transition(label='Packaging Design')
la    = Transition(label='Label Approval')
ia    = Transition(label='Inventory Audit')
osch  = Transition(label='Order Scheduling')
md    = Transition(label='Market Delivery')
mrk   = Transition(label='Marketing Sync')
fr    = Transition(label='Feedback Review')

# Define the packaging-design loop: do Packaging Design, then optionally Feedback Review, looping
pack_loop = OperatorPOWL(operator=Operator.LOOP, children=[pd, fr])

# Define the seasonal inventory loop: do Inventory Audit, then optionally Order Scheduling, looping
inv_loop  = OperatorPOWL(operator=Operator.LOOP, children=[ia, osch])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        ms, qt, cc, sp, curd, wd, mp, fc, age, hc,
        pack_loop, la, inv_loop,
        md, mrk
    ]
)

# Establish the control-flow ordering
edges = [
    (ms,   qt),
    (qt,   cc),
    (cc,   sp),
    (sp,   curd),
    (curd, wd),
    (wd,   mp),
    (mp,   fc),
    (fc,   age),
    (age,  hc),
    (hc,   pack_loop),
    (pack_loop, la),
    (la,   inv_loop),
    (inv_loop, md),
    (inv_loop, mrk)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)