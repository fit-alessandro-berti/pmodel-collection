# Generated from: 9725c04e-86a4-4e10-aa32-4ff30950bbe0.json
# Description: This process outlines the complex steps involved in launching an urban vertical farming operation within a densely populated city environment. It includes site analysis, regulatory compliance, technology integration, crop selection, and community engagement to ensure sustainable food production. The process addresses challenges such as limited space, energy efficiency, and supply chain logistics, while incorporating advanced hydroponic systems, IoT monitoring, and local distribution networks. Collaboration with city planners, environmental experts, and marketing teams is crucial to balance innovation with urban ecosystem demands, leading to a scalable, eco-friendly farming solution that supports local economies and reduces carbon footprints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
permit_filing     = Transition(label='Permit Filing')
tech_setup        = Transition(label='Tech Setup')
crop_research     = Transition(label='Crop Research')
vendor_selection  = Transition(label='Vendor Selection')
system_build      = Transition(label='System Build')
seed_sourcing     = Transition(label='Seed Sourcing')
nutrient_mix      = Transition(label='Nutrient Mix')
iot_config        = Transition(label='IoT Config')
growth_monitor    = Transition(label='Growth Monitor')
pest_control      = Transition(label='Pest Control')
harvest_plan      = Transition(label='Harvest Plan')
packaging         = Transition(label='Packaging')
market_launch     = Transition(label='Market Launch')
community_meet    = Transition(label='Community Meet')
logistics_map     = Transition(label='Logistics Map')
feedback_loop     = Transition(label='Feedback Loop')

# Loop for continuous monitoring & pest control
loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control]
)

# Loop for harvest planning & feedback iteration
loop_harvest = OperatorPOWL(
    operator=Operator.LOOP,
    children=[harvest_plan, feedback_loop]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_filing, tech_setup, crop_research,
    vendor_selection, system_build, seed_sourcing, nutrient_mix,
    iot_config, loop_monitor, loop_harvest,
    packaging, market_launch, community_meet, logistics_map
])

# Define control-flow edges
root.order.add_edge(site_survey,    permit_filing)
root.order.add_edge(permit_filing,  tech_setup)
root.order.add_edge(permit_filing,  crop_research)
root.order.add_edge(tech_setup,     vendor_selection)
root.order.add_edge(vendor_selection, system_build)
root.order.add_edge(crop_research,  seed_sourcing)
root.order.add_edge(seed_sourcing,  nutrient_mix)
root.order.add_edge(system_build,   iot_config)
root.order.add_edge(nutrient_mix,   iot_config)
root.order.add_edge(iot_config,     loop_monitor)
root.order.add_edge(loop_monitor,   loop_harvest)
root.order.add_edge(loop_harvest,   packaging)
root.order.add_edge(packaging,      market_launch)
root.order.add_edge(market_launch,  community_meet)
root.order.add_edge(community_meet, logistics_map)