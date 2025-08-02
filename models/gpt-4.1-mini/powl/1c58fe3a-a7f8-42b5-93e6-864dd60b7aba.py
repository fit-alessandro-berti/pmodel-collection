# Generated from: 1c58fe3a-a7f8-42b5-93e6-864dd60b7aba.json
# Description: This process involves the intricate sourcing of rare cacao beans from remote micro-farms, followed by detailed quality assessments using sensory and chemical analyses. It includes negotiating fair-trade agreements, coordinating logistics through unconventional routes to preserve freshness, and managing relationships with indigenous growers. The process also encompasses seasonal forecasting, custom roasting profiles, and blending trials to craft unique chocolate flavors. Additionally, it integrates sustainability audits, packaging innovation, and niche market targeting before final distribution to boutique chocolatiers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
farm_scouting = Transition(label='Farm scouting')
bean_testing = Transition(label='Bean testing')
trade_negotiation = Transition(label='Trade negotiation')
route_planning = Transition(label='Route planning')
grower_liaison = Transition(label='Grower liaison')
season_forecast = Transition(label='Season forecast')
roast_profiling = Transition(label='Roast profiling')
blend_testing = Transition(label='Blend testing')
sustain_audit = Transition(label='Sustain audit')
packaging_design = Transition(label='Packaging design')
market_research = Transition(label='Market research')
logistics_setup = Transition(label='Logistics setup')
quality_review = Transition(label='Quality review')
contract_signing = Transition(label='Contract signing')
distribution_prep = Transition(label='Distribution prep')

# Structure based on description:

# 1. Farm scouting happens and can be concurrent with season forecast
# (season forecast is done early and independently)
# 2. After farm scouting comes bean testing and quality review (quality review after bean testing)
# 3. Trade negotiation and contract signing happen after quality review
# 4. Grower liaison can happen concurrently with route planning and logistics setup (which also include market research)
# 5. Route planning -> logistics setup (logistics depends on route planning)
# 6. Sustainability audit, packaging design, and market research happen concurrently before distribution prep.
# 7. Roast profiling and blend testing come after contract signing
# 8. Distribution prep happens last, after all prior activities

# PartialOrders for some groups to show concurrent and ordering relations

# Step 1+2
po_quality = StrictPartialOrder(nodes=[bean_testing, quality_review])
po_quality.order.add_edge(bean_testing, quality_review)

po_scouting_season = StrictPartialOrder(nodes=[farm_scouting, season_forecast])
# concurrent, no edges

# Step 3
po_trade = StrictPartialOrder(nodes=[trade_negotiation, contract_signing])
po_trade.order.add_edge(trade_negotiation, contract_signing)

# Step 4+5
po_logistics = StrictPartialOrder(nodes=[route_planning, logistics_setup, market_research])
po_logistics.order.add_edge(route_planning, logistics_setup)
# market research concurrent with logistics setup (no edge)
grower_logistics = StrictPartialOrder(nodes=[grower_liaison, po_logistics])
# grower liaison concurrent with logistics setup subtree (no edge between grower_liaison and po_logistics's nodes)

# Step 6 concurrent group before distribution prep
po_pre_distribution = StrictPartialOrder(nodes=[sustain_audit, packaging_design, market_research])
# All concurrent (no edges)

# Step 7 roast and blend, after contract signing
po_roast_blend = StrictPartialOrder(nodes=[roast_profiling, blend_testing])
po_roast_blend.order.add_edge(roast_profiling, blend_testing)

# Now assemble the bigger structure:
# farm_scouting -> bean_testing -> quality_review -> trade_negotiation -> contract_signing -> roast_profiling -> blend_testing

# From contract_signing -> after: grower liaison/logistics subtree and po_pre_distribution and finally distribution_prep

root = StrictPartialOrder(nodes=[
    farm_scouting,
    season_forecast,
    po_quality,
    po_trade,
    po_roast_blend,
    grower_logistics,
    sustain_audit,
    packaging_design,
    market_research,
    distribution_prep
])

# Add order edges for the main sequence
root.order.add_edge(farm_scouting, po_quality)
root.order.add_edge(po_quality, po_trade)
root.order.add_edge(po_trade, po_roast_blend)

# After roast and blend, start grower liaison/logistics, sustain audit, packaging design, market research
root.order.add_edge(po_roast_blend, grower_logistics)
root.order.add_edge(po_roast_blend, sustain_audit)
root.order.add_edge(po_roast_blend, packaging_design)

# market_research appears twice - unify usage:
# It is inside grower_logistics (logistics_setup, route_planning, market_research)
# and also as concurrent before distribution_prep - to avoid duplicates, remove from grower_logistics nodes and add explicitly here

# To fix that, remove market_research from po_logistics and from po_pre_distribution, add only once before distribution_prep

# Adjust grower_logistics without market_research
po_logistics = StrictPartialOrder(nodes=[route_planning, logistics_setup])
po_logistics.order.add_edge(route_planning, logistics_setup)

grower_logistics = StrictPartialOrder(nodes=[grower_liaison, po_logistics])
# no edges between grower_liaison and po_logistics nodes

po_pre_distribution = StrictPartialOrder(nodes=[sustain_audit, packaging_design, market_research])
# all concurrent

# Redefine root nodes and edges with these fixes
root = StrictPartialOrder(nodes=[
    farm_scouting,
    season_forecast,
    po_quality,
    po_trade,
    po_roast_blend,
    grower_logistics,
    po_pre_distribution,
    distribution_prep
])

root.order.add_edge(farm_scouting, po_quality)
root.order.add_edge(po_quality, po_trade)
root.order.add_edge(po_trade, po_roast_blend)
root.order.add_edge(po_roast_blend, grower_logistics)
root.order.add_edge(po_roast_blend, po_pre_distribution)
# grower_logistics and po_pre_distribution concurrent, no edges between them

root.order.add_edge(grower_logistics, distribution_prep)
root.order.add_edge(po_pre_distribution, distribution_prep)

# The season_forecast happens concurrently early, no edges to farm_scouting needed

# Final root