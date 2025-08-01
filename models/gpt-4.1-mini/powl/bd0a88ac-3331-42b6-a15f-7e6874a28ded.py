# Generated from: bd0a88ac-3331-42b6-a15f-7e6874a28ded.json
# Description: This process outlines the complex cycle of urban vertical farming in a multi-level indoor facility designed to maximize crop yield while minimizing resource use. It involves seed selection based on climate data, automated nutrient mixing tailored to specific plants, continuous environmental monitoring, and adaptive lighting schedules. The process also integrates pest detection using AI vision systems, localized pollination methods, and waste recycling via composting units. Harvesting is staggered to optimize freshness, followed by automated packaging and real-time logistics coordination to ensure rapid delivery. Finally, data from each cycle feeds into predictive models to enhance future crop cycles and resource allocation, ensuring sustainability and profitability in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Seed_Select = Transition(label='Seed Select')
Climate_Analyze = Transition(label='Climate Analyze')
Nutrient_Mix = Transition(label='Nutrient Mix')
Env_Monitor = Transition(label='Env Monitor')
Light_Adjust = Transition(label='Light Adjust')
Pest_Detect = Transition(label='Pest Detect')
Pollinate_Local = Transition(label='Pollinate Local')
Growth_Track = Transition(label='Growth Track')
Harvest_Stagger = Transition(label='Harvest Stagger')
Waste_Compost = Transition(label='Waste Compost')
Package_Auto = Transition(label='Package Auto')
Logistics_Plan = Transition(label='Logistics Plan')
Data_Collect = Transition(label='Data Collect')
Model_Update = Transition(label='Model Update')
Resource_Allocate = Transition(label='Resource Allocate')

# Construct partial orders for groups of concurrent or partially ordered activities

# Seed selection and climate analysis
seed_climate = StrictPartialOrder(nodes=[Seed_Select, Climate_Analyze])
seed_climate.order.add_edge(Seed_Select, Climate_Analyze)

# Nutrient mix depends on seed/climate
nutrient = Nutrient_Mix

# Environmental monitoring and light adjustment run concurrently but both start after nutrient mix
env_light = StrictPartialOrder(nodes=[Env_Monitor, Light_Adjust])
# no order edges between Env_Monitor and Light_Adjust => concurrent

# Pest detect and pollinate local run concurrently after env_monitor and light_adjust
pest_pollinate = StrictPartialOrder(nodes=[Pest_Detect, Pollinate_Local])

# Growth track waits for pest detection and pollination
growth = Growth_Track

# Harvest stagger depends on growth track
harvest = Harvest_Stagger

# Waste compost starts after harvest
waste = Waste_Compost

# Package auto and logistics plan run concurrently after harvest
package_logistics = StrictPartialOrder(nodes=[Package_Auto, Logistics_Plan])

# Data collect depends on package and logistics done
data_collect = Data_Collect

# Model update and resource allocate run concurrently after data collect
model_resource = StrictPartialOrder(nodes=[Model_Update, Resource_Allocate])

# Build partial order:

root = StrictPartialOrder(
    nodes=[
        seed_climate,
        nutrient,
        env_light,
        pest_pollinate,
        growth,
        harvest,
        waste,
        package_logistics,
        data_collect,
        model_resource
    ]
)

# Define order edges

# seed_climate --> nutrient
root.order.add_edge(seed_climate, nutrient)

# nutrient --> env_light
root.order.add_edge(nutrient, env_light)

# env_light --> pest_pollinate
root.order.add_edge(env_light, pest_pollinate)

# pest_pollinate --> growth
root.order.add_edge(pest_pollinate, growth)

# growth --> harvest
root.order.add_edge(growth, harvest)

# harvest --> waste
root.order.add_edge(harvest, waste)

# harvest --> package_logistics (package + logistics concurrent after harvest)
root.order.add_edge(harvest, package_logistics)

# package_logistics --> data_collect
root.order.add_edge(package_logistics, data_collect)

# data_collect --> model_resource
root.order.add_edge(data_collect, model_resource)