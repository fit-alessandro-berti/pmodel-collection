# Generated from: 9bc95ec9-6b0a-4b56-b653-3878499008ee.json
# Description: This process describes the end-to-end supply chain for artisan cheese production and distribution, focusing on unique quality control, seasonal sourcing, and small-batch logistics. It begins with selecting rare milk breeds and continues through handcrafted cheese making, aging in controlled environments, specialized packaging, and niche market delivery. The process involves coordination between farmers, cheesemakers, quality inspectors, packaging specialists, and boutique retailers, ensuring each batch maintains distinct flavor profiles while adapting to fluctuating demand and regulatory compliance. Traceability and sustainability are emphasized throughout, requiring detailed record keeping and adaptive transport scheduling to preserve product integrity and freshness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the core activities
breed_select = Transition(label='Breed Select')
milk_collect = Transition(label='Milk Collect')
curd_form = Transition(label='Curd Form')
press_cheese = Transition(label='Press Cheese')
salt_cure = Transition(label='Salt Cure')
age_control = Transition(label='Age Control')
flavor_add = Transition(label='Flavor Add')
rind_treat = Transition(label='Rind Treat')
batch_label = Transition(label='Batch Label')
package_seal = Transition(label='Package Seal')
order_process = Transition(label='Order Process')
delivery_confirm = Transition(label='Delivery Confirm')
customer_feedback = Transition(label='Customer Feedback')

# Define loops for quality control, storage tracking, and transport scheduling
# Quality Test loop: repeat the test until it passes (silent rework)
quality_test = Transition(label='Quality Test')
loop_qc = OperatorPOWL(
    operator=Operator.LOOP,
    children=[quality_test, SilentTransition()]
)

# Storage tracking loop: record-keeping until ready to ship
storage_track = Transition(label='Storage Track')
loop_rr = OperatorPOWL(
    operator=Operator.LOOP,
    children=[storage_track, SilentTransition()]
)

# Transport planning loop: adapt route until finalized
route_plan = Transition(label='Route Plan')
loop_tp = OperatorPOWL(
    operator=Operator.LOOP,
    children=[route_plan, SilentTransition()]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    breed_select,
    milk_collect,
    loop_qc,
    curd_form,
    press_cheese,
    salt_cure,
    age_control,
    flavor_add,
    rind_treat,
    batch_label,
    package_seal,
    loop_rr,
    order_process,
    loop_tp,
    delivery_confirm,
    customer_feedback
])

# Define the control-flow relations
root.order.add_edge(breed_select, milk_collect)
root.order.add_edge(milk_collect, loop_qc)
root.order.add_edge(loop_qc, curd_form)

root.order.add_edge(curd_form, press_cheese)
root.order.add_edge(press_cheese, salt_cure)
root.order.add_edge(salt_cure, age_control)

root.order.add_edge(age_control, flavor_add)
root.order.add_edge(age_control, rind_treat)
root.order.add_edge(flavor_add, batch_label)
root.order.add_edge(rind_treat, batch_label)

root.order.add_edge(batch_label, package_seal)
root.order.add_edge(package_seal, loop_rr)
root.order.add_edge(loop_rr, order_process)

root.order.add_edge(order_process, loop_tp)
root.order.add_edge(loop_tp, delivery_confirm)
root.order.add_edge(delivery_confirm, customer_feedback)