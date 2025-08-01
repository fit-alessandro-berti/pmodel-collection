# Generated from: 92e6d216-ab86-4e8b-9787-4e6d0385f0e5.json
# Description: This process outlines the comprehensive workflow for managing an urban vertical farm, integrating advanced hydroponics and AI-driven environmental controls. Starting from seed selection and germination, it includes nutrient solution preparation, automated lighting adjustments, pest monitoring using drones, and real-time growth analytics. Harvesting is synchronized with market demand forecasts, followed by quality inspection, packaging, and distribution through smart logistics. Waste recycling and system maintenance are continuous to ensure sustainability and operational efficiency in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed         = Transition(label='Seed Selection')
germ         = Transition(label='Germination Start')
nutrient     = Transition(label='Nutrient Mix')
light        = Transition(label='Lighting Adjust')
climate      = Transition(label='Climate Control')
water        = Transition(label='Water Cycle')
pest         = Transition(label='Pest Drone')
growth       = Transition(label='Growth Scan')
analyze      = Transition(label='Data Analyze')
forecast     = Transition(label='Market Forecast')
harvest      = Transition(label='Harvest Sync')
quality      = Transition(label='Quality Check')
pack         = Transition(label='Pack Produce')
dispatch     = Transition(label='Smart Dispatch')
waste        = Transition(label='Waste Recycle')
clean        = Transition(label='System Clean')

# Silent transition for loop exits
tau = SilentTransition()

# Loop for continuous environment control (lighting, climate, water)
env_controls = StrictPartialOrder(nodes=[light, climate, water])
env_loop     = OperatorPOWL(operator=Operator.LOOP, children=[env_controls, tau])

# Loop for periodic pest monitoring
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest, tau])

# Loop for continuous waste recycling
waste_loop   = OperatorPOWL(operator=Operator.LOOP, children=[waste, tau])

# Loop for ongoing system cleaning
maint_loop   = OperatorPOWL(operator=Operator.LOOP, children=[clean, tau])

# Root partial order combining the main sequence with concurrent loops
root = StrictPartialOrder(nodes=[
    seed, germ, nutrient,
    growth, analyze, forecast,
    harvest, quality, pack, dispatch,
    env_loop, monitor_loop, waste_loop, maint_loop
])

# Main sequence of the farming workflow
root.order.add_edge(seed, germ)
root.order.add_edge(germ, nutrient)
root.order.add_edge(nutrient, growth)
root.order.add_edge(growth, analyze)
root.order.add_edge(analyze, forecast)
root.order.add_edge(forecast, harvest)
root.order.add_edge(harvest, quality)
root.order.add_edge(quality, pack)
root.order.add_edge(pack, dispatch)

# Start loops after the nutrient mix is prepared
root.order.add_edge(nutrient, env_loop)
root.order.add_edge(nutrient, monitor_loop)
root.order.add_edge(nutrient, waste_loop)
root.order.add_edge(nutrient, maint_loop)