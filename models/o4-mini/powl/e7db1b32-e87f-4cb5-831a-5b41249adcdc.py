# Generated from: e7db1b32-e87f-4cb5-831a-5b41249adcdc.json
# Description: This process outlines the complex operational cycle of an urban vertical farming facility that integrates IoT sensors, automated nutrient delivery, and AI-driven crop monitoring to optimize yield and resource efficiency. It begins with seed selection based on AI growth predictions, followed by automated planting in vertical trays. Environmental conditions like humidity, temperature, and light are continuously monitored and adjusted via smart controls. Nutrient solutions are precisely dosed through hydroponic systems, while robotic arms conduct pruning and harvesting to maintain plant health. Data collected is analyzed in real-time for predictive maintenance and yield forecasting. The process also involves waste recycling through composting organic residues and repurposing water. Finally, harvested produce is packaged using biodegradable materials and dispatched through an integrated logistics platform focused on reducing carbon footprint. This atypical process merges agriculture, technology, and sustainability in an urban setting to revolutionize food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
t1  = Transition(label="Seed Selection")
t2  = Transition(label="AI Prediction")
t3  = Transition(label="Automated Planting")
t4  = Transition(label="Sensor Calibration")
t5  = Transition(label="Environment Adjust")
t6  = Transition(label="Nutrient Dosing")
t7  = Transition(label="Hydroponic Flow")
t8  = Transition(label="Robotic Pruning")
t9  = Transition(label="Health Monitor")
t10 = Transition(label="Harvesting Ops")
t11 = Transition(label="Data Analysis")
t12 = Transition(label="Predictive Check")
t13 = Transition(label="Waste Composting")
t14 = Transition(label="Water Recycling")
t15 = Transition(label="Eco Packaging")
t16 = Transition(label="Carbon Tracking")
t17 = Transition(label="Logistics Dispatch")

# Define the cycle of monitoring & maintenance as a partial order
growth_cycle = StrictPartialOrder(
    nodes=[t4, t5, t6, t7, t8, t9, t10, t11, t12]
)
growth_cycle.order.add_edge(t4,  t5)
growth_cycle.order.add_edge(t5,  t6)
growth_cycle.order.add_edge(t6,  t7)
growth_cycle.order.add_edge(t7,  t8)
growth_cycle.order.add_edge(t8,  t9)
growth_cycle.order.add_edge(t9,  t10)
growth_cycle.order.add_edge(t10, t11)
growth_cycle.order.add_edge(t11, t12)

# Wrap the growth cycle in a loop (repeat monitoring until exit)
loop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_cycle, growth_cycle]
)

# Build the top‐level process: seed → plant → (loop) → finalize
root = StrictPartialOrder(
    nodes=[t1, t2, t3, loop_cycle, t13, t14, t15, t16, t17]
)
root.order.add_edge(t1,  t2)
root.order.add_edge(t2,  t3)
root.order.add_edge(t3,  loop_cycle)
root.order.add_edge(loop_cycle, t13)
root.order.add_edge(t13, t14)
root.order.add_edge(t14, t15)
root.order.add_edge(t15, t16)
root.order.add_edge(t16, t17)