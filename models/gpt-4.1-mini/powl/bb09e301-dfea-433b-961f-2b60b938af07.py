# Generated from: bb09e301-dfea-433b-961f-2b60b938af07.json
# Description: This process describes the full lifecycle of managing an urban vertical farm designed to optimize space and resources in densely populated areas. It starts with site analysis and environmental setup, followed by seed selection based on market demand and climate conditions. Seeds are then germinated in controlled environments before transplanting into vertical hydroponic systems. Continuous monitoring of nutrient levels, lighting, and humidity ensures optimal growth. Pest detection uses AI-driven sensors with targeted organic treatments. Harvesting is staggered for continuous yield, followed by automated packaging and quality inspection. Waste is processed for composting and energy recovery. The process concludes with market distribution planning and feedback analysis to improve future crop cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Monitoring as partial order of nutrient_check, light_adjust, humidity_control (concurrent)
monitoring = StrictPartialOrder(nodes=[nutrient_check, light_adjust, humidity_control])

# Pest management loop: Pest Detect then Organic Treat, possibly repeated
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_detect, organic_treat])

# Harvest -> Packaging -> Quality Inspect partial order
harvest_pack_quality = StrictPartialOrder(nodes=[stagger_harvest, auto_packaging, quality_inspect])
harvest_pack_quality.order.add_edge(stagger_harvest, auto_packaging)
harvest_pack_quality.order.add_edge(auto_packaging, quality_inspect)

# Waste processing after Quality Inspect
quality_to_waste = StrictPartialOrder(nodes=[quality_inspect, waste_process])
quality_to_waste.order.add_edge(quality_inspect, waste_process)

# Market plan then feedback review partial order
market_feedback = StrictPartialOrder(nodes=[market_plan, feedback_review])
market_feedback.order.add_edge(market_plan, feedback_review)

# Combine last stages: waste_process and market_feedback are concurrent
end_concurrent = StrictPartialOrder(nodes=[waste_process, market_plan, feedback_review])
end_concurrent.order.add_edge(market_plan, feedback_review)

# Build a PO for main sequence up to monitoring
main_sequence = StrictPartialOrder(nodes=[
    site_analysis,
    env_setup,
    seed_select,
    seed_germination,
    transplanting,
    monitoring,
    pest_loop,
    harvest_pack_quality,
    end_concurrent
])

# Define order edges for main sequence
main_sequence.order.add_edge(site_analysis, env_setup)
main_sequence.order.add_edge(env_setup, seed_select)
main_sequence.order.add_edge(seed_select, seed_germination)
main_sequence.order.add_edge(seed_germination, transplanting)
main_sequence.order.add_edge(transplanting, monitoring)
main_sequence.order.add_edge(monitoring, pest_loop)
main_sequence.order.add_edge(pest_loop, harvest_pack_quality)
main_sequence.order.add_edge(harvest_pack_quality, end_concurrent)

root = main_sequence