# Generated from: 6c22511b-2346-4480-b476-a93bf369ecb9.json
# Description: This process outlines the establishment of a vertical farming system in an urban environment, integrating sustainable agriculture with smart technology. It involves site evaluation, modular farm design, installation of hydroponic or aeroponic systems, climate control setup, integration of IoT sensors for real-time monitoring, nutrient solution management, lighting calibration, crop selection optimized for vertical growth, staff training on system maintenance, pest control through biological agents, continuous data analysis for yield optimization, and establishing distribution channels for urban markets. The process emphasizes resource efficiency, minimal environmental impact, and scalability to adapt to various building types and urban constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site       = Transition(label='Site Survey')
design     = Transition(label='Design Layout')
install    = Transition(label='System Install')
climate    = Transition(label='Climate Setup')
sensor     = Transition(label='Sensor Deploy')
nutrient   = Transition(label='Nutrient Mix')
lighting   = Transition(label='Lighting Tune')
crop       = Transition(label='Crop Select')
staff      = Transition(label='Staff Train')
supply     = Transition(label='Supply Chain')
pest       = Transition(label='Pest Control')
waste      = Transition(label='Waste Manage')
comp       = Transition(label='Compliance Check')
dm         = Transition(label='Data Monitor')
ya         = Transition(label='Yield Analyze')

# "A" part of loop: monitoring → analyzing
sync = StrictPartialOrder(nodes=[dm, ya])
sync.order.add_edge(dm, ya)

# "B" part of loop: pest control → waste manage → compliance check
intervene = StrictPartialOrder(nodes=[pest, waste, comp])
intervene.order.add_edge(pest, waste)
intervene.order.add_edge(waste, comp)

# The LOOP operator: do (sync), then either exit or do (intervene) and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[sync, intervene])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site, design, install, climate, sensor,
    nutrient, lighting, crop, staff,
    supply, loop
])
root.order.add_edge(site, design)
root.order.add_edge(design, install)
root.order.add_edge(install, climate)
root.order.add_edge(climate, sensor)
root.order.add_edge(sensor, nutrient)
root.order.add_edge(nutrient, lighting)
root.order.add_edge(lighting, crop)
root.order.add_edge(crop, staff)
root.order.add_edge(staff, supply)
root.order.add_edge(supply, loop)