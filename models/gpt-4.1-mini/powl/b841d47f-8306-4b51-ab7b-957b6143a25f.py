# Generated from: b841d47f-8306-4b51-ab7b-957b6143a25f.json
# Description: This process involves the intricate creation of bespoke artisanal perfumes by blending rare natural essences through a series of highly specialized steps. Starting with ingredient sourcing from remote locations, the process continues through extraction, scent profiling, and iterative blending, incorporating sensory evaluations and stability testing. Packaging is customized for each batch with handcrafted bottles and personalized labels, followed by targeted marketing to niche luxury clients. The entire workflow requires coordination between botanists, chemists, and artisans to ensure each fragrance is unique, consistent, and meets high-quality standards before distribution to exclusive retail partners or direct clients.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Scent_Sourcing = Transition(label='Scent Sourcing')
Essence_Extract = Transition(label='Essence Extract')
Profile_Scents = Transition(label='Profile Scents')
Blend_Trial = Transition(label='Blend Trial')
Sensory_Test = Transition(label='Sensory Test')
Stability_Check = Transition(label='Stability Check')
Batch_Adjust = Transition(label='Batch Adjust')
Bottle_Craft = Transition(label='Bottle Craft')
Label_Design = Transition(label='Label Design')
Package_Assemble = Transition(label='Package Assemble')
Quality_Audit = Transition(label='Quality Audit')
Client_Consult = Transition(label='Client Consult')
Marketing_Prep = Transition(label='Marketing Prep')
Order_Manage = Transition(label='Order Manage')
Ship_Product = Transition(label='Ship Product')
Feedback_Review = Transition(label='Feedback Review')

# Loop part: iterative blending steps:
# loop = *(A=BlendTrial_Steps, B=Batch_Adjust)
# BlendTrial_Steps: Blend Trial -> Sensory Test -> Stability Check
BlendTrial_Steps = StrictPartialOrder(nodes=[Blend_Trial, Sensory_Test, Stability_Check])
BlendTrial_Steps.order.add_edge(Blend_Trial, Sensory_Test)
BlendTrial_Steps.order.add_edge(Sensory_Test, Stability_Check)

Loop_blending = OperatorPOWL(operator=Operator.LOOP, children=[BlendTrial_Steps, Batch_Adjust])

# Packaging partial order:
Packaging = StrictPartialOrder(nodes=[Bottle_Craft, Label_Design, Package_Assemble])
# Bottle Craft and Label Design concurrent, both precede packaging assemble
Packaging.order.add_edge(Bottle_Craft, Package_Assemble)
Packaging.order.add_edge(Label_Design, Package_Assemble)

# Marketing and order management partial order: Client Consult -> Marketing Prep -> Order Manage
Marketing_Flow = StrictPartialOrder(nodes=[Client_Consult, Marketing_Prep, Order_Manage])
Marketing_Flow.order.add_edge(Client_Consult, Marketing_Prep)
Marketing_Flow.order.add_edge(Marketing_Prep, Order_Manage)

# Shipping and feedback partial order: Order Manage -> Ship Product -> Feedback Review
Shipping_Flow = StrictPartialOrder(nodes=[Order_Manage, Ship_Product, Feedback_Review])
Shipping_Flow.order.add_edge(Order_Manage, Ship_Product)
Shipping_Flow.order.add_edge(Ship_Product, Feedback_Review)

# Quality audit should follow packaging before marketing starts
# Assembly of Packaging, Quality audit and Marketing_Flow in partial order:
Pack_Quality_Marketing = StrictPartialOrder(
    nodes=[Packaging, Quality_Audit, Marketing_Flow]
)
Pack_Quality_Marketing.order.add_edge(Packaging, Quality_Audit)
Pack_Quality_Marketing.order.add_edge(Quality_Audit, Marketing_Flow)

# Full process partial order:
# Start with sourcing, extraction, profiling scents in sequence
PreBlending = StrictPartialOrder(nodes=[Scent_Sourcing, Essence_Extract, Profile_Scents])
PreBlending.order.add_edge(Scent_Sourcing, Essence_Extract)
PreBlending.order.add_edge(Essence_Extract, Profile_Scents)

# Now order flow
root = StrictPartialOrder(
    nodes=[PreBlending, Loop_blending, Pack_Quality_Marketing, Shipping_Flow]
)

# Connect pre-blending to loop_blending
root.order.add_edge(PreBlending, Loop_blending)
# loop_blending to packaging/quality/marketing
root.order.add_edge(Loop_blending, Pack_Quality_Marketing)
# marketing flow to shipping flow
root.order.add_edge(Pack_Quality_Marketing, Shipping_Flow)