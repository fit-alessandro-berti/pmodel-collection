# Generated from: a673c1a3-b543-4a19-9a53-932fb82be8f9.json
# Description: This process outlines the end-to-end workflow for managing international drone-based parcel delivery services. It involves complex coordination between drone fleet management, airspace compliance, customs clearance, real-time weather adaptation, dynamic routing, payload security verification, and automated customer notifications to ensure timely and secure cross-border shipments. The process requires continuous monitoring of regulatory changes in multiple jurisdictions, integration of AI-driven risk assessment modules, and contingency handling for drone malfunctions or restricted zones. Additionally, it incorporates blockchain-based tracking for transparency and dispute resolution, as well as post-delivery data analytics to optimize future operations and maintain service quality across diverse geographies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
fleet_check = Transition(label='Fleet Check')
route_plan = Transition(label='Route Plan')
weather_scan = Transition(label='Weather Scan')
airspace_clear = Transition(label='Airspace Clear')
payload_secure = Transition(label='Payload Secure')
flight_authorize = Transition(label='Flight Authorize')
customs_file = Transition(label='Customs File')
drone_launch = Transition(label='Drone Launch')
real_time_track = Transition(label='Real-time Track')
mid_flight_adjust = Transition(label='Mid-flight Adjust')
no_fly_zone = Transition(label='No-fly Zone')
delivery_confirm = Transition(label='Delivery Confirm')
return_route = Transition(label='Return Route')
post_flight_scan = Transition(label='Post-flight Scan')
data_sync = Transition(label='Data Sync')
performance_review = Transition(label='Performance Review')

# Pre-flight preparation partial order
pre_flight = StrictPartialOrder(nodes=[fleet_check, route_plan, weather_scan, airspace_clear, payload_secure])
pre_flight.order.add_edge(fleet_check, route_plan)
pre_flight.order.add_edge(route_plan, weather_scan)
pre_flight.order.add_edge(weather_scan, airspace_clear)
pre_flight.order.add_edge(airspace_clear, payload_secure)

# Authorization and customs clearance in parallel with final prep
auth = StrictPartialOrder(nodes=[flight_authorize, customs_file])
auth.order.add_edge(flight_authorize, customs_file)

prep_and_auth = StrictPartialOrder(nodes=[pre_flight, auth])
prep_and_auth.order.add_edge(pre_flight, auth)

# Launch follows clearance
launch_phase = StrictPartialOrder(nodes=[prep_and_auth, drone_launch])
launch_phase.order.add_edge(prep_and_auth, drone_launch)

# Flight partial order with possible loops for mid-flight adjustments and no-fly zones
# Represent mid-flight adjust and no-fly zone handling as a loop:
# After real-time track, either exit (continue flight) or:
# - Encounter no-fly zone, then mid-flight adjust, then back to real-time track
loop_body = StrictPartialOrder(nodes=[no_fly_zone, mid_flight_adjust])
loop_body.order.add_edge(no_fly_zone, mid_flight_adjust)

flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[real_time_track, loop_body])

# Delivery and return partial order
delivery_phase = StrictPartialOrder(nodes=[delivery_confirm, return_route])
delivery_phase.order.add_edge(delivery_confirm, return_route)

# Post-flight analytics partial order
post_flight_phase = StrictPartialOrder(nodes=[post_flight_scan, data_sync, performance_review])
post_flight_phase.order.add_edge(post_flight_scan, data_sync)
post_flight_phase.order.add_edge(data_sync, performance_review)

# Combine flight, delivery and post-flight phases in partial order
flight_and_post = StrictPartialOrder(nodes=[flight_loop, delivery_phase, post_flight_phase])
flight_and_post.order.add_edge(flight_loop, delivery_phase)
flight_and_post.order.add_edge(delivery_phase, post_flight_phase)

# Root process partial order combining launch and flight/post-flight phases
root = StrictPartialOrder(nodes=[launch_phase, flight_and_post])
root.order.add_edge(launch_phase, flight_and_post)