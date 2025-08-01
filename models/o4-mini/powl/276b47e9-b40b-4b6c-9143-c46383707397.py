# Generated from: 276b47e9-b40b-4b6c-9143-c46383707397.json
# Description: This process outlines the complex setup of an urban vertical farm integrating hydroponics and renewable energy systems. It involves site analysis, modular design adaptation, climate control calibration, nutrient formula optimization, automated irrigation programming, sensor deployment, energy storage integration, waste recycling implementation, community engagement, and continuous system monitoring to ensure sustainable crop yields in constrained city environments. The process requires coordination between agronomists, engineers, sustainability experts, and local authorities to balance productivity with environmental impact while leveraging IoT technologies for data-driven decisions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activity nodes
site = Transition(label='Site Survey')
design = Transition(label='Design Layout')
fabricate = Transition(label='Module Fabricate')
climate = Transition(label='Climate Setup')
nutrient = Transition(label='Nutrient Mix')
irrigation = Transition(label='Irrigation Code')
sensor = Transition(label='Sensor Install')
sync = Transition(label='Data Sync')
forecast = Transition(label='Yield Forecast')
energy = Transition(label='Energy Grid')
waste = Transition(label='Waste Process')
train = Transition(label='Staff Train')
meet = Transition(label='Community Meet')

# Loop for continuous system test and adjustment
test = Transition(label='System Test')
monitor = Transition(label='Monitor Adjust')
loop = OperatorPOWL(operator=Operator.LOOP, children=[test, monitor])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site, design, fabricate, climate, nutrient,
    irrigation, sensor, sync, forecast,
    energy, waste, train, meet, loop
])

# Define the control‐flow dependencies
root.order.add_edge(site, design)
root.order.add_edge(design, fabricate)
root.order.add_edge(fabricate, climate)
root.order.add_edge(climate, nutrient)

# Parallel setup of irrigation code and sensor install
root.order.add_edge(nutrient, irrigation)
root.order.add_edge(nutrient, sensor)
root.order.add_edge(irrigation, sync)
root.order.add_edge(sensor, sync)

# Data processing and forecasting
root.order.add_edge(sync, forecast)

# Infrastructure integration (energy and waste)
root.order.add_edge(forecast, energy)
root.order.add_edge(forecast, waste)

# Preparation steps before community/staff activities
root.order.add_edge(energy, train)
root.order.add_edge(waste, train)
root.order.add_edge(energy, meet)
root.order.add_edge(waste, meet)

# After training and community meeting, enter continuous test/monitor loop
root.order.add_edge(train, loop)
root.order.add_edge(meet, loop)