# Generated from: a97ec77a-8db8-4ffa-b3ff-7b0d199f273c.json
# Description: This process involves sourcing rare artisan cheeses from multiple small-scale farms, ensuring compliance with diverse international food safety standards, coordinating cold-chain logistics for perishable goods, handling customs documentation unique to dairy products, conducting quality assurance tests at multiple checkpoints, and managing niche market distribution channels to premium retailers and specialty stores worldwide. The process demands meticulous tracking of batch provenance, temperature-controlled packaging innovations, and adaptive scheduling to accommodate variable production cycles and fluctuating demand in global luxury markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

FarmSourcing = Transition(label='Farm Sourcing')
BatchTesting = Transition(label='Batch Testing')
SafetyAudit = Transition(label='Safety Audit')
ColdPacking = Transition(label='Cold Packing')
LabelDesign = Transition(label='Label Design')
CustomsFiling = Transition(label='Customs Filing')
LogisticsBooking = Transition(label='Logistics Booking')
TemperatureCheck = Transition(label='Temperature Check')
QualityControl = Transition(label='Quality Control')
ComplianceReview = Transition(label='Compliance Review')
MarketAnalysis = Transition(label='Market Analysis')
OrderProcessing = Transition(label='Order Processing')
InventorySync = Transition(label='Inventory Sync')
RetailCoordination = Transition(label='Retail Coordination')
DeliveryTracking = Transition(label='Delivery Tracking')

# Partial order for sourcing and compliance checks (parallel where possible)
# Farm Sourcing -> Batch Testing and Safety Audit (can be concurrent)
source_check = StrictPartialOrder(nodes=[FarmSourcing, BatchTesting, SafetyAudit])
source_check.order.add_edge(FarmSourcing, BatchTesting)
source_check.order.add_edge(FarmSourcing, SafetyAudit)

# Parallel packing: ColdPacking followed by TemperatureCheck and LabelDesign (concurrent)
packing = StrictPartialOrder(nodes=[ColdPacking, TemperatureCheck, LabelDesign])
packing.order.add_edge(ColdPacking, TemperatureCheck)
packing.order.add_edge(ColdPacking, LabelDesign)

# Customs and logistics are sequential but can have some concurrency with Packing
customs_logistics = StrictPartialOrder(nodes=[CustomsFiling, LogisticsBooking])
customs_logistics.order.add_edge(CustomsFiling, LogisticsBooking)

# Quality control steps: QualityControl then ComplianceReview (sequential)
quality = StrictPartialOrder(nodes=[QualityControl, ComplianceReview])
quality.order.add_edge(QualityControl, ComplianceReview)

# Market-facing activities: MarketAnalysis -> OrderProcessing -> InventorySync -> RetailCoordination -> DeliveryTracking
market = StrictPartialOrder(nodes=[MarketAnalysis, OrderProcessing, InventorySync, RetailCoordination, DeliveryTracking])
market.order.add_edge(MarketAnalysis, OrderProcessing)
market.order.add_edge(OrderProcessing, InventorySync)
market.order.add_edge(InventorySync, RetailCoordination)
market.order.add_edge(RetailCoordination, DeliveryTracking)

# Combine packing and customs_logistics in parallel (no orders between them)
pack_and_log = StrictPartialOrder(nodes=[packing, customs_logistics])

# Combine source_check and pack_and_log sequentially (packing/logistics after sourcing/check)
source_pack_log = StrictPartialOrder(nodes=[source_check, pack_and_log])
source_pack_log.order.add_edge(source_check, pack_and_log)

# Combine quality control after packing/logistics
full_before_market = StrictPartialOrder(nodes=[source_pack_log, quality])
full_before_market.order.add_edge(source_pack_log, quality)

# Finally combine market activities sequentially after quality control
root = StrictPartialOrder(nodes=[full_before_market, market])
root.order.add_edge(full_before_market, market)