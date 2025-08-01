# Generated from: a673c1a3-b543-4a19-9a53-932fb82be8f9.json
# Description: This process outlines the end-to-end workflow for managing international drone-based parcel delivery services. It involves complex coordination between drone fleet management, airspace compliance, customs clearance, real-time weather adaptation, dynamic routing, payload security verification, and automated customer notifications to ensure timely and secure cross-border shipments. The process requires continuous monitoring of regulatory changes in multiple jurisdictions, integration of AI-driven risk assessment modules, and contingency handling for drone malfunctions or restricted zones. Additionally, it incorporates blockchain-based tracking for transparency and dispute resolution, as well as post-delivery data analytics to optimize future operations and maintain service quality across diverse geographies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
fleet_check = Transition(label="Fleet Check")
route_plan = Transition(label="Route Plan")
weather_scan = Transition(label="Weather Scan")
airspace_clear = Transition(label="Airspace Clear")
payload_secure = Transition(label="Payload Secure")
flight_authorize = Transition(label="Flight Authorize")
customs_file = Transition(label="Customs File")
drone_launch = Transition(label="Drone Launch")
real_time_track = Transition(label="Real-time Track")
mid_flight_adjust = Transition(label="Mid-flight Adjust")
no_fly_zone = Transition(label="No-fly Zone")
delivery_confirm = Transition(label="Delivery Confirm")
return_route = Transition(label="Return Route")
post_flight_scan = Transition(label="Post-flight Scan")
data_sync = Transition(label="Data Sync")
performance_review = Transition(label="Performance Review")

# Build the in-flight contingency choice: either adjust mid-flight or handle no-fly zone
in_flight_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[mid_flight_adjust, no_fly_zone]
)

# Build the flight loop: continuously track, then optionally handle contingencies, then track again, until exit
flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[real_time_track, in_flight_choice]
)

# Assemble the full process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        fleet_check,
        route_plan,
        weather_scan,
        airspace_clear,
        payload_secure,
        flight_authorize,
        customs_file,
        drone_launch,
        flight_loop,
        delivery_confirm,
        return_route,
        post_flight_scan,
        data_sync,
        performance_review
    ]
)

# Define the control-flow edges (sequence)
root.order.add_edge(fleet_check, route_plan)
root.order.add_edge(route_plan, weather_scan)
root.order.add_edge(weather_scan, airspace_clear)
root.order.add_edge(airspace_clear, payload_secure)
root.order.add_edge(payload_secure, flight_authorize)
root.order.add_edge(flight_authorize, customs_file)
root.order.add_edge(customs_file, drone_launch)
root.order.add_edge(drone_launch, flight_loop)
root.order.add_edge(flight_loop, delivery_confirm)
root.order.add_edge(delivery_confirm, return_route)
root.order.add_edge(return_route, post_flight_scan)
root.order.add_edge(post_flight_scan, data_sync)
root.order.add_edge(data_sync, performance_review)