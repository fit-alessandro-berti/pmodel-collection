# Generated from: 48d26c37-a630-47cf-8e08-02e96fd96c3c.json
# Description: This process outlines the end-to-end flow for producing and distributing artisanal cheese from small-scale farms. It begins with raw milk sourcing from select local farms, followed by quality testing and fermentation initiation under controlled conditions. The curdling phase involves precise temperature and humidity adjustments, then aging in specialized environments with regular monitoring. Packaging is done using eco-friendly materials, then the product undergoes certification for organic and regional authenticity. Distribution channels include farmer’s markets, boutique stores, and direct online sales, supported by customer feedback loops and inventory management to ensure freshness and demand alignment. Finally, waste materials are composted or repurposed, closing the sustainable cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
QualityTest = Transition(label='Quality Test')
FermentationStart = Transition(label='Fermentation Start')
CurdlingPhase = Transition(label='Curdling Phase')
TemperatureControl = Transition(label='Temperature Control')
HumidityAdjust = Transition(label='Humidity Adjust')
AgingMonitor = Transition(label='Aging Monitor')
EcoPackaging = Transition(label='Eco Packaging')
CertificationCheck = Transition(label='Certification Check')
MarketDistribution = Transition(label='Market Distribution')
StoreDelivery = Transition(label='Store Delivery')
OnlineSales = Transition(label='Online Sales')
FeedbackLoop = Transition(label='Feedback Loop')
InventoryAudit = Transition(label='Inventory Audit')
WasteCompost = Transition(label='Waste Compost')

# Curdling phase concurrency: Temperature Control and Humidity Adjust concurrent after Curdling Phase
curdling_sub = StrictPartialOrder(nodes=[CurdlingPhase, TemperatureControl, HumidityAdjust])
curdling_sub.order.add_edge(CurdlingPhase, TemperatureControl)
curdling_sub.order.add_edge(CurdlingPhase, HumidityAdjust)

# Aging with monitoring
aging_sub = StrictPartialOrder(nodes=[AgingMonitor])

# Distribution channels as a choice of Market, Store, Online sales
distribution_choice = OperatorPOWL(operator=Operator.XOR, children=[MarketDistribution, StoreDelivery, OnlineSales])

# Feedback and inventory after distribution in partial order
feedback_inventory = StrictPartialOrder(nodes=[FeedbackLoop, InventoryAudit])

# The overall flow:
# MilkSourcing -> QualityTest -> FermentationStart -> curdling_sub(phase + concurrent adj) -> aging_sub -> EcoPackaging -> CertificationCheck -> distribution_choice -> feedback_inventory -> WasteCompost

root = StrictPartialOrder(nodes=[MilkSourcing, QualityTest, FermentationStart, curdling_sub, aging_sub, EcoPackaging, CertificationCheck, distribution_choice, feedback_inventory, WasteCompost])
root.order.add_edge(MilkSourcing, QualityTest)
root.order.add_edge(QualityTest, FermentationStart)
root.order.add_edge(FermentationStart, curdling_sub)
root.order.add_edge(curdling_sub, aging_sub)
root.order.add_edge(aging_sub, EcoPackaging)
root.order.add_edge(EcoPackaging, CertificationCheck)
root.order.add_edge(CertificationCheck, distribution_choice)
root.order.add_edge(distribution_choice, feedback_inventory)
root.order.add_edge(feedback_inventory, WasteCompost)