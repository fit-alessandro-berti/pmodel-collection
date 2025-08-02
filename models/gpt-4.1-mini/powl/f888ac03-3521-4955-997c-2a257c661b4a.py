# Generated from: f888ac03-3521-4955-997c-2a257c661b4a.json
# Description: This process manages the end-to-end operation of urban drone deliveries for perishable goods. It includes initial order validation, dynamic route optimization considering real-time air traffic and weather conditions, automated drone dispatch, continuous in-flight monitoring with obstacle avoidance, secure parcel handoff using biometric verification, and post-delivery data analytics to improve future efficiency. The workflow integrates cross-functional teams and advanced AI algorithms to ensure timely, safe, and compliant deliveries within congested city environments, adapting dynamically to unexpected disruptions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
order_validate = Transition(label='Order Validate')
route_optimize = Transition(label='Route Optimize')
drone_assign = Transition(label='Drone Assign')
preflight_check = Transition(label='Preflight Check')
load_package = Transition(label='Load Package')
flight_launch = Transition(label='Flight Launch')
traffic_monitor = Transition(label='Traffic Monitor')
weather_assess = Transition(label='Weather Assess')
obstacle_avoid = Transition(label='Obstacle Avoid')
battery_check = Transition(label='Battery Check')
delivery_verify = Transition(label='Delivery Verify')
biometric_scan = Transition(label='Biometric Scan')
package_release = Transition(label='Package Release')
return_flight = Transition(label='Return Flight')
post_flight = Transition(label='Post Flight')
data_analyze = Transition(label='Data Analyze')
feedback_collect = Transition(label='Feedback Collect')

# Dynamic route optimization partial order: traffic_monitor and weather_assess concurrent, both depend on route_optimize
dynamic_route_opt = StrictPartialOrder(nodes=[route_optimize, traffic_monitor, weather_assess])
dynamic_route_opt.order.add_edge(route_optimize, traffic_monitor)
dynamic_route_opt.order.add_edge(route_optimize, weather_assess)

# In-flight monitoring partial order: obstacle_avoid and battery_check concurrent, both depend on flight_launch
in_flight_monitor = StrictPartialOrder(nodes=[flight_launch, obstacle_avoid, battery_check])
in_flight_monitor.order.add_edge(flight_launch, obstacle_avoid)
in_flight_monitor.order.add_edge(flight_launch, battery_check)

# Delivery verification partial order: biometric_scan then package_release, both depend on delivery_verify
delivery_security = StrictPartialOrder(nodes=[delivery_verify, biometric_scan, package_release])
delivery_security.order.add_edge(delivery_verify, biometric_scan)
delivery_security.order.add_edge(biometric_scan, package_release)

# Post-delivery partial order: data_analyze then feedback_collect
post_delivery = StrictPartialOrder(nodes=[data_analyze, feedback_collect])
post_delivery.order.add_edge(data_analyze, feedback_collect)

# Pre-flight checks partial order: preflight_check then load_package (sequential)
pre_flight = StrictPartialOrder(nodes=[preflight_check, load_package])
pre_flight.order.add_edge(preflight_check, load_package)

# Flight sequence partial order: flight_launch then in-flight monitoring then delivery verification then package release then return flight
# We can merge in_flight_monitor and delivery_security, respecting order between flight_launch->in_flight_monitor and then delivery_security starting after in_flight_monitor
flight_and_delivery = StrictPartialOrder(nodes=[flight_launch, obstacle_avoid, battery_check,
                                                delivery_verify, biometric_scan, package_release,
                                                return_flight])
flight_and_delivery.order.add_edge(flight_launch, obstacle_avoid)
flight_and_delivery.order.add_edge(flight_launch, battery_check)
flight_and_delivery.order.add_edge(obstacle_avoid, delivery_verify)
flight_and_delivery.order.add_edge(battery_check, delivery_verify)
flight_and_delivery.order.add_edge(delivery_verify, biometric_scan)
flight_and_delivery.order.add_edge(biometric_scan, package_release)
flight_and_delivery.order.add_edge(package_release, return_flight)

# Full sequence construction:
# Order Validate -> dynamic_route_opt -> drone_assign -> pre_flight -> flight_and_delivery -> post_flight -> post_delivery

# Compose all nodes involved in one StrictPartialOrder for the overall sequence except post_delivery which can run concurrently with feedback_collect (part of post_delivery)
overall_sequence_nodes = [order_validate, dynamic_route_opt, drone_assign, pre_flight,
                          flight_and_delivery, post_flight]

overall_sequence = StrictPartialOrder(nodes=overall_sequence_nodes)
overall_sequence.order.add_edge(order_validate, dynamic_route_opt)
overall_sequence.order.add_edge(dynamic_route_opt, drone_assign)
overall_sequence.order.add_edge(drone_assign, pre_flight)
overall_sequence.order.add_edge(pre_flight, flight_and_delivery)
overall_sequence.order.add_edge(flight_and_delivery, post_flight)

# post_delivery depends on post_flight
post_delivery_with_dep = StrictPartialOrder(nodes=[post_flight, data_analyze, feedback_collect])
post_delivery_with_dep.order.add_edge(post_flight, data_analyze)
post_delivery_with_dep.order.add_edge(data_analyze, feedback_collect)

# Root POWL: combine overall_sequence and post_delivery_with_dep concurrent (feedback_collect waits for data_analyze, which waits for post_flight)
root = StrictPartialOrder(nodes=[overall_sequence, post_delivery_with_dep])