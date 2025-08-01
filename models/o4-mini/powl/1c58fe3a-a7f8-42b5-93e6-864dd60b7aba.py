# Generated from: 1c58fe3a-a7f8-42b5-93e6-864dd60b7aba.json
# Description: This process involves the intricate sourcing of rare cacao beans from remote micro-farms, followed by detailed quality assessments using sensory and chemical analyses. It includes negotiating fair-trade agreements, coordinating logistics through unconventional routes to preserve freshness, and managing relationships with indigenous growers. The process also encompasses seasonal forecasting, custom roasting profiles, and blending trials to craft unique chocolate flavors. Additionally, it integrates sustainability audits, packaging innovation, and niche market targeting before final distribution to boutique chocolatiers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
farm_scouting    = Transition(label='Farm scouting')
bean_testing     = Transition(label='Bean testing')
trade_negotiation= Transition(label='Trade negotiation')
route_planning   = Transition(label='Route planning')
grower_liaison   = Transition(label='Grower liaison')
season_forecast  = Transition(label='Season forecast')
roast_profiling  = Transition(label='Roast profiling')
blend_testing    = Transition(label='Blend testing')
sustain_audit    = Transition(label='Sustain audit')
packaging_design = Transition(label='Packaging design')
market_research  = Transition(label='Market research')
logistics_setup  = Transition(label='Logistics setup')
quality_review   = Transition(label='Quality review')
contract_signing = Transition(label='Contract signing')
distribution_prep= Transition(label='Distribution prep')

# Model the roast-and-blend loop (repeat roast→blend until satisfied)
roast_blend_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[roast_profiling, blend_testing]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    farm_scouting, bean_testing, season_forecast,
    trade_negotiation, grower_liaison, contract_signing,
    route_planning, logistics_setup, packaging_design,
    market_research, quality_review, sustain_audit,
    distribution_prep, roast_blend_loop
])

o = root.order
# Sourcing & initial quality
o.add_edge(farm_scouting, bean_testing)
o.add_edge(farm_scouting, season_forecast)

# Quality review triggers negotiation and can also go directly to final prep
o.add_edge(bean_testing, quality_review)
o.add_edge(quality_review, trade_negotiation)
o.add_edge(quality_review, distribution_prep)

# Negotiation → liaison → contract
o.add_edge(trade_negotiation, grower_liaison)
o.add_edge(grower_liaison, contract_signing)

# Contract → planning & audits
o.add_edge(contract_signing, route_planning)
o.add_edge(route_planning, logistics_setup)
o.add_edge(contract_signing, sustain_audit)

# Season forecasting feeds into the roast-blend loop
o.add_edge(season_forecast, roast_blend_loop)

# After loop: packaging & market research
o.add_edge(roast_blend_loop, packaging_design)
o.add_edge(roast_blend_loop, market_research)

# All streams converge into final distribution prep
o.add_edge(logistics_setup, distribution_prep)
o.add_edge(sustain_audit,   distribution_prep)
o.add_edge(packaging_design,distribution_prep)
o.add_edge(market_research, distribution_prep)