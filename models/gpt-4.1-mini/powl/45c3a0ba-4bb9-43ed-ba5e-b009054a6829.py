# Generated from: 45c3a0ba-4bb9-43ed-ba5e-b009054a6829.json
# Description: This process outlines the intricate journey of artisan coffee beans from origin to cup, incorporating sustainable sourcing, quality verification, and direct farmer engagement. It involves coordinating micro-lot harvests, implementing blockchain traceability, specialized roasting profiles, and personalized distribution channels to ensure freshness and ethical standards. The process also integrates customer feedback loops for continuous blend refinement and adapts dynamically to seasonal crop variations and market demand fluctuations while maintaining transparency and premium quality assurance throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Farm_Selection = Transition(label='Farm Selection')
Lot_Harvest = Transition(label='Lot Harvest')
Sample_Testing = Transition(label='Sample Testing')
Trace_Logging = Transition(label='Trace Logging')
Quality_Audit = Transition(label='Quality Audit')
Farmer_Payment = Transition(label='Farmer Payment')
Roast_Profiling = Transition(label='Roast Profiling')
Batch_Roasting = Transition(label='Batch Roasting')
Flavor_Tasting = Transition(label='Flavor Tasting')
Packaging_Seal = Transition(label='Packaging Seal')
Inventory_Check = Transition(label='Inventory Check')
Order_Allocation = Transition(label='Order Allocation')
Delivery_Routing = Transition(label='Delivery Routing')
Customer_Feedback = Transition(label='Customer Feedback')
Blend_Refinement = Transition(label='Blend Refinement')
Market_Analysis = Transition(label='Market Analysis')
Demand_Forecast = Transition(label='Demand Forecast')

# Sustainability & sourcing partial order:
# Farm Selection -> Lot Harvest and Sample Testing parallel
sourcing = StrictPartialOrder(
    nodes=[Farm_Selection, Lot_Harvest, Sample_Testing]
)
sourcing.order.add_edge(Farm_Selection, Lot_Harvest)
sourcing.order.add_edge(Farm_Selection, Sample_Testing)

# Traceability partial order:
# Sample Testing -> Trace Logging -> Quality Audit -> Farmer Payment
traceability = StrictPartialOrder(
    nodes=[Sample_Testing, Trace_Logging, Quality_Audit, Farmer_Payment]
)
traceability.order.add_edge(Sample_Testing, Trace_Logging)
traceability.order.add_edge(Trace_Logging, Quality_Audit)
traceability.order.add_edge(Quality_Audit, Farmer_Payment)

# Roasting partial order:
# Roast Profiling -> Batch Roasting -> Flavor Tasting
roasting = StrictPartialOrder(
    nodes=[Roast_Profiling, Batch_Roasting, Flavor_Tasting]
)
roasting.order.add_edge(Roast_Profiling, Batch_Roasting)
roasting.order.add_edge(Batch_Roasting, Flavor_Tasting)

# Packaging and delivery partial order:
# Packaging Seal -> Inventory Check -> Order Allocation -> Delivery Routing
packaging_delivery = StrictPartialOrder(
    nodes=[Packaging_Seal, Inventory_Check, Order_Allocation, Delivery_Routing]
)
packaging_delivery.order.add_edge(Packaging_Seal, Inventory_Check)
packaging_delivery.order.add_edge(Inventory_Check, Order_Allocation)
packaging_delivery.order.add_edge(Order_Allocation, Delivery_Routing)

# Feedback and blend refinement loop:
# LOOP: 
#  - Execute Customer Feedback
#  - Choose exit or Blend Refinement then back to Customer Feedback
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Customer_Feedback, Blend_Refinement]
)

# Market analysis and demand forecast partial order - these can happen concurrently with feedback loop
market_demand = StrictPartialOrder(
    nodes=[Market_Analysis, Demand_Forecast]
)

# Combine all major parts in a partial order with dependencies and concurrency:
# - After sourcing is done, traceability proceeds
# - Roast Profiling can start after Farmer Payment (payment completes supply chain)
# - Packaging & delivery start after Flavor Tasting (roasting finished)
# - Market/demand and feedback loop run concurrently with packaging & delivery
root = StrictPartialOrder(
    nodes=[
        sourcing, 
        traceability, 
        roasting, 
        packaging_delivery,
        feedback_loop,
        market_demand
    ]
)

# Edges between these big phases to reflect the dependencies:
root.order.add_edge(sourcing, traceability)          # sourcing -> traceability
root.order.add_edge(traceability, roasting)          # traceability -> roasting
root.order.add_edge(roasting, packaging_delivery)    # roasting -> packaging/delivery

# Feedback loop and market/demand run concurrently with packaging/delivery, so no edges needed
