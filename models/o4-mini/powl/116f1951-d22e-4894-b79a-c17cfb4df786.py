# Generated from: 116f1951-d22e-4894-b79a-c17cfb4df786.json
# Description: This process outlines the end-to-end operations of an urban vertical farming facility that integrates automated hydroponics, AI-driven environmental control, and community-supported agriculture. Starting from seed selection, the cycle includes nutrient mixing, lighting calibration, pest monitoring via drones, and adaptive harvesting schedules. Post-harvest, produce undergoes smart packaging and local distribution using electric vehicles. The system continuously collects data on growth patterns and energy consumption to optimize future yields and reduce environmental impact. Additionally, the process incorporates community engagement through workshops and feedback loops, ensuring sustainable urban agriculture development.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
lighting = Transition(label='Lighting Setup')
drone = Transition(label='Drone Scan')
pest = Transition(label='Pest Control')
growth = Transition(label='Growth Monitor')
water = Transition(label='Water Recycle')
climate = Transition(label='Climate Adjust')
harvest = Transition(label='Harvest Schedule')
packing = Transition(label='Smart Packing')
quality = Transition(label='Quality Check')
dispatch = Transition(label='Local Dispatch')
analysis = Transition(label='Data Analysis')
audit = Transition(label='Energy Audit')
meet = Transition(label='Community Meet')
feedback = Transition(label='Feedback Loop')

# Silent transition for optional pest control
skip = SilentTransition()

# Choice: either perform pest control or skip if no pests detected
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest, skip])

# Loop for continuous data analysis -> energy audit cycle
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[analysis, audit])

# Loop for community engagement: workshops and feedback sessions
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[meet, feedback])

# Build the partial-order workflow
root = StrictPartialOrder(nodes=[
    seed, nutrient, lighting, drone, pest_choice, growth,
    water, climate, harvest, packing, quality, dispatch,
    data_loop, feedback_loop
])

# Define the control-flow/order relations
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, lighting)
root.order.add_edge(lighting, drone)
root.order.add_edge(drone, pest_choice)
root.order.add_edge(pest_choice, growth)
root.order.add_edge(growth, water)
root.order.add_edge(growth, climate)
root.order.add_edge(water, harvest)
root.order.add_edge(climate, harvest)
root.order.add_edge(harvest, packing)
root.order.add_edge(packing, quality)
root.order.add_edge(quality, dispatch)

# After dispatch, start concurrent loops for data cycle and community engagement
root.order.add_edge(dispatch, data_loop)
root.order.add_edge(dispatch, feedback_loop)