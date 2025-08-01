# Generated from: e3fbee47-9929-4f35-a2d8-3bf76e9b0d8c.json
# Description: This process details the end-to-end supply chain of artisan cheese production and distribution, involving unique steps such as milk sourcing from rare breed farms, custom fermentation monitoring, seasonal flavor adjustments, and niche market logistics. It integrates quality control with traditional craftsmanship, regulatory compliance, specialty packaging, and targeted retail partnerships. Each activity ensures the preservation of distinct cheese characteristics while optimizing delivery times to specialty shops and gourmet restaurants, balancing small-batch production constraints with demand forecasting and inventory management for limited edition releases.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Farm_Selection = Transition(label='Farm Selection')
Milk_Testing = Transition(label='Milk Testing')
Batch_Pasteurize = Transition(label='Batch Pasteurize')
Culture_Add = Transition(label='Culture Add')
Curd_Cut = Transition(label='Curd Cut')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Form = Transition(label='Press Form')
Salt_Rub = Transition(label='Salt Rub')
Aging_Monitor = Transition(label='Aging Monitor')
Flavor_Adjust = Transition(label='Flavor Adjust')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Order_Processing = Transition(label='Order Processing')
Cold_Storage = Transition(label='Cold Storage')
Delivery_Schedule = Transition(label='Delivery Schedule')
Retail_Setup = Transition(label='Retail Setup')
Feedback_Collect = Transition(label='Feedback Collect')

# Quality control loop: Aging Monitor -> Flavor Adjust (repeated until done)
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Monitor, Flavor_Adjust])

# Packaging and labeling in sequence
packaging_po = StrictPartialOrder(nodes=[Packaging_Design, Label_Approval])
packaging_po.order.add_edge(Packaging_Design, Label_Approval)

# Distribution branch after packaging: Order Processing -> Cold Storage -> Delivery Schedule -> Retail Setup -> Feedback Collect
distribution_po = StrictPartialOrder(
    nodes=[Order_Processing, Cold_Storage, Delivery_Schedule, Retail_Setup, Feedback_Collect]
)
distribution_po.order.add_edge(Order_Processing, Cold_Storage)
distribution_po.order.add_edge(Cold_Storage, Delivery_Schedule)
distribution_po.order.add_edge(Delivery_Schedule, Retail_Setup)
distribution_po.order.add_edge(Retail_Setup, Feedback_Collect)

# Cheese making sequential steps before aging:
# Farm Selection -> Milk Testing -> Batch Pasteurize -> Culture Add -> Curd Cut -> Whey Drain 
# -> Mold Inoculate -> Press Form -> Salt Rub
cheesemaking_po = StrictPartialOrder(
    nodes=[
        Farm_Selection, Milk_Testing, Batch_Pasteurize, Culture_Add,
        Curd_Cut, Whey_Drain, Mold_Inoculate, Press_Form, Salt_Rub
    ]
)
cheesemaking_po.order.add_edge(Farm_Selection, Milk_Testing)
cheesemaking_po.order.add_edge(Milk_Testing, Batch_Pasteurize)
cheesemaking_po.order.add_edge(Batch_Pasteurize, Culture_Add)
cheesemaking_po.order.add_edge(Culture_Add, Curd_Cut)
cheesemaking_po.order.add_edge(Curd_Cut, Whey_Drain)
cheesemaking_po.order.add_edge(Whey_Drain, Mold_Inoculate)
cheesemaking_po.order.add_edge(Mold_Inoculate, Press_Form)
cheesemaking_po.order.add_edge(Press_Form, Salt_Rub)

# Combine cheese making with quality control loop
cheese_and_aging = StrictPartialOrder(
    nodes=[cheesemaking_po, quality_loop]
)
cheese_and_aging.order.add_edge(cheesemaking_po, quality_loop)

# Combine with packaging sequence after aging loop
process_until_packaging = StrictPartialOrder(
    nodes=[cheese_and_aging, packaging_po]
)
process_until_packaging.order.add_edge(cheese_and_aging, packaging_po)

# Combine whole process with distribution sequence after packaging
root = StrictPartialOrder(
    nodes=[process_until_packaging, distribution_po]
)
root.order.add_edge(process_until_packaging, distribution_po)