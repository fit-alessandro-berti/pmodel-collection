# Generated from: 760dc89e-da5b-4370-b399-aac0443faa09.json
# Description: This process outlines the intricate steps involved in the production and distribution of artisan cheese, from sourcing rare milk varieties to aging and quality testing. It includes delicate decisions on fermentation duration, packaging with sustainable materials, coordinating with niche retailers, and managing seasonal demand fluctuations. The process also ensures compliance with regional food safety standards while incorporating customer feedback loops to refine flavor profiles and enhance brand reputation. Logistics coordination involves cold chain management, customs clearance for international shipments, and contingency planning for supply disruptions caused by environmental factors or animal health issues. Marketing efforts focus on storytelling and provenance verification to attract discerning consumers and maintain premium pricing strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Coagulation_Step = Transition(label='Coagulation Step')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Molding_Cheese = Transition(label='Molding Cheese')
Pressing_Block = Transition(label='Pressing Block')
Salting_Process = Transition(label='Salting Process')
Aging_Monitor = Transition(label='Aging Monitor')
Flavor_Tasting = Transition(label='Flavor Tasting')
Packaging_Prep = Transition(label='Packaging Prep')
Sustainability_Check = Transition(label='Sustainability Check')
Order_Coordination = Transition(label='Order Coordination')
Cold_Storage = Transition(label='Cold Storage')
Customs_Clearance = Transition(label='Customs Clearance')
Retail_Delivery = Transition(label='Retail Delivery')
Customer_Feedback = Transition(label='Customer Feedback')
Market_Analysis = Transition(label='Market Analysis')

skip = SilentTransition()

# Loop for fermentation duration and quality control:
# LOOP(body=Aging_Monitor, redo=Flavor_Tasting)
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Monitor, Flavor_Tasting])

# Packaging choice: either package with Sustainability Check or skip it
packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[Packaging_Prep, Sustainability_Check])

# Logistics partial order:
# Customs Clearance --> Cold Storage --> Retail Delivery
logistics_po = StrictPartialOrder(nodes=[Customs_Clearance, Cold_Storage, Retail_Delivery])
logistics_po.order.add_edge(Customs_Clearance, Cold_Storage)
logistics_po.order.add_edge(Cold_Storage, Retail_Delivery)

# Customer feedback loop with market analysis:
# LOOP(body=Customer_Feedback, redo=Market_Analysis)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Feedback, Market_Analysis])

# Cheese production steps partial order (sequential):
# Milk Sourcing --> Quality Testing --> Culture Selection --> Milk Pasteurize --> Coagulation Step -->
# Curd Cutting --> Whey Drain --> Molding Cheese --> Pressing Block --> Salting Process
production_po = StrictPartialOrder(
    nodes=[Milk_Sourcing, Quality_Testing, Culture_Selection, Milk_Pasteurize, Coagulation_Step,
           Curd_Cutting, Whey_Drain, Molding_Cheese, Pressing_Block, Salting_Process]
)
production_po.order.add_edge(Milk_Sourcing, Quality_Testing)
production_po.order.add_edge(Quality_Testing, Culture_Selection)
production_po.order.add_edge(Culture_Selection, Milk_Pasteurize)
production_po.order.add_edge(Milk_Pasteurize, Coagulation_Step)
production_po.order.add_edge(Coagulation_Step, Curd_Cutting)
production_po.order.add_edge(Curd_Cutting, Whey_Drain)
production_po.order.add_edge(Whey_Drain, Molding_Cheese)
production_po.order.add_edge(Molding_Cheese, Pressing_Block)
production_po.order.add_edge(Pressing_Block, Salting_Process)

# After Salting_Process proceed to fermentation loop and quality testing (Quality Testing can be after Milk Sourcing only)
# But the description suggests quality testing at start; assume also at end before packaging

# Connect production_po and fermentation_loop and packaging_choice in partial order
production_and_fermentation_po = StrictPartialOrder(
    nodes=[production_po, fermentation_loop, packaging_choice]
)
production_and_fermentation_po.order.add_edge(production_po, fermentation_loop)
production_and_fermentation_po.order.add_edge(fermentation_loop, packaging_choice)

# Order coordination before logistics and after packaging prep and sustainability check
order_and_logistics_po = StrictPartialOrder(
    nodes=[packaging_choice, Order_Coordination, logistics_po]
)
order_and_logistics_po.order.add_edge(packaging_choice, Order_Coordination)
order_and_logistics_po.order.add_edge(Order_Coordination, logistics_po)

# The overall root partial order: production_and_fermentation_po --> order_and_logistics_po
# Also incorporate feedback loop concurrent to Order Coordination and logistics (can happen continuously)
root = StrictPartialOrder(
    nodes=[production_and_fermentation_po, order_and_logistics_po, feedback_loop]
)
root.order.add_edge(production_and_fermentation_po, order_and_logistics_po)

# No edges added from/to feedback_loop to express concurrency

# Incorporate initial Quality Testing after Milk Sourcing before Culture Selection
# To do this, adjust production_po edges: 
# Milk_Sourcing->Quality_Testing->Culture_Selection
# This is already done.

# Final model held in variable 'root'