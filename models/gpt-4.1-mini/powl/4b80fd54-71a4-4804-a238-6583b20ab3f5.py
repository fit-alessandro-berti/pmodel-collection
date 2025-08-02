# Generated from: 4b80fd54-71a4-4804-a238-6583b20ab3f5.json
# Description: This process manages the end-to-end flow of rare artisan materials from ethically sourced rural suppliers to luxury handcrafted product manufacturers. It involves scouting unique raw material providers, verifying authenticity, coordinating special transport methods to preserve quality, scheduling precise delivery windows, conducting multi-stage quality inspections, managing artisan contracts, and integrating customer feedback for continuous product refinement. The process must handle irregular supply schedules, fluctuating demand, and maintain strong relationships with niche suppliers while ensuring compliance with international trade regulations and sustainability standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
SupplierScout = Transition(label='Supplier Scout')
AuthVerify = Transition(label='Auth Verify')
SampleCollect = Transition(label='Sample Collect')
QualityInspect = Transition(label='Quality Inspect')
TransportSetup = Transition(label='Transport Setup')
CustomsClear = Transition(label='Customs Clear')
InventoryLog = Transition(label='Inventory Log')
OrderConfirm = Transition(label='Order Confirm')
SchedulePickup = Transition(label='Schedule Pickup')
ArtisanAssign = Transition(label='Artisan Assign')
ContractReview = Transition(label='Contract Review')
ProductAssemble = Transition(label='Product Assemble')
FinalInspect = Transition(label='Final Inspect')
FeedbackGather = Transition(label='Feedback Gather')
DemandForecast = Transition(label='Demand Forecast')
SustainAudit = Transition(label='Sustain Audit')
ShipmentTrack = Transition(label='Shipment Track')

# Model irregular supply schedules and fluctuating demand with XOR choices for supplier scouting and demand forecasting
supplier_choice = OperatorPOWL(operator=Operator.XOR, children=[SupplierScout, DemandForecast])

# Supply chain initial sequence: scout, verify auth, collect sample
initial_supply = StrictPartialOrder(nodes=[supplier_choice, AuthVerify, SampleCollect])
initial_supply.order.add_edge(supplier_choice, AuthVerify)
initial_supply.order.add_edge(AuthVerify, SampleCollect)

# Quality and transport partial order
quality_transport = StrictPartialOrder(nodes=[
    QualityInspect,
    TransportSetup,
    CustomsClear,
    InventoryLog
])
# QualityInspect must precede TransportSetup & CustomsClear, InventoryLog depends on CustomsClear
quality_transport.order.add_edge(QualityInspect, TransportSetup)
quality_transport.order.add_edge(QualityInspect, CustomsClear)
quality_transport.order.add_edge(CustomsClear, InventoryLog)

# Delivery scheduling and order confirmation partial order
delivery_order = StrictPartialOrder(nodes=[
    SchedulePickup,
    OrderConfirm
])
delivery_order.order.add_edge(SchedulePickup, OrderConfirm)

# Artisan management partial order: assign artisan, review contract, assemble product
artisan_management = StrictPartialOrder(nodes=[
    ArtisanAssign,
    ContractReview,
    ProductAssemble
])
artisan_management.order.add_edge(ArtisanAssign, ContractReview)
artisan_management.order.add_edge(ContractReview, ProductAssemble)

# Final inspection before shipment tracking
final_stage = StrictPartialOrder(nodes=[
    FinalInspect,
    ShipmentTrack
])
final_stage.order.add_edge(FinalInspect, ShipmentTrack)

# Feedback and sustainability audit can run concurrently after shipment tracking
feedback_sustain = StrictPartialOrder(nodes=[
    FeedbackGather,
    SustainAudit
])

# Combine the sequences in partial order for overall process
# 1) initial supply -> 2) quality_transport -> 3) delivery_order and artisan_management (concurrent) -> 4) final_stage -> 5) feedback_sustain

root = StrictPartialOrder(nodes=[
    initial_supply,
    quality_transport,
    delivery_order,
    artisan_management,
    final_stage,
    feedback_sustain
])

# Define control flow edges:
# initial_supply before quality_transport
root.order.add_edge(initial_supply, quality_transport)
# quality_transport before delivery_order and artisan_management (concurrent)
root.order.add_edge(quality_transport, delivery_order)
root.order.add_edge(quality_transport, artisan_management)
# delivery_order and artisan_management before final_stage
root.order.add_edge(delivery_order, final_stage)
root.order.add_edge(artisan_management, final_stage)
# final_stage before feedback_sustain
root.order.add_edge(final_stage, feedback_sustain)