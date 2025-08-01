# Generated from: f43b35e4-f493-452b-918e-6f2bb594fac9.json
# Description: This process outlines the intricate steps involved in custom drone assembly, which includes initial client consultation, bespoke component design, precision part fabrication, iterative software calibration, and rigorous quality assurance testing. The workflow incorporates multiple feedback loops between hardware adjustments and software tuning to ensure optimal flight performance. Post-assembly, drones undergo environmental stress testing and client-specific payload integration, followed by final certification and delivery scheduling. This atypical process demands close coordination between engineering, design, and logistics teams to meet unique client specifications within tight deadlines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
client = Transition(label='Client Brief')
design = Transition(label='Design Draft')
sourcing = Transition(label='Part Sourcing')
fabric = Transition(label='Component Fabric')
assembly = Transition(label='Circuit Assembly')
upload = Transition(label='Software Upload')
initial_test = Transition(label='Initial Testing')
calibrate = Transition(label='Flight Calibrate')
feedback = Transition(label='Feedback Loop')
stress = Transition(label='Stress Testing')
payload = Transition(label='Payload Mount')
quality = Transition(label='Quality Check')
cert = Transition(label='Certification')
packaging = Transition(label='Packaging')
delivery = Transition(label='Delivery Plan')
support = Transition(label='Post Support')

# Pre-loop partial order: design → sourcing → fabric → assembly → upload → initial test → calibrate → quality check
pre_loop = StrictPartialOrder(nodes=[
    design, sourcing, fabric, assembly,
    upload, initial_test, calibrate, quality
])
pre_loop.order.add_edge(design, sourcing)
pre_loop.order.add_edge(sourcing, fabric)
pre_loop.order.add_edge(fabric, assembly)
pre_loop.order.add_edge(assembly, upload)
pre_loop.order.add_edge(upload, initial_test)
pre_loop.order.add_edge(initial_test, calibrate)
pre_loop.order.add_edge(calibrate, quality)

# Loop for iterative feedback between calibration and adjustments
loop = OperatorPOWL(operator=Operator.LOOP, children=[pre_loop, feedback])

# Main workflow partial order
root = StrictPartialOrder(nodes=[
    client,      # client consultation
    pre_loop,    # initial design → build → calibrate → QA
    loop,        # feedback loop
    stress,      # environmental stress testing
    payload,     # client-specific payload mounting
    cert,        # final certification
    packaging,   # packaging
    delivery,    # delivery plan
    support      # post‐delivery support
])
root.order.add_edge(client, pre_loop)
root.order.add_edge(pre_loop, loop)
root.order.add_edge(loop, stress)
root.order.add_edge(stress, payload)
root.order.add_edge(payload, cert)
root.order.add_edge(cert, packaging)
root.order.add_edge(packaging, delivery)
root.order.add_edge(delivery, support)