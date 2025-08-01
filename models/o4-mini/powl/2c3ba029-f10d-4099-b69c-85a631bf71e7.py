# Generated from: 2c3ba029-f10d-4099-b69c-85a631bf71e7.json
# Description: This process outlines the comprehensive setup of an urban vertical farm, integrating advanced hydroponic systems with AI-driven climate control. It starts with site analysis and structural retrofitting, followed by nutrient solution formulation and seed selection tailored for vertical growth. Continuous monitoring includes pest detection via machine vision and predictive yield modeling. The process concludes with automated harvesting and supply chain integration to local markets, ensuring sustainability and minimal environmental impact throughout the farm's lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as POWL transitions
site_analysis    = Transition(label="Site Analysis")
structural_retro = Transition(label="Structural Retrofit")
hydroponic_setup = Transition(label="Hydroponic Setup")
seed_selection   = Transition(label="Seed Selection")
nutrient_mix     = Transition(label="Nutrient Mix")
climate_tuning   = Transition(label="Climate Tuning")
lighting_install = Transition(label="Lighting Install")
ai_calibration   = Transition(label="AI Calibration")
pest_detection   = Transition(label="Pest Detection")
growth_monitor   = Transition(label="Growth Monitoring")
water_recycle    = Transition(label="Water Recycling")
yield_predict    = Transition(label="Yield Prediction")
auto_harvest     = Transition(label="Automated Harvest")
packaging_prep   = Transition(label="Packaging Prep")
market_integration = Transition(label="Market Integration")

# 1. Initial setup: site → structure → hydroponics → seed → nutrients → climate → lighting → AI
setup = StrictPartialOrder(nodes=[
    site_analysis, structural_retro, hydroponic_setup,
    seed_selection, nutrient_mix, climate_tuning,
    lighting_install, ai_calibration
])
setup.order.add_edge(site_analysis,    structural_retro)
setup.order.add_edge(structural_retro, hydroponic_setup)
setup.order.add_edge(hydroponic_setup, seed_selection)
setup.order.add_edge(seed_selection,   nutrient_mix)
setup.order.add_edge(nutrient_mix,     climate_tuning)
setup.order.add_edge(climate_tuning,   lighting_install)
setup.order.add_edge(lighting_install, ai_calibration)

# 2. Monitoring loop: pest → {growth, water} → yield, repeat until exit
monitor_cycle = StrictPartialOrder(nodes=[
    pest_detection, growth_monitor,
    water_recycle, yield_predict
])
monitor_cycle.order.add_edge(pest_detection, growth_monitor)
monitor_cycle.order.add_edge(pest_detection, water_recycle)
monitor_cycle.order.add_edge(growth_monitor, yield_predict)
monitor_cycle.order.add_edge(water_recycle,  yield_predict)

monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_cycle, monitor_cycle]
)

# 3. Harvest and supply chain: harvest → packaging → market
harvest_flow = StrictPartialOrder(nodes=[
    auto_harvest, packaging_prep, market_integration
])
harvest_flow.order.add_edge(auto_harvest,     packaging_prep)
harvest_flow.order.add_edge(packaging_prep,   market_integration)

# 4. Combine everything in a top‐level partial order
root = StrictPartialOrder(nodes=[setup, monitor_loop, harvest_flow])
root.order.add_edge(setup,        monitor_loop)
root.order.add_edge(monitor_loop, harvest_flow)