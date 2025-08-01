# Generated from: 958fc63f-191e-43b4-bab2-01fee66f885a.json
# Description: This process involves the design, development, and assembly of custom drones tailored for specialized applications such as environmental monitoring, precision agriculture, and industrial inspection. Starting from client consultation to understand unique requirements, it proceeds through iterative prototype design, component sourcing from niche suppliers, and integration of advanced sensors. Quality assurance includes rigorous flight testing under varied conditions and software calibration for autonomous navigation. The process concludes with client training and after-sales support including firmware updates and maintenance scheduling to ensure optimal drone performance over its operational lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
client        = Transition(label='Client Consult')
req           = Transition(label='Requirement Gather')
concept       = Transition(label='Concept Sketch')
prototype     = Transition(label='Prototype Build')
sensor        = Transition(label='Sensor Select')
component     = Transition(label='Component Source')
flight        = Transition(label='Flight Testing')
upload        = Transition(label='Software Upload')
autonomy      = Transition(label='Autonomy Setup')
calibration   = Transition(label='Calibration Run')
quality       = Transition(label='Quality Check')
pack          = Transition(label='Packaging Prep')
training      = Transition(label='Client Training')
warranty      = Transition(label='Warranty Setup')
maintenance   = Transition(label='Maintenance Plan')
firmware      = Transition(label='Firmware Update')

# QA loop: Flight Testing, then (Software Upload -> Autonomy Setup -> Calibration Run) repeatedly
sub_qa = StrictPartialOrder(nodes=[upload, autonomy, calibration])
sub_qa.order.add_edge(upload, autonomy)
sub_qa.order.add_edge(autonomy, calibration)
qa_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight, sub_qa])

# After‐sales loop: Maintenance Plan, then optionally Firmware Update repeatedly
as_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance, firmware])

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        client, req, concept, prototype,
        sensor, component,
        qa_loop, quality,
        pack, training, warranty,
        as_loop
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(client, req)
root.order.add_edge(req, concept)
root.order.add_edge(concept, prototype)
root.order.add_edge(prototype, sensor)
root.order.add_edge(prototype, component)
root.order.add_edge(sensor, qa_loop)
root.order.add_edge(component, qa_loop)
root.order.add_edge(qa_loop, quality)
root.order.add_edge(quality, pack)
root.order.add_edge(pack, training)
root.order.add_edge(training, warranty)
root.order.add_edge(warranty, as_loop)