# Generated from: 95f2b779-22be-45e5-a785-43deb2bc45a1.json
# Description: This process outlines the end-to-end setup of an urban vertical farming system within a repurposed industrial building. It begins with site analysis and structural assessment to ensure the building can support multi-layered grow racks. Following this, environmental controls such as lighting, humidity, and temperature systems are installed and calibrated. The integration of hydroponic or aeroponic systems is next, requiring precise plumbing and nutrient delivery setups. Crop selection and seeding protocols are established based on market demand and growth cycles. Automated monitoring and AI-driven adjustments optimize plant health. Periodic maintenance routines and yield tracking ensure sustainability and profitability. The process concludes with packaging and distribution planning tailored for urban consumers, incorporating waste recycling strategies to minimize environmental footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site = Transition(label='Site Survey')
structure = Transition(label='Structure Check')
design = Transition(label='System Design')
lighting = Transition(label='Lighting Setup')
climate = Transition(label='Climate Control')
water = Transition(label='Water Install')
nutrient = Transition(label='Nutrient Mix')
rack = Transition(label='Rack Assembly')
seeding = Transition(label='Seed Planting')
sensor = Transition(label='Sensor Install')
ai = Transition(label='AI Calibration')
monitor = Transition(label='Growth Monitor')
maintenance = Transition(label='Maintenance')
harvest = Transition(label='Harvest Prep')
pack = Transition(label='Packaging')
waste = Transition(label='Waste Manage')
distribution = Transition(label='Distribution')

# Loop for periodic monitoring and maintenance
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, maintenance])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site, structure, design,
    lighting, climate,
    water, nutrient,
    rack, seeding,
    sensor, ai,
    loop,
    harvest, pack, waste, distribution
])

# Define ordering constraints
root.order.add_edge(site, design)
root.order.add_edge(structure, design)

root.order.add_edge(design, lighting)
root.order.add_edge(design, climate)

root.order.add_edge(lighting, water)
root.order.add_edge(climate, water)
root.order.add_edge(lighting, nutrient)
root.order.add_edge(climate, nutrient)

root.order.add_edge(water, rack)
root.order.add_edge(nutrient, rack)

root.order.add_edge(rack, seeding)
root.order.add_edge(seeding, sensor)
root.order.add_edge(sensor, ai)

root.order.add_edge(ai, loop)
root.order.add_edge(loop, harvest)

root.order.add_edge(harvest, pack)
root.order.add_edge(harvest, waste)

root.order.add_edge(pack, distribution)
root.order.add_edge(waste, distribution)