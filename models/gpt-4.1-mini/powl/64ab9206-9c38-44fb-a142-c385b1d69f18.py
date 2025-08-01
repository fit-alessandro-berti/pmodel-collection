# Generated from: 64ab9206-9c38-44fb-a142-c385b1d69f18.json
# Description: This process manages the end-to-end supply chain for artisanal cheese production, from sourcing rare milk varieties to aging and packaging. It involves coordination between local farmers, quality testing labs, fermentation specialists, and niche distributors. The process ensures strict adherence to regional regulations, maintains traceability of each cheese batch, and incorporates seasonal adjustments for milk quality, climate effects, and aging times. It culminates in specialized logistics to deliver fresh, handcrafted cheese to gourmet retailers and direct customers while preserving optimal flavor and texture profiles throughout transit.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_check = Transition(label='Quality Check')
milk_pasteurize = Transition(label='Milk Pasteurize')
culture_add = Transition(label='Culture Add')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
salt_rub = Transition(label='Salt Rub')
aging_monitor = Transition(label='Aging Monitor')
humidity_adjust = Transition(label='Humidity Adjust')
batch_label = Transition(label='Batch Label')
packaging_prep = Transition(label='Packaging Prep')
storage_assign = Transition(label='Storage Assign')
order_dispatch = Transition(label='Order Dispatch')
customer_notify = Transition(label='Customer Notify')

# The loop part models seasonal adjustments for milk quality, climate effects, and aging times.
# Let's consider humidity_adjust as adjustment, aging_monitor as monitoring
# Loop: Aging Monitor then either exit or Humidity Adjust then Aging Monitor (repeated)
loop_seasonal_adjust = OperatorPOWL(operator=Operator.LOOP, children=[aging_monitor, humidity_adjust])

# Partial order representing the flow from milk sourcing to packaging before final dispatch
# The flow splits after whey_drain into parallel activities mold_inoculate and press_cheese (concurrent)
# salt_rub comes after press_cheese
# The loop for aging_monitor and humidity_adjust comes after salt_rub (modeling seasonal adjustments)
# batch_label, packaging_prep, storage_assign follow in sequence
# Finally order_dispatch and customer_notify are concurrent final activities

root = StrictPartialOrder(
    nodes=[
        milk_sourcing, quality_check, milk_pasteurize, culture_add,
        curd_cutting, whey_drain, mold_inoculate, press_cheese,
        salt_rub, loop_seasonal_adjust, batch_label, packaging_prep,
        storage_assign, order_dispatch, customer_notify
    ]
)

# Define order (dependencies)
root.order.add_edge(milk_sourcing, quality_check)
root.order.add_edge(quality_check, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_add)
root.order.add_edge(culture_add, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)

# After whey_drain two concurrent branches start: mold_inoculate and press_cheese
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(whey_drain, press_cheese)

# salt_rub after press_cheese
root.order.add_edge(press_cheese, salt_rub)

# loop_seasonal_adjust (aging monitor and humidity adjust loop) after salt_rub
root.order.add_edge(salt_rub, loop_seasonal_adjust)

# batch_label after loop_seasonal_adjust
root.order.add_edge(loop_seasonal_adjust, batch_label)
root.order.add_edge(batch_label, packaging_prep)
root.order.add_edge(packaging_prep, storage_assign)

# order_dispatch and customer_notify start after storage_assign, concurrent
root.order.add_edge(storage_assign, order_dispatch)
root.order.add_edge(storage_assign, customer_notify)