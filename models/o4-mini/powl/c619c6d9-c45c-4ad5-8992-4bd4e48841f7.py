# Generated from: c619c6d9-c45c-4ad5-8992-4bd4e48841f7.json
# Description: This process involves the bespoke assembly of unmanned aerial vehicles tailored to specific client requirements. Starting from initial design consultation, the workflow includes component sourcing from multiple specialized suppliers, precision calibration of sensors, custom firmware integration, iterative flight testing in controlled environments, and compliance verification with aviation regulations. The process demands cross-functional coordination among engineering, quality assurance, software development, and logistics teams to ensure timely delivery of fully operational drones equipped with client-specific payloads and optimized flight parameters.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
design          = Transition(label='Design Consult')
component       = Transition(label='Component Sourcing')
sensor          = Transition(label='Sensor Calibrate')
firmware        = Transition(label='Firmware Integrate')
payload         = Transition(label='Payload Configure')
assembly        = Transition(label='Assembly Setup')
wiring          = Transition(label='Wiring Connect')
chassis         = Transition(label='Chassis Build')
software        = Transition(label='Software Load')
testing         = Transition(label='Flight Testing')
analyze         = Transition(label='Data Analyze')
regulation      = Transition(label='Regulation Check')
quality         = Transition(label='Quality Inspect')
packaging       = Transition(label='Packaging Prep')
logistics       = Transition(label='Logistics Plan')
client_review   = Transition(label='Client Review')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    design, component, sensor, firmware, payload,
    assembly, wiring, chassis, software, testing,
    analyze, regulation, quality, packaging,
    logistics, client_review
])

# Add control‐flow dependencies
root.order.add_edge(design,        component)
root.order.add_edge(component,     sensor)
root.order.add_edge(sensor,        firmware)
root.order.add_edge(firmware,      payload)
root.order.add_edge(payload,       assembly)

# Assembly splits into wiring and chassis (concurrent after setup)
root.order.add_edge(assembly,      wiring)
root.order.add_edge(assembly,      chassis)

# Both wiring and chassis must finish before software load
root.order.add_edge(wiring,        software)
root.order.add_edge(chassis,       software)

# Continue sequentially
root.order.add_edge(software,      testing)
root.order.add_edge(testing,       analyze)

# After data analysis, perform regulation check and quality inspection in parallel
root.order.add_edge(analyze,       regulation)
root.order.add_edge(analyze,       quality)

# Packaging and logistics follow their respective checks
root.order.add_edge(regulation,    packaging)
root.order.add_edge(quality,       logistics)

# Final client review requires both packaging and logistics to complete
root.order.add_edge(packaging,     client_review)
root.order.add_edge(logistics,     client_review)