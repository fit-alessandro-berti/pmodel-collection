# Generated from: f0c57729-9608-427e-940c-019931fda78e.json
# Description: This process manages the end-to-end workflow of commissioning custom artwork from initial client inquiry to final delivery. It includes client consultation, concept drafting, iterative feedback cycles, contract negotiation with unique terms, artist assignment based on style matching, material sourcing with ethical considerations, progress tracking with milestone reviews, quality assurance involving third-party evaluation, legal copyright transfer, packaging design for fragile items, and post-delivery support including care instructions and follow-up surveys. This atypical process ensures both artist creativity and client satisfaction through structured yet flexible collaboration while addressing logistics, legalities, and customer experience comprehensively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
inquiry = Transition(label='Inquiry Intake')
consult = Transition(label='Consultation Call')
concept = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
contract = Transition(label='Contract Setup')
match = Transition(label='Artist Match')
sourcing = Transition(label='Material Sourcing')
ethics = Transition(label='Ethics Review')
progress = Transition(label='Progress Check')
milestone = Transition(label='Milestone Approve')
quality = Transition(label='Quality Audit')
copyright_ = Transition(label='Copyright Transfer')
packaging = Transition(label='Packaging Plan')
shipping = Transition(label='Shipping Arrange')
post = Transition(label='Post Delivery')
survey = Transition(label='Client Survey')

# Feedback iterations: concept followed by optional feedback cycles
loop = OperatorPOWL(operator=Operator.LOOP, children=[concept, feedback])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    inquiry, consult, loop, contract, match, sourcing, ethics,
    progress, milestone, quality, copyright_,
    packaging, shipping, post, survey
])

# Define the sequence dependencies
root.order.add_edge(inquiry, consult)
root.order.add_edge(consult, loop)
root.order.add_edge(loop, contract)
root.order.add_edge(contract, match)
root.order.add_edge(match, sourcing)
root.order.add_edge(sourcing, ethics)
root.order.add_edge(ethics, progress)
root.order.add_edge(progress, milestone)
root.order.add_edge(milestone, quality)
root.order.add_edge(quality, copyright_)
root.order.add_edge(copyright_, packaging)
root.order.add_edge(packaging, shipping)
root.order.add_edge(shipping, post)
root.order.add_edge(post, survey)