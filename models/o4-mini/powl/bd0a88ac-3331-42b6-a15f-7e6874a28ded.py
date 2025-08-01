# Generated from: bd0a88ac-3331-42b6-a15f-7e6874a28ded.json
# Description: This process outlines the complex cycle of urban vertical farming in a multi-level indoor facility designed to maximize crop yield while minimizing resource use. It involves seed selection based on climate data, automated nutrient mixing tailored to specific plants, continuous environmental monitoring, and adaptive lighting schedules. The process also integrates pest detection using AI vision systems, localized pollination methods, and waste recycling via composting units. Harvesting is staggered to optimize freshness, followed by automated packaging and real-time logistics coordination to ensure rapid delivery. Finally, data from each cycle feeds into predictive models to enhance future crop cycles and resource allocation, ensuring sustainability and profitability in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# define the basic activities
seed_select      = Transition(label='Seed Select')
climate_analyze  = Transition(label='Climate Analyze')
nutrient_mix     = Transition(label='Nutrient Mix')
env_monitor      = Transition(label='Env Monitor')
light_adjust     = Transition(label='Light Adjust')
pest_detect      = Transition(label='Pest Detect')
growth_track     = Transition(label='Growth Track')
pollinate_local  = Transition(label='Pollinate Local')
harvest_stagger  = Transition(label='Harvest Stagger')
waste_compost    = Transition(label='Waste Compost')
package_auto     = Transition(label='Package Auto')
logistics_plan   = Transition(label='Logistics Plan')
data_collect     = Transition(label='Data Collect')
model_update     = Transition(label='Model Update')
resource_allocate= Transition(label='Resource Allocate')

# a silent transition for loop exit
skip = SilentTransition()

# build one cycle of the vertical farming process as a partial order
body = StrictPartialOrder(nodes=[
    seed_select, climate_analyze, nutrient_mix,
    env_monitor, light_adjust, pest_detect,
    growth_track, pollinate_local,
    harvest_stagger, waste_compost, package_auto,
    logistics_plan, data_collect, model_update,
    resource_allocate
])

# ordering: seed selection and analysis
body.order.add_edge(seed_select,      climate_analyze)
body.order.add_edge(climate_analyze,  nutrient_mix)

# nutrient mixing precedes monitoring, lighting, pest detection, and pollination
body.order.add_edge(nutrient_mix, env_monitor)
body.order.add_edge(nutrient_mix, light_adjust)
body.order.add_edge(nutrient_mix, pest_detect)
body.order.add_edge(nutrient_mix, pollinate_local)

# monitoring, lighting, and pest detection must complete before growth tracking
body.order.add_edge(env_monitor,  growth_track)
body.order.add_edge(light_adjust, growth_track)
body.order.add_edge(pest_detect,  growth_track)

# pest detection also gates local pollination
body.order.add_edge(pest_detect, pollinate_local)

# after growth and pollination comes harvesting
body.order.add_edge(growth_track,    harvest_stagger)
body.order.add_edge(pollinate_local, harvest_stagger)

# after harvest comes waste composting and packaging
body.order.add_edge(harvest_stagger, waste_compost)
body.order.add_edge(harvest_stagger, package_auto)

# packaging and composting both feed logistics planning
body.order.add_edge(waste_compost,  logistics_plan)
body.order.add_edge(package_auto,   logistics_plan)

# logistics, then data collection and model update, then resource allocation
body.order.add_edge(logistics_plan,  data_collect)
body.order.add_edge(data_collect,   model_update)
body.order.add_edge(model_update,   resource_allocate)

# wrap the cycle in a LOOP operator: execute the body, then optionally repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])