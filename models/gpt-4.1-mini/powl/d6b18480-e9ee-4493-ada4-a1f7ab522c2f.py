# Generated from: d6b18480-e9ee-4493-ada4-a1f7ab522c2f.json
# Description: This process involves coordinating a decentralized network of artisan producers, raw material foragers, quality inspectors, and niche market distributors to deliver bespoke craft products. It includes sourcing rare materials, verifying authenticity through blockchain, managing seasonal production cycles, synchronizing handmade assembly timelines, and adapting logistics due to fluctuating artisan availability and handcrafted batch variability. The process also incorporates dynamic pricing based on demand insights and artisan reputation, ensures compliance with local cultural heritage laws, and integrates direct customer feedback loops for continuous product refinement. This atypical supply chain balances traditional craftsmanship with modern digital tools to maintain unique product integrity while scaling niche artisan markets internationally.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Material_Sourcing = Transition(label='Material Sourcing')
Forager_Dispatch = Transition(label='Forager Dispatch')
Authenticity_Check = Transition(label='Authenticity Check')
Batch_Scheduling = Transition(label='Batch Scheduling')
Artisan_Allocation = Transition(label='Artisan Allocation')
Craft_Assembly = Transition(label='Craft Assembly')
Quality_Inspection = Transition(label='Quality Inspection')
Blockchain_Update = Transition(label='Blockchain Update')
Demand_Forecast = Transition(label='Demand Forecast')
Price_Adjustment = Transition(label='Price Adjustment')
Compliance_Review = Transition(label='Compliance Review')
Logistics_Planning = Transition(label='Logistics Planning')
Distributor_Sync = Transition(label='Distributor Sync')
Customer_Feedback = Transition(label='Customer Feedback')
Product_Refinement = Transition(label='Product Refinement')
Reputation_Audit = Transition(label='Reputation Audit')
Seasonal_Review = Transition(label='Seasonal Review')

# Model seasonal cycle as a loop:
# Batch_Scheduling initiates seasonal production cycle,
# Seasonal_Review adjusts or repeats batch scheduling.
seasonal_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Batch_Scheduling, Seasonal_Review]
)

# Model feedback loop for product refinement:
# Customer_Feedback leads to Product_Refinement which feeds back to Craft_Assembly
feedback_po = StrictPartialOrder(
    nodes=[Customer_Feedback, Product_Refinement, Craft_Assembly]
)
feedback_po.order.add_edge(Customer_Feedback, Product_Refinement)
feedback_po.order.add_edge(Product_Refinement, Craft_Assembly)

# Model reputation audit and dynamic pricing as a partial order:
# Demand_Forecast precedes Price_Adjustment and Reputation_Audit (concurrent)
pricing_po = StrictPartialOrder(
    nodes=[Demand_Forecast, Price_Adjustment, Reputation_Audit]
)
pricing_po.order.add_edge(Demand_Forecast, Price_Adjustment)
pricing_po.order.add_edge(Demand_Forecast, Reputation_Audit)

# Model supply chain sourcing and validation flow:
# Material_Sourcing -> Forager_Dispatch -> Authenticity_Check -> Blockchain_Update
sourcing_po = StrictPartialOrder(
    nodes=[Material_Sourcing, Forager_Dispatch, Authenticity_Check, Blockchain_Update]
)
sourcing_po.order.add_edge(Material_Sourcing, Forager_Dispatch)
sourcing_po.order.add_edge(Forager_Dispatch, Authenticity_Check)
sourcing_po.order.add_edge(Authenticity_Check, Blockchain_Update)

# Model artisan allocation and craft assembly flow:
# Artisan_Allocation -> Craft_Assembly -> Quality_Inspection
artisan_po = StrictPartialOrder(
    nodes=[Artisan_Allocation, Craft_Assembly, Quality_Inspection]
)
artisan_po.order.add_edge(Artisan_Allocation, Craft_Assembly)
artisan_po.order.add_edge(Craft_Assembly, Quality_Inspection)

# Compliance review stands before logistics planning and distributor sync
compliance_po = StrictPartialOrder(
    nodes=[Compliance_Review, Logistics_Planning, Distributor_Sync]
)
compliance_po.order.add_edge(Compliance_Review, Logistics_Planning)
compliance_po.order.add_edge(Compliance_Review, Distributor_Sync)

# Combine logistics and distribution as concurrent nodes synced afterwards:
logistics_sync_po = StrictPartialOrder(
    nodes=[Logistics_Planning, Distributor_Sync]
)  # No order between these two means concurrent

# Now build overall process partial order:

# Nodes: all the main components above plus seasonal_loop, pricing_po, feedback_po combined
root = StrictPartialOrder(
    nodes=[
        sourcing_po,
        artisan_po,
        seasonal_loop,
        pricing_po,
        compliance_po,
        feedback_po
    ]
)

# Define ordering between big blocks:

# Sourcing leads to artisan allocation
root.order.add_edge(sourcing_po, artisan_po)

# After artisan allocation and quality inspection, start seasonal loop
root.order.add_edge(artisan_po, seasonal_loop)

# Seasonal loop ends, then pricing decisions
root.order.add_edge(seasonal_loop, pricing_po)

# Pricing and reputation audit precede compliance review
root.order.add_edge(pricing_po, compliance_po)

# Compliance review precedes customer feedback process (product refinement loop)
root.order.add_edge(compliance_po, feedback_po)