# Generated from: e458e94a-0166-465f-b120-3f590c5f341e.json
# Description: This process manages the end-to-end workflow for commissioning custom artwork from initial client inquiry through final delivery and post-sale support. It includes client onboarding, concept development, iterative feedback loops, contract negotiation, milestone payments, artwork creation, quality assurance, framing coordination, shipping logistics, and customer satisfaction follow-up. The process ensures tailored communication between artist and client while maintaining clear documentation and legal compliance throughout. It also incorporates contingency planning for creative revisions and unexpected delays, ensuring a seamless experience from idea inception to completed commissioned piece delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
inq = Transition(label='Inquiry Review')
onboard = Transition(label='Client Onboard')
concept = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Cycle')
revision = Transition(label='Revision Manage')
contract = Transition(label='Contract Setup')
payment = Transition(label='Payment Schedule')
sourcing = Transition(label='Material Sourcing')
artwork = Transition(label='Artwork Create')
quality = Transition(label='Quality Check')
framing = Transition(label='Frame Selection')
packaging = Transition(label='Packaging Prep')
shipment = Transition(label='Shipment Arrange')
delay = Transition(label='Delay Mitigate')
delivery = Transition(label='Delivery Confirm')
post_support = Transition(label='Post-Sale Support')

# Sub‐process: feedback + revision loop (creative revisions)
po_feedback = StrictPartialOrder(nodes=[feedback, revision])
po_feedback.order.add_edge(feedback, revision)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[concept, po_feedback])

# Sub‐process: contract negotiation, payment schedule, material sourcing
contract_flow = StrictPartialOrder(nodes=[contract, payment, sourcing])
contract_flow.order.add_edge(contract, payment)
contract_flow.order.add_edge(payment, sourcing)

# Sub‐process: artwork creation + quality check
artwork_flow = StrictPartialOrder(nodes=[artwork, quality])
artwork_flow.order.add_edge(artwork, quality)

# Sub‐process: framing + packaging
packaging_flow = StrictPartialOrder(nodes=[framing, packaging])
packaging_flow.order.add_edge(framing, packaging)

# Sub‐process: shipping + delay mitigation loop
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[shipment, delay])

# Root partial order stitching everything together
root = StrictPartialOrder(nodes=[
    inq,
    onboard,
    feedback_loop,
    contract_flow,
    artwork_flow,
    packaging_flow,
    shipping_loop,
    delivery,
    post_support
])

# Define the overall sequencing constraints
root.order.add_edge(inq, onboard)
root.order.add_edge(onboard, feedback_loop)
root.order.add_edge(onboard, contract_flow)
root.order.add_edge(feedback_loop, artwork_flow)
root.order.add_edge(contract_flow, artwork_flow)
root.order.add_edge(artwork_flow, packaging_flow)
root.order.add_edge(packaging_flow, shipping_loop)
root.order.add_edge(shipping_loop, delivery)
root.order.add_edge(delivery, post_support)