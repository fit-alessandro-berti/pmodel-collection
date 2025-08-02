# Generated from: bda62501-19d1-43b9-a6f4-ec438f7e8e34.json
# Description: This process manages the sourcing, verification, and distribution of rare artisanal goods across multiple continents. It involves intricate coordination between local artisan communities, regional quality inspectors, international logistics teams, and digital marketplace platforms. The process ensures authenticity through multi-layered certification, incorporates environmental impact assessments, and adapts dynamically to geopolitical and climate-related disruptions while maintaining sustainable practices and ethical trade standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Artisan_Sourcing = Transition(label='Artisan Sourcing')
Material_Testing = Transition(label='Material Testing')
Quality_Audit = Transition(label='Quality Audit')
Certify_Origin = Transition(label='Certify Origin')
Carbon_Scan = Transition(label='Carbon Scan')
Risk_Mapping = Transition(label='Risk Mapping')
Contract_Draft = Transition(label='Contract Draft')
Local_Training = Transition(label='Local Training')
Inventory_Sync = Transition(label='Inventory Sync')
Customs_Filing = Transition(label='Customs Filing')
Freight_Booking = Transition(label='Freight Booking')
Damage_Inspect = Transition(label='Damage Inspect')
Market_Listing = Transition(label='Market Listing')
Demand_Forecast = Transition(label='Demand Forecast')
Sales_Report = Transition(label='Sales Report')
Feedback_Loop = Transition(label='Feedback Loop')
Reorder_Planning = Transition(label='Reorder Planning')

# Model multi-layered certification workflow:
# Artisan sourcing -> Material testing and Risk Mapping (concurrent) -> Quality Audit -> Certify Origin
certification_PO = StrictPartialOrder(
    nodes=[
        Artisan_Sourcing,
        Material_Testing,
        Risk_Mapping,
        Quality_Audit,
        Certify_Origin
    ]
)
certification_PO.order.add_edge(Artisan_Sourcing, Material_Testing)
certification_PO.order.add_edge(Artisan_Sourcing, Risk_Mapping)
certification_PO.order.add_edge(Material_Testing, Quality_Audit)
certification_PO.order.add_edge(Risk_Mapping, Quality_Audit)
certification_PO.order.add_edge(Quality_Audit, Certify_Origin)

# Environmental impact assessment: Carbon Scan after Risk Mapping (to reflect dynamic environmental risks)
env_PO = StrictPartialOrder(
    nodes=[Risk_Mapping, Carbon_Scan]
)
env_PO.order.add_edge(Risk_Mapping, Carbon_Scan)

# Contract draft and local training prepare for ethical trade and sustainability (after certification)
ethics_PO = StrictPartialOrder(
    nodes=[Certify_Origin, Contract_Draft, Local_Training]
)
ethics_PO.order.add_edge(Certify_Origin, Contract_Draft)
ethics_PO.order.add_edge(Certify_Origin, Local_Training)

# Logistics preparation: Inventory Sync -> Customs Filing -> Freight Booking -> Damage Inspect
logistics_PO = StrictPartialOrder(
    nodes=[Inventory_Sync, Customs_Filing, Freight_Booking, Damage_Inspect]
)
logistics_PO.order.add_edge(Inventory_Sync, Customs_Filing)
logistics_PO.order.add_edge(Customs_Filing, Freight_Booking)
logistics_PO.order.add_edge(Freight_Booking, Damage_Inspect)

# Market and sales activities: Demand Forecast -> Market Listing -> Sales Report
market_PO = StrictPartialOrder(
    nodes=[Demand_Forecast, Market_Listing, Sales_Report]
)
market_PO.order.add_edge(Demand_Forecast, Market_Listing)
market_PO.order.add_edge(Market_Listing, Sales_Report)

# Feedback and reorder planning form a loop with Market activities:
# Loop body: Feedback_Loop then Reorder_Planning then Market activities again
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Feedback_Loop,
        Reorder_Planning
    ]
)

# Combine market activities with loop: Market Listing and Sales Report before Feedback loop,
# Demand Forecast before Market Listing: loop is Feedback & Reorder planning, returning to market_PO
market_loop_PO = StrictPartialOrder(
    nodes=[
        Demand_Forecast,
        Market_Listing,
        Sales_Report,
        loop
    ]
)
market_loop_PO.order.add_edge(Demand_Forecast, Market_Listing)
market_loop_PO.order.add_edge(Market_Listing, Sales_Report)
market_loop_PO.order.add_edge(Sales_Report, loop)

# Final overall PO combines:
# 1. Certification + Environmental impact (Carbon Scan)
# 2. Ethics (Contract Draft + Local Training)
# 3. Logistics
# 4. Market activities + feedback loop
#
# Ordering:
# Carbon Scan after Risk Mapping is already defined.
# Environmental and certification precede ethics.
# Ethics precede logistics sync (Inventory Sync)
# Logistics precede market loop
# Note that artisan sourcing spawns certification (already defined)

root = StrictPartialOrder(
    nodes=[
        certification_PO,
        env_PO,
        ethics_PO,
        logistics_PO,
        market_loop_PO
    ]
)

# Edges between major blocks
root.order.add_edge(certification_PO, ethics_PO)      # Certification precedes ethics
root.order.add_edge(env_PO, ethics_PO)                # Environmental after Risk Mapping but before ethics
root.order.add_edge(ethics_PO, logistics_PO)          # Ethics before logistics
root.order.add_edge(logistics_PO, market_loop_PO)     # Logistics before market and feedback loop

# Add internal edges between certification_PO and env_PO to link Risk Mapping and Carbon Scan inside root order
# But these are included internally already, so here only for cross node relation
# Add edge from certification_PO to env_PO for their internal concurrency (to maintain partial order)
root.order.add_edge(certification_PO, env_PO)

# Model also concurrency between artisan sourcing and risk mapping inside certification_PO was done, but
# certification_PO and env_PO are nodes inside root, so define their connection here

# This completes the multi-layered complex process reflecting sourcing, certification, environmental,
# ethical, logistics, market, and feedback activities with partial order and loop structure
