# Generated from: 5e622164-60ec-4761-a954-7551cd3b26b0.json
# Description: This process outlines the intricate coordination required in an artisan supply chain, where handcrafted goods are sourced, produced, and distributed with a focus on sustainability and cultural heritage. It involves raw material scouting in remote areas, quality validation by experts, adaptive production scheduling based on artisan availability, and bespoke packaging design. The process also integrates community feedback loops, dynamic pricing adjustments influenced by market trends, and specialized logistics management to ensure fragile items reach niche markets globally while maintaining ethical standards and minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
MaterialScout = Transition(label='Material Scout')
SampleTest = Transition(label='Sample Test')
ArtisanMatch = Transition(label='Artisan Match')
SchedulePlan = Transition(label='Schedule Plan')
ToolSetup = Transition(label='Tool Setup')
CraftProduce = Transition(label='Craft Produce')
QualityCheck = Transition(label='Quality Check')
FeedbackCollect = Transition(label='Feedback Collect')
PriceAdjust = Transition(label='Price Adjust')
PackageDesign = Transition(label='Package Design')
EcoLabeling = Transition(label='Eco Labeling')
OrderConfirm = Transition(label='Order Confirm')
LogisticsPlan = Transition(label='Logistics Plan')
ShipmentTrack = Transition(label='Shipment Track')
MarketReview = Transition(label='Market Review')
InventoryAudit = Transition(label='Inventory Audit')
CommunityEngage = Transition(label='Community Engage')

# Construct partial orders reflecting the process description:

# 1. Raw material scouting and quality validation:
# MaterialScout --> SampleTest
raw_and_quality = StrictPartialOrder(nodes=[MaterialScout, SampleTest])
raw_and_quality.order.add_edge(MaterialScout, SampleTest)

# 2. Adaptive production scheduling based on artisan availability:
# ArtisanMatch --> SchedulePlan
artisans_schedule = StrictPartialOrder(nodes=[ArtisanMatch, SchedulePlan])
artisans_schedule.order.add_edge(ArtisanMatch, SchedulePlan)

# 3. Tool setup before production
# SchedulePlan --> ToolSetup --> CraftProduce --> QualityCheck
production = StrictPartialOrder(nodes=[SchedulePlan, ToolSetup, CraftProduce, QualityCheck])
production.order.add_edge(SchedulePlan, ToolSetup)
production.order.add_edge(ToolSetup, CraftProduce)
production.order.add_edge(CraftProduce, QualityCheck)

# 4. Packaging design and eco labeling after quality check:
# PackageDesign --> EcoLabeling
packaging = StrictPartialOrder(nodes=[PackageDesign, EcoLabeling])
packaging.order.add_edge(PackageDesign, EcoLabeling)

# 5. Final order confirmation after eco labeling
order_confirm = StrictPartialOrder(nodes=[EcoLabeling, OrderConfirm])
order_confirm.order.add_edge(EcoLabeling, OrderConfirm)

# 6. Logistics plan and shipment tracking after order confirmation
logistics = StrictPartialOrder(nodes=[OrderConfirm, LogisticsPlan, ShipmentTrack])
logistics.order.add_edge(OrderConfirm, LogisticsPlan)
logistics.order.add_edge(LogisticsPlan, ShipmentTrack)

# 7. Market review and inventory audit can run concurrently, then influence price adjustment
market_inventory = StrictPartialOrder(nodes=[MarketReview, InventoryAudit])
# No edges: concurrent

price_adjust = OperatorPOWL(operator=Operator.XOR, children=[PriceAdjust, SilentTransition()]) # optional price adjust

# 8. Feedback collect and community engage form a loop with price adjustment:
# Loop: FeedbackCollect -> PriceAdjust (optional) -> back to FeedbackCollect or exit loop
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    FeedbackCollect,
    price_adjust
])

# Compose all partial orders into a bigger partial order:
# The higher level order:
# raw_and_quality --> artisans_schedule
# artisans_schedule --> production
# production --> packaging
# packaging --> order_confirm
# order_confirm --> logistics
# market_inventory runs concurrently with feedback_loop
# feedback_loop and market_inventory join before logistics

# Define one big PO combining these:
all_nodes = [
    raw_and_quality,
    artisans_schedule,
    production,
    packaging,
    order_confirm,
    logistics,
    market_inventory,
    feedback_loop,
    CommunityEngage
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges reflecting their order (partial order between submodels)
root.order.add_edge(raw_and_quality, artisans_schedule)
root.order.add_edge(artisans_schedule, production)
root.order.add_edge(production, packaging)
root.order.add_edge(packaging, order_confirm)
root.order.add_edge(order_confirm, logistics)

# market_inventory and feedback_loop concurrent, but both precede logistics
root.order.add_edge(market_inventory, logistics)
root.order.add_edge(feedback_loop, logistics)

# Add CommunityEngage as concurrent with market_inventory and feedback_loop but before logistics
# Since "community feedback loops" and "community engage" is likely related to feedback_loop and market_inventory
root.order.add_edge(CommunityEngage, logistics)

# CommunityEngage can run concurrently with market_inventory and feedback_loop (no edges between them)
# so no edges connecting CommunityEngage to market_inventory or feedback_loop

# The model captures:
# - MaterialScout and SampleTest sequential
# - ArtisanMatch and SchedulePlan sequential
# - Production sequence ToolSetup, CraftProduce, QualityCheck
# - Packaging and labeling sequence
# - Order confirm, logistics and shipment
# - Market review and inventory audit concurrently
# - Feedback and price adjust loop with optional price adjust skipping
# - Community engage as concurrent activity before logistics

# Return the final model in 'root'