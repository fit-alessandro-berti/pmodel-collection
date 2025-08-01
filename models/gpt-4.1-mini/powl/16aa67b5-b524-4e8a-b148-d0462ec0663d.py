# Generated from: 16aa67b5-b524-4e8a-b148-d0462ec0663d.json
# Description: This process describes the end-to-end supply chain of artisanal cheese production and distribution involving unique steps such as milk sourcing from rare breeds, precise aging conditions monitoring, custom flavor profiling, and direct-to-consumer sales through curated events. It includes managing small batch fermentation, quality control using sensory panels, packaging with sustainable materials, and coordinating with niche retailers globally. The complexity arises from balancing traditional craftsmanship with modern logistics and traceability requirements, ensuring each cheese wheel maintains its distinctive character while meeting regulatory standards and consumer expectations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for activities
Breed_Selection = Transition(label='Breed Selection')
Milk_Harvest = Transition(label='Milk Harvest')
Quality_Check = Transition(label='Quality Check')
Starter_Prep = Transition(label='Starter Prep')
Curd_Cutting = Transition(label='Curd Cutting')
Molding_Press = Transition(label='Molding Press')
Salt_Brining = Transition(label='Salt Brining')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Flavor_Test = Transition(label='Flavor Test')
Batch_Labeling = Transition(label='Batch Labeling')
Eco_Packaging = Transition(label='Eco Packaging')
Event_Planning = Transition(label='Event Planning')
Retail_Outreach = Transition(label='Retail Outreach')
Order_Fulfill = Transition(label='Order Fulfill')
Feedback_Loop = Transition(label='Feedback Loop')
Inventory_Audit = Transition(label='Inventory Audit')

# Construct the milk sourcing and preparation partial order
milk_preparation = StrictPartialOrder(
    nodes=[Breed_Selection, Milk_Harvest, Quality_Check, Starter_Prep, Curd_Cutting, Molding_Press, Salt_Brining],
)
milk_preparation.order.add_edge(Breed_Selection, Milk_Harvest)
milk_preparation.order.add_edge(Milk_Harvest, Quality_Check)
milk_preparation.order.add_edge(Quality_Check, Starter_Prep)
milk_preparation.order.add_edge(Starter_Prep, Curd_Cutting)
milk_preparation.order.add_edge(Curd_Cutting, Molding_Press)
milk_preparation.order.add_edge(Molding_Press, Salt_Brining)

# Aging setup branch with monitoring humidity and flavor testing in parallel after setup
aging_setup = StrictPartialOrder(
    nodes=[Aging_Setup, Humidity_Control, Flavor_Test],
)
aging_setup.order.add_edge(Aging_Setup, Humidity_Control)
aging_setup.order.add_edge(Aging_Setup, Flavor_Test)

# Packaging and labeling
packaging = StrictPartialOrder(
    nodes=[Batch_Labeling, Eco_Packaging],
)
packaging.order.add_edge(Batch_Labeling, Eco_Packaging)

# Sales & distribution partial order with event planning and retail outreach concurrent
sales_distribution = StrictPartialOrder(
    nodes=[Event_Planning, Retail_Outreach, Order_Fulfill],
)
# No order edges here, so concurrency between Event_Planning, Retail_Outreach and Order_Fulfill

# Quality feedback loop (loop activity)
# Loop: execute Feedback_Loop, then Inventory_Audit and back to Feedback_Loop or exit
feedback_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Feedback_Loop, Inventory_Audit]
)

# Top-level partial order combining all major parts
root = StrictPartialOrder(
    nodes=[
        milk_preparation,
        aging_setup,
        packaging,
        sales_distribution,
        feedback_cycle
    ]
)

# Define control flow edges between main phases
root.order.add_edge(milk_preparation, aging_setup)
root.order.add_edge(aging_setup, packaging)
root.order.add_edge(packaging, sales_distribution)
root.order.add_edge(sales_distribution, feedback_cycle)