# Generated from: 59108579-dac3-4143-9163-78fb2bb792ff.json
# Description: This process outlines the end-to-end operations involved in producing and distributing artisan cheese from small dairy farms to niche retail shops. It includes raw milk sourcing, quality checks under varying seasonal conditions, traditional cheese culturing, aging in controlled environments, custom packaging, and logistics coordination with temperature-sensitive transport. It also incorporates periodic artisan workshops for skill improvement, market trend analysis for new cheese varieties, and direct customer feedback loops to adjust production. The process balances artisanal craftsmanship with traceability and regulatory compliance across multiple regions, ensuring product authenticity and superior taste consistency in a competitive specialty food market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Check = Transition(label='Quality Check')
Culture_Prep = Transition(label='Culture Prep')
Curd_Formation = Transition(label='Curd Formation')
Cutting_Curd = Transition(label='Cutting Curd')
Molding_Cheese = Transition(label='Molding Cheese')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Stage = Transition(label='Salting Stage')
Aging_Control = Transition(label='Aging Control')
Packaging_Art = Transition(label='Packaging Art')
Label_Design = Transition(label='Label Design')
Storage_Audit = Transition(label='Storage Audit')
Market_Survey = Transition(label='Market Survey')
Workshop_Host = Transition(label='Workshop Host')
Order_Processing = Transition(label='Order Processing')
Temp_Logistics = Transition(label='Temp Logistics')
Customer_Review = Transition(label='Customer Review')

# Model periodic artisan workshops and market survey + customer review as concurrent background activities
# They run concurrently alongside packaging/auditing/logistics.

# Looping in Customer Feedback loop:
# After Order Processing and Temp Logistics, Customer Review happens,
# which leads to adjustments (Workshop_Host and Market_Survey)
# which in turn influence production again.
# We'll model loop as: (Order Processing + Temp Logistics) -> loop(Workshop_Host, Market_Survey) then back.

# The core cheese making sequence is mostly sequential with Aging_Control, Packaging, Labeling, Storage Audit

# Partial order modeling the main production sequence:
nodes_main = [
    Milk_Sourcing,
    Quality_Check,
    Culture_Prep,
    Curd_Formation,
    Cutting_Curd,
    Molding_Cheese,
    Pressing_Cheese,
    Salting_Stage,
    Aging_Control,
    Packaging_Art,
    Label_Design,
    Storage_Audit,
    Order_Processing,
    Temp_Logistics,
    Customer_Review,
]

# Order for the main production chain before customer feedback:
root = StrictPartialOrder(nodes=nodes_main)

root.order.add_edge(Milk_Sourcing, Quality_Check)
root.order.add_edge(Quality_Check, Culture_Prep)
root.order.add_edge(Culture_Prep, Curd_Formation)
root.order.add_edge(Curd_Formation, Cutting_Curd)
root.order.add_edge(Cutting_Curd, Molding_Cheese)
root.order.add_edge(Molding_Cheese, Pressing_Cheese)
root.order.add_edge(Pressing_Cheese, Salting_Stage)
root.order.add_edge(Salting_Stage, Aging_Control)

# Packaging Art, Label Design and Storage Audit can run in partial order (some concurrency):
root.order.add_edge(Aging_Control, Packaging_Art)
root.order.add_edge(Packaging_Art, Label_Design)
root.order.add_edge(Label_Design, Storage_Audit)

root.order.add_edge(Storage_Audit, Order_Processing)
root.order.add_edge(Order_Processing, Temp_Logistics)
root.order.add_edge(Temp_Logistics, Customer_Review)

# Model the loop for workshops and market survey (as skill improvement and market trend analysis)
# Workshop and Market survey influence production again, so we'll model a loop after customer review
loop_child_A = OperatorPOWL(operator=Operator.XOR, children=[Workshop_Host, Market_Survey])
loop = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Review, loop_child_A])

# Now, replace just Customer_Review node with the loop to reflect feedback loop
# For that, we create a new StrictPartialOrder with everything up to temp logistics, then loop

nodes_before_loop = [
    Milk_Sourcing,
    Quality_Check,
    Culture_Prep,
    Curd_Formation,
    Cutting_Curd,
    Molding_Cheese,
    Pressing_Cheese,
    Salting_Stage,
    Aging_Control,
    Packaging_Art,
    Label_Design,
    Storage_Audit,
    Order_Processing,
    Temp_Logistics
]

root = StrictPartialOrder(nodes=nodes_before_loop + [loop])

# Rebuild order edges:
root.order.add_edge(Milk_Sourcing, Quality_Check)
root.order.add_edge(Quality_Check, Culture_Prep)
root.order.add_edge(Culture_Prep, Curd_Formation)
root.order.add_edge(Curd_Formation, Cutting_Curd)
root.order.add_edge(Cutting_Curd, Molding_Cheese)
root.order.add_edge(Molding_Cheese, Pressing_Cheese)
root.order.add_edge(Pressing_Cheese, Salting_Stage)
root.order.add_edge(Salting_Stage, Aging_Control)

root.order.add_edge(Aging_Control, Packaging_Art)
root.order.add_edge(Packaging_Art, Label_Design)
root.order.add_edge(Label_Design, Storage_Audit)

root.order.add_edge(Storage_Audit, Order_Processing)
root.order.add_edge(Order_Processing, Temp_Logistics)
root.order.add_edge(Temp_Logistics, loop)