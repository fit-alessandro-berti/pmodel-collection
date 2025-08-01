# Generated from: 95850c46-42b9-474f-b989-4ca730949347.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm integrating IoT sensors, AI-driven climate control, and hydroponic systems. It involves seed selection based on market trends, nutrient solution calibration, automated seeding, and environmental monitoring. Continuous data analysis optimizes growth conditions while predictive maintenance ensures equipment uptime. Post-harvest, produce undergoes quality sorting, packaging with sustainable materials, and direct-to-consumer distribution via an app platform. The process also includes waste recycling into bio-fertilizers and real-time feedback integration from customers to adjust crop varieties and schedules, maximizing yield in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
seeding = Transition(label='Automated Seeding')
sensor = Transition(label='Sensor Calibration')
climate = Transition(label='Climate Control')
monitor = Transition(label='Growth Monitoring')
analysis = Transition(label='Data Analysis')
repair = Transition(label='Predictive Repair')
harvest = Transition(label='Harvest Sorting')
packaging = Transition(label='Eco Packaging')
dispatch = Transition(label='Order Dispatch')
feedback = Transition(label='Customer Feedback')
recycling = Transition(label='Waste Recycling')
adjust = Transition(label='Crop Adjustment')
report = Transition(label='Yield Reporting')

# Build the environmental-control loop: Sensor Calibration, then
# Climate Control -> Growth Monitoring -> Data Analysis -> Predictive Repair
cycle_body = StrictPartialOrder(
    nodes=[climate, monitor, analysis, repair]
)
cycle_body.order.add_edge(climate, monitor)
cycle_body.order.add_edge(monitor, analysis)
cycle_body.order.add_edge(analysis, repair)

env_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sensor, cycle_body]
)

# Top‐level partial order
root = StrictPartialOrder(
    nodes=[
        seed,
        nutrient,
        seeding,
        env_loop,
        harvest,
        packaging,
        dispatch,
        feedback,
        adjust,
        report,
        recycling
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, seeding)
root.order.add_edge(seeding, env_loop)
root.order.add_edge(env_loop, harvest)
root.order.add_edge(harvest, packaging)
root.order.add_edge(packaging, dispatch)
root.order.add_edge(dispatch, feedback)
root.order.add_edge(feedback, adjust)
root.order.add_edge(adjust, report)
# Waste recycling can start right after harvest independently
root.order.add_edge(harvest, recycling)