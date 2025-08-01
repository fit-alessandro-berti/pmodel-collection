# Generated from: d17d4b27-980e-4733-9218-02ad61230552.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a densely populated city environment. It begins with site analysis and zoning compliance, followed by modular infrastructure design and climate control system integration. The process includes nutrient solution formulation, AI-driven crop monitoring, and energy optimization through renewable sources. Waste recycling and water reclamation activities ensure sustainability. Additionally, community engagement and educational outreach are integrated to promote urban agriculture awareness. The final stages focus on yield forecasting and supply chain coordination to deliver fresh produce efficiently to local markets, making this a highly specialized and multifaceted operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteAnalysis = Transition(label='Site Analysis')
ZoningReview = Transition(label='Zoning Review')
ModularDesign = Transition(label='Modular Design')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
SeedSelection = Transition(label='Seed Selection')
AIMonitoring = Transition(label='AI Monitoring')
LightingControl = Transition(label='Lighting Control')
EnergyAudit = Transition(label='Energy Audit')
WaterReclaim = Transition(label='Water Reclaim')
WasteSorting = Transition(label='Waste Sorting')
CommunityMeet = Transition(label='Community Meet')
StaffTraining = Transition(label='Staff Training')
YieldForecast = Transition(label='Yield Forecast')
MarketSync = Transition(label='Market Sync')
SupplyChain = Transition(label='Supply Chain')

# Site Analysis and Zoning Review are sequential
site_and_zoning = StrictPartialOrder(nodes=[SiteAnalysis, ZoningReview])
site_and_zoning.order.add_edge(SiteAnalysis, ZoningReview)

# Modular Design and Climate Setup sequential (following zoning)
modular_and_climate = StrictPartialOrder(nodes=[ModularDesign, ClimateSetup])
modular_and_climate.order.add_edge(ModularDesign, ClimateSetup)

# Nutrient Mix and Seed Selection concurrent (independent)
nutrients_and_seeds = StrictPartialOrder(nodes=[NutrientMix, SeedSelection])

# AI Monitoring and Lighting Control concurrent (crop monitoring + lighting)
ai_and_lighting = StrictPartialOrder(nodes=[AIMonitoring, LightingControl])

# Energy Audit (after lighting control)
energy_after_lighting = StrictPartialOrder(nodes=[LightingControl, EnergyAudit])
energy_after_lighting.order.add_edge(LightingControl, EnergyAudit)

# Waste Sorting and Water Reclaim concurrent sustainability activities
waste_and_water = StrictPartialOrder(nodes=[WasteSorting, WaterReclaim])

# Community Meeting and Staff Training concurrent community engagement activities
community_and_training = StrictPartialOrder(nodes=[CommunityMeet, StaffTraining])

# Yield Forecast followed by Market Sync and then Supply Chain sequentially
forecast_to_supply = StrictPartialOrder(nodes=[YieldForecast, MarketSync, SupplyChain])
forecast_to_supply.order.add_edge(YieldForecast, MarketSync)
forecast_to_supply.order.add_edge(MarketSync, SupplyChain)

# Connect sequences respecting partial order:
# site_and_zoning --> modular_and_climate
# modular_and_climate --> nutrients_and_seeds and
# nutrients_and_seeds --> ai_and_lighting
# ai_and_lighting --> energy_after_lighting and waste_and_water and community_and_training (all concurrent after)
# finally all join to forecast_to_supply

# Build a partial order with all above as nodes
root = StrictPartialOrder(
    nodes=[
        site_and_zoning,
        modular_and_climate,
        nutrients_and_seeds,
        ai_and_lighting,
        energy_after_lighting,
        waste_and_water,
        community_and_training,
        forecast_to_supply,
    ]
)

# Add edges between these to impose the described order
root.order.add_edge(site_and_zoning, modular_and_climate)
root.order.add_edge(modular_and_climate, nutrients_and_seeds)
root.order.add_edge(nutrients_and_seeds, ai_and_lighting)

root.order.add_edge(ai_and_lighting, energy_after_lighting)
root.order.add_edge(ai_and_lighting, waste_and_water)
root.order.add_edge(ai_and_lighting, community_and_training)

root.order.add_edge(energy_after_lighting, forecast_to_supply)
root.order.add_edge(waste_and_water, forecast_to_supply)
root.order.add_edge(community_and_training, forecast_to_supply)