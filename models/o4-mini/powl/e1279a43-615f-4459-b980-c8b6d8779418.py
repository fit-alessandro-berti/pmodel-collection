# Generated from: e1279a43-615f-4459-b980-c8b6d8779418.json
# Description: This process describes the comprehensive cycle of an urban vertical farming operation, integrating technology, resource management, and distribution logistics. It begins with site analysis and infrastructure setup, followed by seed selection and nutrient calibration. Real-time monitoring and climate adjustment optimize plant growth, while automated harvesting and quality inspection ensure produce standards. Post-harvest, products undergo packaging and cold storage before distribution via eco-friendly channels. Waste recycling and system maintenance close the loop, promoting sustainability in an atypical yet realistic agricultural business model embedded within urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sa = Transition(label='Site Analysis')
infra = Transition(label='Infrastructure Setup')
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
planting = Transition(label='Planting Cycle')
growth_mon = Transition(label='Growth Monitor')
climate = Transition(label='Climate Adjust')
pest = Transition(label='Pest Control')
harvest = Transition(label='Harvesting Mode')
quality = Transition(label='Quality Check')
packaging = Transition(label='Packaging Phase')
cold = Transition(label='Cold Storage')
dispatch = Transition(label='Order Dispatch')
waste = Transition(label='Waste Recycling')
maintain = Transition(label='System Maintain')

# Silent skip for loop redo
skip = SilentTransition()

# Body of the growth-monitoring loop: Growth Monitor -> Climate Adjust -> Pest Control
body = StrictPartialOrder(nodes=[growth_mon, climate, pest])
body.order.add_edge(growth_mon, climate)
body.order.add_edge(climate, pest)

# Loop: monitor body, then either exit or redo after a silent skip
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    sa, infra, seed, nutrient, planting,
    loop_monitor,
    harvest, quality, packaging, cold, dispatch,
    waste, maintain
])

# Define the control-flow edges
root.order.add_edge(sa, infra)
root.order.add_edge(infra, seed)
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, planting)
root.order.add_edge(planting, loop_monitor)

root.order.add_edge(loop_monitor, harvest)
root.order.add_edge(harvest, quality)
root.order.add_edge(quality, packaging)
root.order.add_edge(packaging, cold)
root.order.add_edge(cold, dispatch)

# After dispatch, waste recycling and system maintenance can proceed in parallel
root.order.add_edge(dispatch, waste)
root.order.add_edge(dispatch, maintain)