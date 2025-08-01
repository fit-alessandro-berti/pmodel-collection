# Generated from: d17d4b27-980e-4733-9218-02ad61230552.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a densely populated city environment. It begins with site analysis and zoning compliance, followed by modular infrastructure design and climate control system integration. The process includes nutrient solution formulation, AI-driven crop monitoring, and energy optimization through renewable sources. Waste recycling and water reclamation activities ensure sustainability. Additionally, community engagement and educational outreach are integrated to promote urban agriculture awareness. The final stages focus on yield forecasting and supply chain coordination to deliver fresh produce efficiently to local markets, making this a highly specialized and multifaceted operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_analysis    = Transition(label='Site Analysis')
zoning_review    = Transition(label='Zoning Review')
modular_design   = Transition(label='Modular Design')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_selection   = Transition(label='Seed Selection')
ai_monitoring    = Transition(label='AI Monitoring')
lighting_control = Transition(label='Lighting Control')
energy_audit     = Transition(label='Energy Audit')
waste_sorting    = Transition(label='Waste Sorting')
water_reclaim    = Transition(label='Water Reclaim')
community_meet   = Transition(label='Community Meet')
staff_training   = Transition(label='Staff Training')
yield_forecast   = Transition(label='Yield Forecast')
market_sync      = Transition(label='Market Sync')
supply_chain     = Transition(label='Supply Chain')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    site_analysis, zoning_review,
    modular_design, climate_setup,
    nutrient_mix, seed_selection,
    ai_monitoring, lighting_control, energy_audit,
    waste_sorting, water_reclaim,
    community_meet, staff_training,
    yield_forecast, market_sync, supply_chain
])

# Site analysis and zoning review must finish before design and climate setup
root.order.add_edge(site_analysis, modular_design)
root.order.add_edge(zoning_review, modular_design)
root.order.add_edge(site_analysis, climate_setup)
root.order.add_edge(zoning_review, climate_setup)

# Design and climate setup precede nutrient mix
root.order.add_edge(modular_design, nutrient_mix)
root.order.add_edge(climate_setup, nutrient_mix)

# Nutrient mix precedes seed selection
root.order.add_edge(nutrient_mix, seed_selection)

# After seed selection, monitoring, lighting, and energy audit can run
root.order.add_edge(seed_selection, ai_monitoring)
root.order.add_edge(seed_selection, lighting_control)
root.order.add_edge(seed_selection, energy_audit)

# Sustainability steps depend on all three operations
for pred in [ai_monitoring, lighting_control, energy_audit]:
    root.order.add_edge(pred, waste_sorting)
    root.order.add_edge(pred, water_reclaim)

# Community engagement and training after sustainability
root.order.add_edge(waste_sorting, community_meet)
root.order.add_edge(waste_sorting, staff_training)
root.order.add_edge(water_reclaim, community_meet)
root.order.add_edge(water_reclaim, staff_training)

# Final stages: forecasting, market sync, then supply chain
root.order.add_edge(community_meet, yield_forecast)
root.order.add_edge(staff_training, yield_forecast)
root.order.add_edge(yield_forecast, market_sync)
root.order.add_edge(market_sync, supply_chain)