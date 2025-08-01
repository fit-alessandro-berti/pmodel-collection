# Generated from: 8ccfaa81-8c42-49eb-a56c-9a61f5eb74c1.json
# Description: This process outlines the steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site assessment, modular system design, environmental control calibration, crop selection based on local demand, nutrient solution formulation, automation integration, pest monitoring, employee training, and continuous yield optimization. The process ensures sustainable resource use, minimal waste, and maximized production efficiency in a confined urban environment, adapting to fluctuating market needs and regulatory requirements while maintaining high product quality and safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site       = Transition(label="Site Survey")
design     = Transition(label="Design Layout")
build      = Transition(label="System Build")
climate    = Transition(label="Climate Setup")
crop       = Transition(label="Crop Select")
nutrient   = Transition(label="Nutrient Mix")
install    = Transition(label="Install Sensors")
automate   = Transition(label="Automate Controls")
train      = Transition(label="Staff Train")
harvest    = Transition(label="Harvest Plan")
pest       = Transition(label="Pest Monitor")
data       = Transition(label="Data Analyze")
market     = Transition(label="Market Align")
waste      = Transition(label="Waste Manage")
yield_opt  = Transition(label="Yield Optimize")

# A silent skip node for loop exit
skip = SilentTransition()

# Build the monitoring & optimization cycle as a partial order
cycle = StrictPartialOrder(nodes=[pest, data, market, waste, yield_opt])
cycle.order.add_edge(pest,    data)
cycle.order.add_edge(data,    market)
cycle.order.add_edge(market,  waste)
cycle.order.add_edge(waste,   yield_opt)

# Wrap the cycle in a LOOP: do the cycle, then either exit or take the skip and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Build the top‐level workflow: initial sequence + harvest planning + loop
nodes = [
    site, design, build, climate, crop, nutrient,
    install, automate, train, harvest, loop
]
root = StrictPartialOrder(nodes=nodes)

# Add the control‐flow edges for the initial setup phase
root.order.add_edge(site,     design)
root.order.add_edge(design,   build)
root.order.add_edge(build,    climate)
root.order.add_edge(climate,  crop)
root.order.add_edge(crop,     nutrient)
root.order.add_edge(nutrient, install)
root.order.add_edge(install,  automate)
root.order.add_edge(automate, train)
root.order.add_edge(train,    harvest)

# After planning the first harvest, enter the monitoring‐optimization loop
root.order.add_edge(harvest, loop)