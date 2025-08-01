# Generated from: cae103f2-cdc5-4785-8a7c-64cdd34232e4.json
# Description: This process outlines the complex steps involved in launching an urban vertical farming operation within a dense metropolitan area. It includes site acquisition, environmental impact assessment, modular infrastructure setup, multi-tier crop planting, automated nutrient management, integrated pest control, real-time growth monitoring, community engagement programs, yield forecasting, supply chain coordination, regulatory compliance verification, waste recycling systems, energy usage optimization, market entry strategy, and post-launch performance analysis to ensure sustainable urban agriculture and profitability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_acq         = Transition(label="Site Acquisition")
impact_assess    = Transition(label="Impact Assess")
modular_setup    = Transition(label="Modular Setup")
crop_planting    = Transition(label="Crop Planting")
nutrient_control = Transition(label="Nutrient Control")
pest_control     = Transition(label="Pest Control")
growth_monitor   = Transition(label="Growth Monitor")
community_engage = Transition(label="Community Engage")
yield_forecast   = Transition(label="Yield Forecast")
supply_coord     = Transition(label="Supply Coordinate")
compliance_check = Transition(label="Compliance Check")
waste_recycle    = Transition(label="Waste Recycle")
energy_optimize  = Transition(label="Energy Optimize")
market_strategy  = Transition(label="Market Strategy")
performance_rev  = Transition(label="Performance Review")

# Build a partial‐order where some tasks run in sequence,
# some run in parallel, and then rejoin.
root = StrictPartialOrder(nodes=[
    site_acq, impact_assess, modular_setup, crop_planting,
    nutrient_control, pest_control, growth_monitor, community_engage,
    yield_forecast, supply_coord, compliance_check, waste_recycle,
    energy_optimize, market_strategy, performance_rev
])

# Sequential ordering up to planting
root.order.add_edge(site_acq,      impact_assess)
root.order.add_edge(impact_assess, modular_setup)
root.order.add_edge(modular_setup, crop_planting)

# After planting: nutrient & pest in parallel
root.order.add_edge(crop_planting, nutrient_control)
root.order.add_edge(crop_planting, pest_control)

# Re‐synchronize before forecasting
root.order.add_edge(nutrient_control, growth_monitor)
root.order.add_edge(pest_control,     growth_monitor)

# Community engagement runs in parallel with growth monitoring
root.order.add_edge(growth_monitor,   community_engage)

# Both growth monitoring and community engagement must finish before forecasting
root.order.add_edge(growth_monitor, yield_forecast)
root.order.add_edge(community_engage, yield_forecast)

# Then the remaining sequence
root.order.add_edge(yield_forecast,   supply_coord)
root.order.add_edge(supply_coord,     compliance_check)
root.order.add_edge(compliance_check, waste_recycle)
root.order.add_edge(waste_recycle,    energy_optimize)
root.order.add_edge(energy_optimize,  market_strategy)
root.order.add_edge(market_strategy,  performance_rev)