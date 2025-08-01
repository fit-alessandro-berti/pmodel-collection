# Generated from: 64ab9206-9c38-44fb-a142-c385b1d69f18.json
# Description: This process manages the end-to-end supply chain for artisanal cheese production, from sourcing rare milk varieties to aging and packaging. It involves coordination between local farmers, quality testing labs, fermentation specialists, and niche distributors. The process ensures strict adherence to regional regulations, maintains traceability of each cheese batch, and incorporates seasonal adjustments for milk quality, climate effects, and aging times. It culminates in specialized logistics to deliver fresh, handcrafted cheese to gourmet retailers and direct customers while preserving optimal flavor and texture profiles throughout transit.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
milk_sourcing    = Transition(label='Milk Sourcing')
quality_check    = Transition(label='Quality Check')
milk_pasteurize  = Transition(label='Milk Pasteurize')
culture_add      = Transition(label='Culture Add')
curd_cutting     = Transition(label='Curd Cutting')
whey_drain       = Transition(label='Whey Drain')
mold_inoculate   = Transition(label='Mold Inoculate')
press_cheese     = Transition(label='Press Cheese')
salt_rub         = Transition(label='Salt Rub')
aging_monitor    = Transition(label='Aging Monitor')
humidity_adjust  = Transition(label='Humidity Adjust')
batch_label      = Transition(label='Batch Label')
packaging_prep   = Transition(label='Packaging Prep')
storage_assign   = Transition(label='Storage Assign')
order_dispatch   = Transition(label='Order Dispatch')
customer_notify  = Transition(label='Customer Notify')

# Choice: optionally inoculate with mold or skip
skip_mold = SilentTransition()
choice_mold = OperatorPOWL(
    operator=Operator.XOR,
    children=[mold_inoculate, skip_mold]
)

# Loop: monitor aging, then optionally adjust humidity, repeat until done
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_monitor, humidity_adjust]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_check,
    milk_pasteurize,
    culture_add,
    curd_cutting,
    whey_drain,
    choice_mold,
    press_cheese,
    salt_rub,
    aging_loop,
    batch_label,
    packaging_prep,
    storage_assign,
    order_dispatch,
    customer_notify
])

# Sequential control‐flow dependencies
root.order.add_edge(milk_sourcing,   quality_check)
root.order.add_edge(quality_check,   milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_add)
root.order.add_edge(culture_add,     curd_cutting)
root.order.add_edge(curd_cutting,    whey_drain)
root.order.add_edge(whey_drain,      choice_mold)
root.order.add_edge(choice_mold,     press_cheese)
root.order.add_edge(press_cheese,    salt_rub)
root.order.add_edge(salt_rub,        aging_loop)
root.order.add_edge(aging_loop,      batch_label)
root.order.add_edge(batch_label,     packaging_prep)
root.order.add_edge(packaging_prep,  storage_assign)
root.order.add_edge(storage_assign,  order_dispatch)
root.order.add_edge(order_dispatch,  customer_notify)