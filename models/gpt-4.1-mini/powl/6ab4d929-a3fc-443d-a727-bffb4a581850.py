# Generated from: 6ab4d929-a3fc-443d-a727-bffb4a581850.json
# Description: This process outlines the detailed steps involved in producing and distributing artisanal cheese from small-scale farms to gourmet retail outlets. It includes raw milk collection from diverse breeds, precise temperature-controlled fermentation, multiple rounds of quality assessment, packaging with eco-friendly materials, specialized cold-chain logistics, and targeted marketing to niche consumers. The process also incorporates feedback loops with cheesemakers and retailers to continually refine taste profiles and shelf life, ensuring product consistency and brand reputation in a highly competitive specialty food market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions with exact given labels
Milk_Collection = Transition(label='Milk Collection')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Starter_Culture = Transition(label='Starter Culture')
Curd_Formation = Transition(label='Curd Formation')
Cut_Curd = Transition(label='Cut Curd')
Drain_Whey = Transition(label='Drain Whey')
Press_Cheese = Transition(label='Press Cheese')
Salt_Application = Transition(label='Salt Application')
Fermentation = Transition(label='Fermentation')
Rind_Treatment = Transition(label='Rind Treatment')
Aging_Monitor = Transition(label='Aging Monitor')
Quality_Check = Transition(label='Quality Check')
Eco_Packaging = Transition(label='Eco Packaging')
Cold_Storage = Transition(label='Cold Storage')
Order_Processing = Transition(label='Order Processing')
Logistics_Plan = Transition(label='Logistics Plan')
Retail_Delivery = Transition(label='Retail Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

# Define loops for quality assessment section:
# Multiple rounds of quality assessment between Quality Testing and Quality Check with feedback loop
# Represent loop as (* (Quality Testing, Quality Check))
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Testing, Quality_Check])

# Define loop for customer feedback to refine taste and shelf life
# loop on feedback: (* (Order Processing, Customer Feedback))
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Order_Processing, Customer_Feedback])

# Define partial order for cheese production steps:
# Milk Collection --> Milk Pasteurize --> Starter Culture --> Curd Formation
# --> Cut Curd --> Drain Whey --> Press Cheese --> Salt Application --> Fermentation
prod_steps = StrictPartialOrder(nodes=[
    Milk_Collection, Milk_Pasteurize, Starter_Culture, Curd_Formation,
    Cut_Curd, Drain_Whey, Press_Cheese, Salt_Application, Fermentation
])
prod_steps.order.add_edge(Milk_Collection, Milk_Pasteurize)
prod_steps.order.add_edge(Milk_Pasteurize, Starter_Culture)
prod_steps.order.add_edge(Starter_Culture, Curd_Formation)
prod_steps.order.add_edge(Curd_Formation, Cut_Curd)
prod_steps.order.add_edge(Cut_Curd, Drain_Whey)
prod_steps.order.add_edge(Drain_Whey, Press_Cheese)
prod_steps.order.add_edge(Press_Cheese, Salt_Application)
prod_steps.order.add_edge(Salt_Application, Fermentation)

# Define partial order for rind treatment, aging and monitoring:
# Rind Treatment --> Aging Monitor
aging_section = StrictPartialOrder(nodes=[Rind_Treatment, Aging_Monitor])
aging_section.order.add_edge(Rind_Treatment, Aging_Monitor)

# After fermentation comes rind treatment and aging in parallel with quality loop
# We model parallel for aging_section and quality_loop after fermentation
post_fermentation = StrictPartialOrder(nodes=[aging_section, quality_loop])
post_fermentation.order.add_edge(aging_section, quality_loop) # To enforce aging before or in parallel with quality assessment
# Actually, quality_loop is part of quality assessment, which is referencing post fermentation quality checks.
# But process suggests quality testing and quality check more a loop at start or mid production.
# Instead, connect post_fermentation and quality loop concurrently.

# Adjust: fermentation --> aging_section, fermentation --> quality_loop
post_fermentation = StrictPartialOrder(nodes=[aging_section, quality_loop])
post_fermentation.order.add_edge(aging_section, quality_loop)  # to get a partial order between these two? Actually, no direct order stated
# We'll define fermentation as predecessor for both aging_section and quality_loop.
# So we merge fermentation plus after with these two in a PO.

# Define packaging and logistics
packaging_and_logistics = StrictPartialOrder(nodes=[Eco_Packaging, Cold_Storage, Logistics_Plan, Retail_Delivery])
packaging_and_logistics.order.add_edge(Eco_Packaging, Cold_Storage)
packaging_and_logistics.order.add_edge(Cold_Storage, Logistics_Plan)
packaging_and_logistics.order.add_edge(Logistics_Plan, Retail_Delivery)

# Define full process partial order nodes:
# Merge prod_steps, post_fermentation (aging_section, quality_loop), packaging_and_logistics, Order Processing, feedback_loop

# Connect nodes:
# Fermentation --> Rind Treatment & Aging Monitor (aging_section)
# Fermentation --> quality_loop (quality assessment loop)

# Packaging starts after quality checks complete — after Quality_Check in quality_loop

# Order Processing happens after Retail Delivery
# feedback_loop on Order Processing <-> Customer Feedback

# Build top level PO by listing all main components as nodes:
root = StrictPartialOrder(
    nodes=[
        prod_steps,
        aging_section,
        quality_loop,
        packaging_and_logistics,
        Order_Processing,
        feedback_loop
    ]
)

# Define ordering edges:

# From prod_steps' last activity Fermentation to aging_section and quality_loop (start)
root.order.add_edge(prod_steps, aging_section)
root.order.add_edge(prod_steps, quality_loop)

# Quality loop involves Quality Testing and Quality Check internally looping.
# Packaging starts after quality_loop finishes (Quality_Check)
root.order.add_edge(quality_loop, packaging_and_logistics)

# Packaging ends with Retail Delivery, then Order Processing starts
root.order.add_edge(packaging_and_logistics, Order_Processing)

# Feedback loop around Order Processing and Customer Feedback
root.order.add_edge(Order_Processing, feedback_loop)

# The classes require edges between nodes (which must be nodes from root.nodes)
# But we added some arcs with prod_steps, aging_section, etc., which are StrictPartialOrder and OperatorPOWL objects.

# For strict typing, prod_steps is StrictPartialOrder as node, aging_section is StrictPartialOrder as node, quality_loop is OperatorPOWL node, etc.

# No direct edges needed inside these contained partial orders except their internal edges.

# This models the described process with partial concurrency and loops
