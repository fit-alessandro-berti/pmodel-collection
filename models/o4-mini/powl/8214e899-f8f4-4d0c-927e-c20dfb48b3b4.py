# Generated from: 8214e899-f8f4-4d0c-927e-c20dfb48b3b4.json
# Description: This process manages the end-to-end workflow for sourcing rare, handcrafted materials from remote artisan communities and integrating them into a luxury goods manufacturing pipeline. It involves delicate coordination between local cooperatives, quality verification through sensory and historical validation, sustainable logistics planning, custom tariff negotiations, and adaptive production scheduling to accommodate fluctuating artisan output while ensuring ethical sourcing standards and minimizing environmental impact throughout the supply chain lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SourceArtisans     = Transition(label='Source Artisans')
ValidateOrigins    = Transition(label='Validate Origins')
QualityInspect     = Transition(label='Quality Inspect')
NegotiateTariffs   = Transition(label='Negotiate Tariffs')
SchedulePickup     = Transition(label='Schedule Pickup')
CustomClearance    = Transition(label='Custom Clearance')
TransportGoods     = Transition(label='Transport Goods')
InventoryCheck     = Transition(label='Inventory Check')
MaterialTesting    = Transition(label='Material Testing')
SustainabilityAudit= Transition(label='Sustainability Audit')
AdjustProduction   = Transition(label='Adjust Production')
PackagingDesign    = Transition(label='Packaging Design')
FinalizeOrders     = Transition(label='Finalize Orders')
DistributeStock    = Transition(label='Distribute Stock')
FeedbackCollect    = Transition(label='Feedback Collect')
SupplierReview     = Transition(label='Supplier Review')

# Loop: do inventory check, then optionally perform supplier review and repeat
loop_inventory = OperatorPOWL(
    operator=Operator.LOOP,
    children=[InventoryCheck, SupplierReview]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    SourceArtisans, ValidateOrigins, QualityInspect,
    MaterialTesting, SustainabilityAudit,
    NegotiateTariffs, AdjustProduction,
    CustomClearance, SchedulePickup,
    TransportGoods, loop_inventory,
    PackagingDesign, FinalizeOrders,
    DistributeStock, FeedbackCollect
])

# Source & quality verification
root.order.add_edge(SourceArtisans, ValidateOrigins)
root.order.add_edge(ValidateOrigins, QualityInspect)

# Parallel testing & sustainability audit after quality inspect
root.order.add_edge(QualityInspect, MaterialTesting)
root.order.add_edge(QualityInspect, SustainabilityAudit)

# After both tests & audit, do tariff negotiation and adjust production in parallel
root.order.add_edge(MaterialTesting, NegotiateTariffs)
root.order.add_edge(SustainabilityAudit, NegotiateTariffs)
root.order.add_edge(MaterialTesting, AdjustProduction)
root.order.add_edge(SustainabilityAudit, AdjustProduction)

# Logistics planning & clearance
root.order.add_edge(NegotiateTariffs, CustomClearance)
root.order.add_edge(CustomClearance, SchedulePickup)
root.order.add_edge(SchedulePickup, TransportGoods)

# Upon arrival, loop on inventory check → supplier review until exit
root.order.add_edge(TransportGoods, loop_inventory)
root.order.add_edge(loop_inventory, PackagingDesign)

# Ensure production is adjusted before packaging
root.order.add_edge(AdjustProduction, PackagingDesign)

# Final packaging & distribution
root.order.add_edge(PackagingDesign, FinalizeOrders)
root.order.add_edge(FinalizeOrders, DistributeStock)
root.order.add_edge(DistributeStock, FeedbackCollect)