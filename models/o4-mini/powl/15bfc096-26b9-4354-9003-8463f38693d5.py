# Generated from: 15bfc096-26b9-4354-9003-8463f38693d5.json
# Description: This process details the establishment of an urban vertical farming system within a repurposed industrial warehouse. It involves site assessment, modular rack installation, climate control calibration, nutrient solution preparation, seed selection and planting, automated monitoring setup, pest management protocols, and harvest scheduling. The process requires integration of IoT sensors for real-time data analysis, energy optimization strategies, waste recycling plans, and distribution logistics coordination to ensure sustainable local food production. Each step demands cross-functional collaboration between agronomists, engineers, and supply chain managers, emphasizing innovation and environmental impact mitigation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
site = Transition(label='Site Survey')
rack = Transition(label='Rack Install')
climate = Transition(label='Climate Setup')
nutrient = Transition(label='Nutrient Mix')
seed_sel = Transition(label='Seed Selection')
plant = Transition(label='Planting Seeds')
sensor = Transition(label='Sensor Deploy')
data_init = Transition(label='Data Monitor')    # initial data check
pest = Transition(label='Pest Control')
growth = Transition(label='Growth Check')
data_loop = Transition(label='Data Monitor')    # looped data check
energy = Transition(label='Energy Audit')
waste = Transition(label='Waste Cycle')
harvest = Transition(label='Harvest Plan')
logistics = Transition(label='Logistics Prep')
quality = Transition(label='Quality Test')
market = Transition(label='Market Launch')

# Define the monitoring loop: Pest & Growth concurrently, then data check
inner_po = StrictPartialOrder(nodes=[pest, growth, data_loop])
inner_po.order.add_edge(pest, data_loop)
inner_po.order.add_edge(growth, data_loop)

monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_init, inner_po])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site, rack, climate,
    nutrient, seed_sel, plant,
    sensor, monitor_loop,
    energy, waste,
    harvest, logistics, quality, market
])

# Sequence: Site Survey -> Rack Install -> Climate Setup
root.order.add_edge(site, rack)
root.order.add_edge(rack, climate)

# After climate setup, Nutrient Mix and Seed Selection in parallel
root.order.add_edge(climate, nutrient)
root.order.add_edge(climate, seed_sel)

# Both feed into Planting Seeds
root.order.add_edge(nutrient, plant)
root.order.add_edge(seed_sel, plant)

# Then deploy sensors and enter the monitoring loop
root.order.add_edge(plant, sensor)
root.order.add_edge(sensor, monitor_loop)

# After exiting the loop, run Energy Audit and Waste Cycle in parallel
root.order.add_edge(monitor_loop, energy)
root.order.add_edge(monitor_loop, waste)

# Both lead to Harvest Plan
root.order.add_edge(energy, harvest)
root.order.add_edge(waste, harvest)

# Harvest Plan enables Logistics Prep and Quality Test (in parallel)
root.order.add_edge(harvest, logistics)
root.order.add_edge(harvest, quality)

# Both must complete before Market Launch
root.order.add_edge(logistics, market)
root.order.add_edge(quality, market)