# Generated from: 9c69c021-a181-4094-a22b-cfe4d7323e99.json
# Description: This process involves the creation and market introduction of a niche artisan perfume line. Beginning with raw botanical sourcing from remote locations, the workflow includes scent formulation through iterative blending cycles, stability testing under varying environmental conditions, packaging design aligned with sustainable principles, and limited batch production using traditional methods. Following quality assurance, the marketing team crafts immersive storytelling campaigns targeting select luxury boutiques, followed by influencer collaboration and exclusive launch events. Post-launch, customer feedback is gathered via curated channels to inform future iterations and maintain brand authenticity in a competitive artisan space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
bot = Transition(label="Botanical Sourcing")
scent = Transition(label="Scent Formulation")
blend = Transition(label="Blend Testing")
stability = Transition(label="Stability Check")
pack = Transition(label="Packaging Design")
batch = Transition(label="Batch Production")
quality = Transition(label="Quality Review")
story = Transition(label="Story Crafting")
boutique = Transition(label="Boutique Targeting")
influencer = Transition(label="Influencer Outreach")
launch = Transition(label="Launch Planning")
event = Transition(label="Event Coordination")
feedback = Transition(label="Feedback Gathering")
iteration = Transition(label="Iteration Planning")
monitor = Transition(label="Brand Monitoring")

# Silent transition for loop exit
skip = SilentTransition()

# Build the iterative blending loop: Scent Formulation -> Blend Testing -> Stability Check
blend_seq = StrictPartialOrder(nodes=[scent, blend, stability])
blend_seq.order.add_edge(scent, blend)
blend_seq.order.add_edge(blend, stability)

# LOOP: repeat the blend sequence until stable
blend_loop = OperatorPOWL(operator=Operator.LOOP, children=[blend_seq, skip])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        bot,
        blend_loop,
        pack,
        batch,
        quality,
        story,
        boutique,
        influencer,
        launch,
        event,
        feedback,
        iteration,
        monitor
    ]
)

# Define the control‐flow edges
root.order.add_edge(bot, blend_loop)
root.order.add_edge(blend_loop, pack)
root.order.add_edge(pack, batch)
root.order.add_edge(batch, quality)
root.order.add_edge(quality, story)
root.order.add_edge(story, boutique)
root.order.add_edge(boutique, influencer)
root.order.add_edge(influencer, launch)
root.order.add_edge(launch, event)
root.order.add_edge(event, feedback)
root.order.add_edge(feedback, iteration)
root.order.add_edge(feedback, monitor)