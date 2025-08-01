# Generated from: 90958393-a27c-40b8-bce6-dd508c8b1f8a.json
# Description: This process outlines the complex setup of an urban vertical farm designed to optimize space and resource efficiency in densely populated city environments. It involves site analysis, modular design, climate control integration, nutrient cycling, automated seeding, growth monitoring, pest management, and harvest logistics. The process requires coordination between architects, agronomists, engineers, and supply chain experts to ensure sustainable crop production year-round while minimizing water use and energy consumption. Advanced IoT sensors and AI-driven analytics are employed to continuously adapt environmental parameters, maximize yield, and reduce waste, creating a resilient food production system within urban infrastructure.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site = Transition(label='Site Analysis')
design = Transition(label='Design Layout')
build = Transition(label='Modular Build')
climate = Transition(label='Climate Setup')
water = Transition(label='Water System')
nutrient = Transition(label='Nutrient Mix')
seed = Transition(label='Seed Automation')
growth = Transition(label='Growth Monitor')
pest = Transition(label='Pest Control')
lighting = Transition(label='Lighting Adjust')
data = Transition(label='Data Collection')
forecast = Transition(label='Yield Forecast')
harvest = Transition(label='Harvest Plan')
supply = Transition(label='Supply Sync')
quality = Transition(label='Quality Check')
waste = Transition(label='Waste Manage')
energy = Transition(label='Energy Audit')

# Define the loop body: pest management, lighting adjustment, data collection, yield forecasting
B_loop = StrictPartialOrder(nodes=[pest, lighting, data, forecast])
B_loop.order.add_edge(pest, lighting)
B_loop.order.add_edge(lighting, data)
B_loop.order.add_edge(data, forecast)

# Loop: after each growth monitoring, optionally repeat the adjustment cycle
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, B_loop])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site, design, build,
    climate, water, nutrient,
    seed, monitor_loop,
    harvest, supply, quality, waste,
    energy
])

# Add ordering constraints
root.order.add_edge(site, design)
root.order.add_edge(design, build)
root.order.add_edge(build, climate)
root.order.add_edge(climate, water)
root.order.add_edge(climate, nutrient)
root.order.add_edge(water, seed)
root.order.add_edge(nutrient, seed)
root.order.add_edge(seed, monitor_loop)
root.order.add_edge(monitor_loop, harvest)
root.order.add_edge(harvest, supply)
root.order.add_edge(harvest, quality)
root.order.add_edge(harvest, waste)
root.order.add_edge(supply, energy)
root.order.add_edge(quality, energy)
root.order.add_edge(waste, energy)