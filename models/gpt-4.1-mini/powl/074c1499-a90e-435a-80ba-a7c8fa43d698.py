# Generated from: 074c1499-a90e-435a-80ba-a7c8fa43d698.json
# Description: This process outlines the establishment of a vertical farming operation within an urban environment, integrating advanced hydroponic systems, AI-driven climate control, and local supply chain logistics. It begins with site analysis and ends with ongoing yield optimization, incorporating activities such as nutrient cycling, pest monitoring without pesticides, and community engagement for sustainable food distribution. The process involves cross-disciplinary collaboration among agronomists, engineers, data scientists, and local authorities to ensure compliance and efficiency. It emphasizes resource recycling, energy management, and adaptive crop planning based on real-time data and market demand forecasts, creating a highly responsive urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permits_obtain = Transition(label='Permits Obtain')
system_install = Transition(label='System Install')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_setup = Transition(label='Planting Setup')
climate_control = Transition(label='Climate Control')
pest_monitor = Transition(label='Pest Monitor')
data_integration = Transition(label='Data Integration')
growth_tracking = Transition(label='Growth Tracking')
harvest_plan = Transition(label='Harvest Plan')
yield_analysis = Transition(label='Yield Analysis')
waste_recycle = Transition(label='Waste Recycle')
market_liaison = Transition(label='Market Liaison')
community_engage = Transition(label='Community Engage')

# Define partial orders for the main workflow phases:

# Initial phase: site survey -> design layout -> permits obtain -> system install
init_phase = StrictPartialOrder(nodes=[site_survey, design_layout, permits_obtain, system_install])
init_phase.order.add_edge(site_survey, design_layout)
init_phase.order.add_edge(design_layout, permits_obtain)
init_phase.order.add_edge(permits_obtain, system_install)

# Planting preparation: seed selection followed by nutrient mix and planting setup (nutrient_mix and planting_setup concurrent)
plant_prep = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, planting_setup])
plant_prep.order.add_edge(seed_selection, nutrient_mix)
plant_prep.order.add_edge(seed_selection, planting_setup)
# nutrient_mix and planting_setup are concurrent (no order between them)

# Growth phase: climate control and pest monitor run concurrently after planting_setup
growth_phase = StrictPartialOrder(nodes=[climate_control, pest_monitor])
# No order edges -> concurrent

# Data integration and growth tracking run in sequence after growth phase
data_growth = StrictPartialOrder(nodes=[data_integration, growth_tracking])
data_growth.order.add_edge(data_integration, growth_tracking)

# Harvest planning and yield analysis after growth tracking
harvest_phase = StrictPartialOrder(nodes=[harvest_plan, yield_analysis])
harvest_phase.order.add_edge(harvest_plan, yield_analysis)

# Recycling waste and market liaison run concurrently with community engagement (community engagement depends on market liaison)
post_harvest = StrictPartialOrder(nodes=[waste_recycle, market_liaison, community_engage])
post_harvest.order.add_edge(market_liaison, community_engage)
# waste_recycle concurrent with market_liaison and community_engage

# Build the overall flow:
# init_phase -> plant_prep -> planting_setup -> (growth_phase: climate_control, pest_monitor) concurrent
# Then -> data_integration -> growth_tracking -> harvest_plan -> yield_analysis
# Then post-harvest activities

# Combine growth_phase with data_growth in sequence
growth_and_data = StrictPartialOrder(nodes=[growth_phase, data_growth])
growth_and_data.order.add_edge(growth_phase, data_growth)

# Combine harvest_phase with post_harvest in sequence
harvest_and_post = StrictPartialOrder(nodes=[harvest_phase, post_harvest])
harvest_and_post.order.add_edge(harvest_phase, post_harvest)

# Assemble the whole process in order:
root = StrictPartialOrder(
    nodes=[
        init_phase,
        plant_prep,
        growth_phase,
        data_growth,
        harvest_phase,
        post_harvest
    ]
)
root.order.add_edge(init_phase, plant_prep)
root.order.add_edge(plant_prep, growth_phase)
root.order.add_edge(growth_phase, data_growth)
root.order.add_edge(data_growth, harvest_phase)
root.order.add_edge(harvest_phase, post_harvest)