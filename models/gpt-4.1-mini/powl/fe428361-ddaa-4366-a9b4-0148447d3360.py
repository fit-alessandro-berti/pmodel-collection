# Generated from: fe428361-ddaa-4366-a9b4-0148447d3360.json
# Description: This process outlines the specialized workflow for custom drone delivery services tailored to high-value, fragile, or time-sensitive packages. It includes client consultation to determine delivery constraints, drone customization based on payload and environment, regulatory compliance checks, pre-flight simulations, and dynamic route optimization. Post-flight data analysis and client feedback integration ensure continuous improvement. The process also involves contingency management for weather disruptions or technical failures, warranty registration, and specialized packaging coordination to maintain package integrity during transport. Each stage is designed to ensure precision, safety, and customer satisfaction in an evolving regulatory landscape.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
ClientConsult = Transition(label='Client Consult')
PayloadAssess = Transition(label='Payload Assess')
DroneConfigure = Transition(label='Drone Configure')
RegulationCheck = Transition(label='Regulation Check')
FlightSimulate = Transition(label='Flight Simulate')
RouteOptimize = Transition(label='Route Optimize')
PackageSecure = Transition(label='Package Secure')
PreFlightInspect = Transition(label='Pre-Flight Inspect')
WeatherMonitor = Transition(label='Weather Monitor')
LaunchDrone = Transition(label='Launch Drone')
FlightTrack = Transition(label='Flight Track')
DeliveryConfirm = Transition(label='Delivery Confirm')
DataAnalyze = Transition(label='Data Analyze')
FeedbackCollect = Transition(label='Feedback Collect')
WarrantyRegister = Transition(label='Warranty Register')
IssueResolve = Transition(label='Issue Resolve')
PackageReturn = Transition(label='Package Return')

# Silent transition for loop exit
skip = SilentTransition()

# Contingency loop: Monitor weather, if issue resolve or package return, then re-check weather again or exit
contingency_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    WeatherMonitor,
    OperatorPOWL(operator=Operator.XOR, children=[
        skip,
        StrictPartialOrder(nodes=[IssueResolve, PackageReturn])
    ])
])

# Order partial order of main workflow before contingency
pre_flight = StrictPartialOrder(nodes=[
    ClientConsult,
    PayloadAssess,
    DroneConfigure,
    RegulationCheck,
    FlightSimulate,
    RouteOptimize,
    PackageSecure,
    PreFlightInspect
])
pre_flight.order.add_edge(ClientConsult, PayloadAssess)
pre_flight.order.add_edge(PayloadAssess, DroneConfigure)
pre_flight.order.add_edge(DroneConfigure, RegulationCheck)
pre_flight.order.add_edge(RegulationCheck, FlightSimulate)
pre_flight.order.add_edge(FlightSimulate, RouteOptimize)
pre_flight.order.add_edge(RouteOptimize, PackageSecure)
pre_flight.order.add_edge(PackageSecure, PreFlightInspect)

# Launch and Flight partial order
flight = StrictPartialOrder(nodes=[LaunchDrone, FlightTrack, DeliveryConfirm])
flight.order.add_edge(LaunchDrone, FlightTrack)
flight.order.add_edge(FlightTrack, DeliveryConfirm)

# Post-flight partial order
post_flight = StrictPartialOrder(nodes=[DataAnalyze, FeedbackCollect, WarrantyRegister])
post_flight.order.add_edge(DataAnalyze, FeedbackCollect)
post_flight.order.add_edge(FeedbackCollect, WarrantyRegister)

# Assemble the full workflow partial order
root = StrictPartialOrder(nodes=[pre_flight, contingency_loop, flight, post_flight])

# Ordering between the major blocks
root.order.add_edge(pre_flight, contingency_loop)   # After pre-flight, monitor weather loop starts
root.order.add_edge(contingency_loop, flight)       # After contingency met, launch and flight proceed
root.order.add_edge(flight, post_flight)            # After flight, post-flight activities
