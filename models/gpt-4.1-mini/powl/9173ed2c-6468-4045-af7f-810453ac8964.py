# Generated from: 9173ed2c-6468-4045-af7f-810453ac8964.json
# Description: This process outlines the intricate supply chain management for an artisan cheese producer specializing in rare, aged varieties. It involves sourcing unique milk from selected farms, monitoring fermentation environments, managing aging conditions in specialized caves, coordinating packaging with hand-labeling, and ensuring traceability through blockchain recording. The process also includes quality inspections at multiple stages, custom order handling from boutique retailers, logistics planning for temperature-controlled transport, and real-time inventory balancing to meet fluctuating demand while preserving product integrity and artisanal value.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
FarmSourcing = Transition(label='Farm Sourcing')
MilkTesting = Transition(label='Milk Testing')
BatchMixing = Transition(label='Batch Mixing')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
MoldInoculation = Transition(label='Mold Inoculation')
FermentationCheck = Transition(label='Fermentation Check')
CaveAging = Transition(label='Cave Aging')
QualityInspect1 = Transition(label='Quality Inspect')
HandLabeling = Transition(label='Hand Labeling')
OrderCustomizing = Transition(label='Order Customizing')
InventoryAudit = Transition(label='Inventory Audit')
PackagingPrep = Transition(label='Packaging Prep')
ColdTransport = Transition(label='Cold Transport')
BlockchainLog = Transition(label='Blockchain Log')
RetailCoordination = Transition(label='Retail Coordination')
DemandForecast = Transition(label='Demand Forecast')

# Assemble fermentation process partial order:
# Farm Sourcing --> Milk Testing --> Batch Mixing --> Curd Cutting --> Whey Draining --> Mold Inoculation --> Fermentation Check
fermentation = StrictPartialOrder(nodes=[
    FarmSourcing, MilkTesting, BatchMixing, CurdCutting, WheyDraining,
    MoldInoculation, FermentationCheck
])
fermentation.order.add_edge(FarmSourcing, MilkTesting)
fermentation.order.add_edge(MilkTesting, BatchMixing)
fermentation.order.add_edge(BatchMixing, CurdCutting)
fermentation.order.add_edge(CurdCutting, WheyDraining)
fermentation.order.add_edge(WheyDraining, MoldInoculation)
fermentation.order.add_edge(MoldInoculation, FermentationCheck)

# Aging and inspection sequence:
# Fermentation Check --> Cave Aging --> Quality Inspect
aging_quality = StrictPartialOrder(nodes=[FermentationCheck, CaveAging, QualityInspect1])
aging_quality.order.add_edge(FermentationCheck, CaveAging)
aging_quality.order.add_edge(CaveAging, QualityInspect1)

# Packaging and labeling partial order:
# Packaging Prep --> Hand Labeling --> Blockchain Log
packaging = StrictPartialOrder(nodes=[PackagingPrep, HandLabeling, BlockchainLog])
packaging.order.add_edge(PackagingPrep, HandLabeling)
packaging.order.add_edge(HandLabeling, BlockchainLog)

# Order and retail coordination partial order
order_retail = StrictPartialOrder(nodes=[OrderCustomizing, RetailCoordination])
# assume Order Customizing precedes Retail Coordination
order_retail.order.add_edge(OrderCustomizing, RetailCoordination)

# Logistics and inventory partial order:
# Demand Forecast --> Inventory Audit --> Cold Transport
logistics = StrictPartialOrder(nodes=[DemandForecast, InventoryAudit, ColdTransport])
logistics.order.add_edge(DemandForecast, InventoryAudit)
logistics.order.add_edge(InventoryAudit, ColdTransport)

# Merge packaging and order handling concurrently, both must finish before logistics (cold transport)
# packaging and order_retail are concurrent
packaging_order = StrictPartialOrder(nodes=[packaging, order_retail])
# no edges between packaging and order_retail (concurrent)

# Root partial order: fermentation --> aging_quality --> packaging & order --> logistics
root = StrictPartialOrder(
    nodes=[fermentation, aging_quality, packaging_order, logistics]
)
root.order.add_edge(fermentation, aging_quality)
root.order.add_edge(aging_quality, packaging_order)
root.order.add_edge(packaging_order, logistics)