# Generated from: 89c8d38c-bb5b-44bd-9300-57f88e71e9dc.json
# Description: This process involves the design, assembly, testing, and deployment of bespoke drones tailored for unique environmental monitoring tasks. It starts with client consultation to gather specific requirements, followed by component sourcing and integration of advanced sensors. After assembly, drones undergo rigorous flight simulation and real-world testing to ensure reliability under diverse conditions. Post-testing includes software calibration and custom firmware updates. Finally, drones are packaged with operation manuals and shipped alongside remote support setup for client training and maintenance scheduling to guarantee optimal long-term performance and compliance with aviation regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
client_consult     = Transition(label='Client Consult')
requirement_gather = Transition(label='Requirement Gather')
component_sourcing = Transition(label='Component Sourcing')
sensor_integration = Transition(label='Sensor Integration')
frame_assembly     = Transition(label='Frame Assembly')
quality_inspect    = Transition(label='Quality Inspect')
flight_simulate    = Transition(label='Flight Simulate')
real_test          = Transition(label='Real Test')
data_calibration   = Transition(label='Data Calibration')
firmware_upload    = Transition(label='Firmware Upload')
packaging_prep     = Transition(label='Packaging Prep')
manual_draft       = Transition(label='Manual Draft')
shipping_arrange   = Transition(label='Shipping Arrange')
support_setup      = Transition(label='Support Setup')
training_schedule  = Transition(label='Training Schedule')
maintenance_plan   = Transition(label='Maintenance Plan')

# Create the partial‐order model
root = StrictPartialOrder(nodes=[
    client_consult, requirement_gather, component_sourcing, sensor_integration,
    frame_assembly, quality_inspect, flight_simulate, real_test,
    data_calibration, firmware_upload,
    packaging_prep, manual_draft, shipping_arrange,
    support_setup, training_schedule, maintenance_plan
])

# Sequential design → assembly → testing → calibration → firmware
root.order.add_edge(client_consult,     requirement_gather)
root.order.add_edge(requirement_gather, component_sourcing)
root.order.add_edge(component_sourcing, sensor_integration)
root.order.add_edge(sensor_integration, frame_assembly)
root.order.add_edge(frame_assembly,     quality_inspect)
root.order.add_edge(quality_inspect,    flight_simulate)
root.order.add_edge(flight_simulate,    real_test)
root.order.add_edge(real_test,          data_calibration)
root.order.add_edge(data_calibration,   firmware_upload)

# After firmware upload, split into packaging/manual and support streams
root.order.add_edge(firmware_upload, packaging_prep)
root.order.add_edge(firmware_upload, manual_draft)
root.order.add_edge(firmware_upload, support_setup)
root.order.add_edge(firmware_upload, training_schedule)
root.order.add_edge(firmware_upload, maintenance_plan)

# Shipping depends on both packaging and manual draft
root.order.add_edge(packaging_prep,   shipping_arrange)
root.order.add_edge(manual_draft,     shipping_arrange)