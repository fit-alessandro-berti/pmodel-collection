# Generated from: bb09e301-dfea-433b-961f-2b60b938af07.json
# Description: This process describes the full lifecycle of managing an urban vertical farm designed to optimize space and resources in densely populated areas. It starts with site analysis and environmental setup, followed by seed selection based on market demand and climate conditions. Seeds are then germinated in controlled environments before transplanting into vertical hydroponic systems. Continuous monitoring of nutrient levels, lighting, and humidity ensures optimal growth. Pest detection uses AI-driven sensors with targeted organic treatments. Harvesting is staggered for continuous yield, followed by automated packaging and quality inspection. Waste is processed for composting and energy recovery. The process concludes with market distribution planning and feedback analysis to improve future crop cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions
site_analysis = Transition(label='Site Analysis')
env_setup = Transition(label='Env Setup')
seed_select = Transition(label='Seed Select')
seed_germination = Transition(label='Seed Germination')
transplanting = Transition(label='Transplanting')
nutrient_check = Transition(label='Nutrient Check')
light_adjust = Transition(label='Light Adjust')
humidity_control = Transition(label='Humidity Control')
pest_detect = Transition(label='Pest Detect')
organic_treat = Transition(label='Organic Treat')
stagger_harvest = Transition(label='Stagger Harvest')
auto_packaging = Transition(label='Auto Packaging')
quality_inspect = Transition(label='Quality Inspect')
waste_process = Transition(label='Waste Process')
market_plan = Transition(label='Market Plan')
feedback_review = Transition(label='Feedback Review')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_setup,
    seed_select,
    seed_germination,
    transplanting,
    nutrient_check,
    light_adjust,
    humidity_control,
    pest_detect,
    organic_treat,
    stagger_harvest,
    auto_packaging,
    quality_inspect,
    waste_process,
    market_plan,
    feedback_review
])

# Add ordering edges
root.order.add_edge(site_analysis, env_setup)
root.order.add_edge(env_setup, seed_select)
root.order.add_edge(seed_select, seed_germination)
root.order.add_edge(seed_germination, transplanting)
root.order.add_edge(transplanting, nutrient_check)
root.order.add_edge(nutrient_check, light_adjust)
root.order.add_edge(light_adjust, humidity_control)
root.order.add_edge(humidity_control, pest_detect)
root.order.add_edge(pest_detect, organic_treat)
root.order.add_edge(organic_treat, stagger_harvest)
root.order.add_edge(stagger_harvest, auto_packaging)
root.order.add_edge(auto_packaging, quality_inspect)
root.order.add_edge(quality_inspect, waste_process)
root.order.add_edge(waste_process, market_plan)
root.order.add_edge(market_plan, feedback_review)