# Generated from: 4631eca5-d3e7-4500-9982-5b5530aa7531.json
# Description: This process involves the custom assembly of drones tailored to individual client specifications. It starts with detailed requirement gathering and design adaptation, followed by component sourcing from multiple suppliers, quality verification, and firmware customization. The assembly line incorporates manual and automated steps ensuring precision fitting of sensors, motors, and batteries. Post assembly, each drone undergoes rigorous flight testing in various conditions, calibration of navigation systems, and software integration. Final packaging includes client-specific documentation and configuration files. The entire process requires iterative feedback loops between design and production teams to accommodate rapid changes and ensure compliance with aviation regulations before shipment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities as POWL transitions
req = Transition(label='Req Gathering')
design = Transition(label='Design Adapt')
vetting = Transition(label='Supplier Vetting')
order = Transition(label='Component Order')
quality = Transition(label='Quality Check')
firmware = Transition(label='Firmware Load')
sensor = Transition(label='Sensor Fit')
motor = Transition(label='Motor Install')
battery = Transition(label='Battery Mount')
assembly = Transition(label='Assembly Test')
flight = Transition(label='Flight Trial')
nav = Transition(label='Nav Calibrate')
sync = Transition(label='Software Sync')
doc = Transition(label='Doc Prepare')
client = Transition(label='Client Review')
final = Transition(label='Final Package')
compliance = Transition(label='Compliance Audit')

# Build the “production” phase (from design adaptation through software sync)
A = StrictPartialOrder(nodes=[
    design, vetting, order, quality, firmware,
    sensor, motor, battery, assembly, flight,
    nav, sync
])
A.order.add_edge(design, vetting)
A.order.add_edge(vetting, order)
A.order.add_edge(order, quality)
A.order.add_edge(quality, firmware)
A.order.add_edge(firmware, sensor)
A.order.add_edge(sensor, motor)
A.order.add_edge(motor, battery)
A.order.add_edge(battery, assembly)
A.order.add_edge(assembly, flight)
A.order.add_edge(flight, nav)
A.order.add_edge(nav, sync)

# Loop feedback: after completing A, either exit or go back to design
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, design])

# Build the top‐level workflow: requirements → (looping production) → final packaging & audit
root = StrictPartialOrder(nodes=[req, loop, doc, client, final, compliance])
root.order.add_edge(req, loop)
root.order.add_edge(loop, doc)
root.order.add_edge(doc, client)
root.order.add_edge(client, final)
root.order.add_edge(final, compliance)