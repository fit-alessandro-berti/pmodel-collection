# Generated from: 4b80fd54-71a4-4804-a238-6583b20ab3f5.json
# Description: This process manages the end-to-end flow of rare artisan materials from ethically sourced rural suppliers to luxury handcrafted product manufacturers. It involves scouting unique raw material providers, verifying authenticity, coordinating special transport methods to preserve quality, scheduling precise delivery windows, conducting multi-stage quality inspections, managing artisan contracts, and integrating customer feedback for continuous product refinement. The process must handle irregular supply schedules, fluctuating demand, and maintain strong relationships with niche suppliers while ensuring compliance with international trade regulations and sustainability standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
supplier_scout    = Transition(label='Supplier Scout')
auth_verify       = Transition(label='Auth Verify')
sample_collect    = Transition(label='Sample Collect')
quality_inspect   = Transition(label='Quality Inspect')
transport_setup   = Transition(label='Transport Setup')
customs_clear     = Transition(label='Customs Clear')
shipment_track    = Transition(label='Shipment Track')
inventory_log     = Transition(label='Inventory Log')
order_confirm     = Transition(label='Order Confirm')
schedule_pickup   = Transition(label='Schedule Pickup')
artisan_assign    = Transition(label='Artisan Assign')
contract_review   = Transition(label='Contract Review')
product_assemble  = Transition(label='Product Assemble')
final_inspect     = Transition(label='Final Inspect')
feedback_gather   = Transition(label='Feedback Gather')
demand_forecast   = Transition(label='Demand Forecast')
sustain_audit     = Transition(label='Sustain Audit')

# Silent transition for loop exits
tau = SilentTransition()

# 1) Handle irregular supply: loop supplier scouting until ready
supplier_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        StrictPartialOrder(nodes=[supplier_scout]),  # body: scout once
        tau                                         # redo: silent, then body again
    ]
)

# 2) Handle repeated sampling & inspection until quality OK
sample_inspect_seq = StrictPartialOrder(nodes=[sample_collect, quality_inspect])
sample_inspect_seq.order.add_edge(sample_collect, quality_inspect)

quality_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        sample_inspect_seq,  # do sample->inspect
        tau                  # if not OK, silent then repeat
    ]
)

# 3) Transportation & logistics (some parallelism)
transport_po = StrictPartialOrder(nodes=[
    transport_setup, customs_clear, schedule_pickup,
    shipment_track, inventory_log
])
transport_po.order.add_edge(transport_setup, customs_clear)
transport_po.order.add_edge(customs_clear, schedule_pickup)
# after customs you can log inventory
transport_po.order.add_edge(customs_clear, inventory_log)
# after scheduling pickup you track shipment
transport_po.order.add_edge(schedule_pickup, shipment_track)

# 4) Artisan production sequence
production_po = StrictPartialOrder(nodes=[
    order_confirm, artisan_assign, contract_review,
    product_assemble, final_inspect
])
production_po.order.add_edge(order_confirm, artisan_assign)
production_po.order.add_edge(artisan_assign, contract_review)
production_po.order.add_edge(contract_review, product_assemble)
production_po.order.add_edge(product_assemble, final_inspect)

# 5) Continuous improvement loop: demand forecasting, feedback, sustainability audit
improvement_seq = StrictPartialOrder(nodes=[
    demand_forecast, feedback_gather, sustain_audit
])
improvement_seq.order.add_edge(demand_forecast, feedback_gather)
improvement_seq.order.add_edge(feedback_gather, sustain_audit)

improvement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        improvement_seq,  # body: forecast->feedback->audit
        tau               # redo: silent, then body again
    ]
)

# 6) Assemble the overall process
root = StrictPartialOrder(nodes=[
    supplier_loop, auth_verify, quality_loop,
    transport_po, production_po, improvement_loop
])
# end-to-end ordering
root.order.add_edge(supplier_loop, auth_verify)
root.order.add_edge(auth_verify, quality_loop)
root.order.add_edge(quality_loop, transport_po)
root.order.add_edge(transport_po, production_po)
root.order.add_edge(production_po, improvement_loop)