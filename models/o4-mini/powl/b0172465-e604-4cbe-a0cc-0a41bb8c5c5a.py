# Generated from: b0172465-e604-4cbe-a0cc-0a41bb8c5c5a.json
# Description: This process outlines the comprehensive steps involved in establishing a sustainable urban rooftop farm. It includes site evaluation, structural analysis, soil testing, microclimate assessment, vendor sourcing for modular planting systems, installation of automated irrigation, integration of renewable energy sources, crop selection based on local demand, pest management planning, community engagement for shared maintenance, waste composting setup, yield forecasting, market channel development, and continuous monitoring to ensure productivity and environmental compliance. The process aims to transform underutilized urban rooftop spaces into productive agricultural hubs while addressing logistical, environmental, and social challenges uniquely inherent to urban farming.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site = Transition(label='Site Survey')
load = Transition(label='Load Test')
soil = Transition(label='Soil Sample')
climate = Transition(label='Climate Study')
vendor = Transition(label='Vendor Sourcing')
install = Transition(label='System Install')
irrigation = Transition(label='Irrigation Setup')
energy = Transition(label='Energy Integrate')
crop = Transition(label='Crop Select')
community = Transition(label='Community Meet')
waste = Transition(label='Waste Setup')
yield_f = Transition(label='Yield Forecast')
market = Transition(label='Market Plan')
monitor = Transition(label='Monitor Growth')
pest = Transition(label='Pest Control')

# Loop for continuous monitoring and pest management
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, pest])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site, load, soil, climate,
    vendor, install,
    irrigation, energy,
    crop,
    community, waste,
    yield_f, market,
    loop
])

# Site evaluation precedes detailed analyses
root.order.add_edge(site, load)
root.order.add_edge(site, soil)
root.order.add_edge(site, climate)

# Analyses must finish before vendor sourcing
root.order.add_edge(load, vendor)
root.order.add_edge(soil, vendor)
root.order.add_edge(climate, vendor)

# Sourcing → installation → parallel subsystem setups
root.order.add_edge(vendor, install)
root.order.add_edge(install, irrigation)
root.order.add_edge(install, energy)

# Subsystems ready → crop selection
root.order.add_edge(irrigation, crop)
root.order.add_edge(energy, crop)

# Crop selection → community, waste, market & yield planning (all in parallel)
root.order.add_edge(crop, community)
root.order.add_edge(crop, waste)
root.order.add_edge(crop, market)
root.order.add_edge(crop, yield_f)

# Once setup and planning are done, enter the monitoring loop
root.order.add_edge(community, loop)
root.order.add_edge(waste, loop)
root.order.add_edge(market, loop)
root.order.add_edge(yield_f, loop)