# Generated from: 124e15ad-987b-450b-8f44-6b8dac5a2417.json
# Description: This process outlines the complex and atypical supply chain involved in producing artisan cheese from small-scale farms to niche gourmet shops. It begins with seasonal milk collection, followed by precise fermentation control, handcrafting curd molding, and quality maturation monitoring. The process includes sensory evaluation panels, organic certification audits, and custom packaging design tailored to regional tastes. Distribution leverages specialized cold transport logistics and direct-to-chef delivery schedules. Feedback loops from retailers and consumers inform iterative recipe adjustments, ensuring unique flavors and consistent quality across batches. Sustainability tracking and waste repurposing are integrated throughout, emphasizing eco-conscious production and community engagement within a localized artisan network.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Milk_Harvest = Transition(label='Milk Harvest')
Fermentation_Check = Transition(label='Fermentation Check')
Curd_Molding = Transition(label='Curd Molding')
Salt_Application = Transition(label='Salt Application')
Pressing_Stage = Transition(label='Pressing Stage')
Maturation_Monitor = Transition(label='Maturation Monitor')
Quality_Testing = Transition(label='Quality Testing')
Sensory_Panel = Transition(label='Sensory Panel')
Certification_Audit = Transition(label='Certification Audit')
Packaging_Design = Transition(label='Packaging Design')
Cold_Transport = Transition(label='Cold Transport')
Retail_Delivery = Transition(label='Retail Delivery')
Consumer_Feedback = Transition(label='Consumer Feedback')
Recipe_Tuning = Transition(label='Recipe Tuning')
Waste_Recycling = Transition(label='Waste Recycling')

# Define the core sequence before distribution
pre_distribution = StrictPartialOrder(
    nodes=[
        Milk_Harvest,
        Fermentation_Check,
        Curd_Molding,
        Salt_Application,
        Pressing_Stage,
        Maturation_Monitor,
        Quality_Testing,
        Sensory_Panel,
        Certification_Audit,
        Packaging_Design,
    ]
)
pre_distribution.order.add_edge(Milk_Harvest, Fermentation_Check)
pre_distribution.order.add_edge(Fermentation_Check, Curd_Molding)
pre_distribution.order.add_edge(Curd_Molding, Salt_Application)
pre_distribution.order.add_edge(Salt_Application, Pressing_Stage)
pre_distribution.order.add_edge(Pressing_Stage, Maturation_Monitor)
pre_distribution.order.add_edge(Maturation_Monitor, Quality_Testing)
pre_distribution.order.add_edge(Quality_Testing, Sensory_Panel)
pre_distribution.order.add_edge(Sensory_Panel, Certification_Audit)
pre_distribution.order.add_edge(Certification_Audit, Packaging_Design)

# Distribution nodes partial order (can be concurrent)
distribution = StrictPartialOrder(
    nodes=[Cold_Transport, Retail_Delivery]
)
# No order edges => Cold_Transport and Retail_Delivery are concurrent

# Feedback loop: Consumer_Feedback and Recipe_Tuning in a loop after Retail_Delivery
feedback_loop_body = StrictPartialOrder(
    nodes=[Consumer_Feedback, Waste_Recycling]
)
# Waste_Recycling runs concurrently with Consumer_Feedback in feedback loop body
# They are concurrent, so no edges

feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Retail_Delivery,
        StrictPartialOrder(
            nodes=[feedback_loop_body, Recipe_Tuning]
        )
    ]
)
# Add edges inside the loop child:
# Recipe_Tuning occurs after feedback_loop_body completes,
# (note: children=[Retail_Delivery, PO], so inside PO define internal order)
# To model "iterative recipe adjustments" after feedback and recycling, Recipe_Tuning after feedback body

feedback_loop.children[1].order.add_edge(feedback_loop_body, Recipe_Tuning)

# Full root partial order: pre_distribution --> distribution --> feedback_loop
root = StrictPartialOrder(
    nodes=[pre_distribution, distribution, feedback_loop]
)
root.order.add_edge(pre_distribution, distribution)
root.order.add_edge(distribution, feedback_loop)