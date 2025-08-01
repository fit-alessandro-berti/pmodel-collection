# Generated from: 2524fe81-79fd-4674-a964-49fdbfdda127.json
# Description: This process outlines the end-to-end setup and execution of custom drone delivery services for specialized clients. It involves initial client consultation to understand unique delivery requirements, drone customization to meet payload and navigation needs, regulatory compliance checks including airspace permissions, route optimization considering weather and obstacles, pilot training and certification for specific drone models, real-time monitoring during delivery, incident response planning, and post-delivery analytics. The process ensures tailored solutions while maintaining safety, efficiency, and regulatory adherence in an emerging logistics sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
client_consult    = Transition(label='Client Consult')
needs_analysis    = Transition(label='Needs Analysis')
drone_design      = Transition(label='Drone Design')
payload_setup     = Transition(label='Payload Setup')
software_config   = Transition(label='Software Config')
regulatory_check  = Transition(label='Regulatory Check')
route_planning    = Transition(label='Route Planning')
pilot_assign      = Transition(label='Pilot Assign')
training_session  = Transition(label='Training Session')
incident_response = Transition(label='Incident Response')
preflight_check   = Transition(label='Preflight Check')
launch_drone      = Transition(label='Launch Drone')
monitor_flight    = Transition(label='Monitor Flight')
delivery_confirm  = Transition(label='Delivery Confirm')
data_review       = Transition(label='Data Review')
maintenance_log   = Transition(label='Maintenance Log')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    client_consult, needs_analysis, drone_design,
    payload_setup, software_config, regulatory_check,
    route_planning, pilot_assign, training_session,
    incident_response, preflight_check, launch_drone,
    monitor_flight, delivery_confirm, data_review,
    maintenance_log
])

# Define the control flow (dependencies)
root.order.add_edge(client_consult,    needs_analysis)
root.order.add_edge(needs_analysis,    drone_design)

# Drone customization can be done in parallel
root.order.add_edge(drone_design,      payload_setup)
root.order.add_edge(drone_design,      software_config)

# After both customization tasks, do the regulatory check
root.order.add_edge(payload_setup,     regulatory_check)
root.order.add_edge(software_config,   regulatory_check)

# Post‐check tasks in parallel: route planning, pilot assignment, incident response planning
root.order.add_edge(regulatory_check,  route_planning)
root.order.add_edge(regulatory_check,  pilot_assign)
root.order.add_edge(regulatory_check,  incident_response)

# Pilot assignment -> training
root.order.add_edge(pilot_assign,      training_session)

# All preflight prerequisites must complete before the preflight check
root.order.add_edge(route_planning,    preflight_check)
root.order.add_edge(training_session,  preflight_check)
root.order.add_edge(incident_response, preflight_check)

# Flight execution and post‐delivery steps
root.order.add_edge(preflight_check,   launch_drone)
root.order.add_edge(launch_drone,      monitor_flight)
root.order.add_edge(monitor_flight,    delivery_confirm)
root.order.add_edge(delivery_confirm,  data_review)
root.order.add_edge(data_review,       maintenance_log)