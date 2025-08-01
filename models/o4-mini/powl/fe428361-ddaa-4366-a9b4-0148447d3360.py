# Generated from: fe428361-ddaa-4366-a9b4-0148447d3360.json
# Description: This process outlines the specialized workflow for custom drone delivery services tailored to high-value, fragile, or time-sensitive packages. It includes client consultation to determine delivery constraints, drone customization based on payload and environment, regulatory compliance checks, pre-flight simulations, and dynamic route optimization. Post-flight data analysis and client feedback integration ensure continuous improvement. The process also involves contingency management for weather disruptions or technical failures, warranty registration, and specialized packaging coordination to maintain package integrity during transport. Each stage is designed to ensure precision, safety, and customer satisfaction in an evolving regulatory landscape.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
client_consult       = Transition(label='Client Consult')
payload_assess       = Transition(label='Payload Assess')
drone_configure      = Transition(label='Drone Configure')
regulation_check     = Transition(label='Regulation Check')
package_secure       = Transition(label='Package Secure')
flight_simulate      = Transition(label='Flight Simulate')
route_optimize       = Transition(label='Route Optimize')
pre_flight_inspect   = Transition(label='Pre-Flight Inspect')
weather_monitor      = Transition(label='Weather Monitor')
launch_drone         = Transition(label='Launch Drone')
flight_track         = Transition(label='Flight Track')
delivery_confirm     = Transition(label='Delivery Confirm')
issue_resolve        = Transition(label='Issue Resolve')
data_analyze         = Transition(label='Data Analyze')
feedback_collect     = Transition(label='Feedback Collect')
package_return       = Transition(label='Package Return')
warranty_register    = Transition(label='Warranty Register')

# Core flight sequence A = Launch -> Track -> Confirm
flight_seq = StrictPartialOrder(nodes=[launch_drone, flight_track, delivery_confirm])
flight_seq.order.add_edge(launch_drone, flight_track)
flight_seq.order.add_edge(flight_track, delivery_confirm)

# Loop for contingency: do flight_seq, then on failure issue_resolve, repeat or exit
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_seq, issue_resolve])

# Post‐flight data & feedback branch
data_feedback = StrictPartialOrder(nodes=[data_analyze, feedback_collect])
data_feedback.order.add_edge(data_analyze, feedback_collect)

# Package return branch
return_branch = StrictPartialOrder(nodes=[package_return])

# Choice after flight: either data&feedback or package return
final_choice = OperatorPOWL(operator=Operator.XOR, children=[data_feedback, return_branch])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    client_consult,
    payload_assess,
    drone_configure,
    regulation_check,
    package_secure,
    flight_simulate,
    route_optimize,
    pre_flight_inspect,
    weather_monitor,
    flight_loop,
    final_choice,
    warranty_register
])

# Define control-flow order
root.order.add_edge(client_consult,     payload_assess)
root.order.add_edge(payload_assess,     drone_configure)
root.order.add_edge(drone_configure,    regulation_check)
root.order.add_edge(regulation_check,   package_secure)
root.order.add_edge(package_secure,     flight_simulate)
root.order.add_edge(flight_simulate,    route_optimize)
root.order.add_edge(route_optimize,     pre_flight_inspect)
# Weather monitoring starts after pre‐flight inspect, concurrent with flight_loop
root.order.add_edge(pre_flight_inspect, weather_monitor)
# After inspection we enter the contingency‐aware flight loop
root.order.add_edge(pre_flight_inspect, flight_loop)
# After the loop completes (successful delivery), make the final choice
root.order.add_edge(flight_loop,        final_choice)
# Then register warranty regardless of branch
root.order.add_edge(final_choice,       warranty_register)