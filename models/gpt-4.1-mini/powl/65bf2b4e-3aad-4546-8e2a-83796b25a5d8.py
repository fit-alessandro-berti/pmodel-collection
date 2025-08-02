# Generated from: 65bf2b4e-3aad-4546-8e2a-83796b25a5d8.json
# Description: This process outlines the end-to-end supply chain for artisan cheese production, emphasizing small-batch quality and traceability. It begins with raw milk sourcing from local farms, followed by milk quality testing and fermentation control. The cheese is then manually curdled, molded, and aged under specific conditions. Each batch undergoes sensory evaluation and packaging with detailed provenance labels. Distribution involves coordinating with niche retailers and specialty food markets. The process includes customer feedback loops to adjust recipes and maintain artisanal standards while ensuring regulatory compliance and seasonal ingredient management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Fermentation_Check = Transition(label='Fermentation Check')
Curd_Formation = Transition(label='Curd Formation')
Molding_Cheese = Transition(label='Molding Cheese')
Aging_Control = Transition(label='Aging Control')
Sensory_Eval = Transition(label='Sensory Eval')
Batch_Packaging = Transition(label='Batch Packaging')
Label_Printing = Transition(label='Label Printing')
Inventory_Logging = Transition(label='Inventory Logging')
Retail_Coordination = Transition(label='Retail Coordination')
Transport_Scheduling = Transition(label='Transport Scheduling')
Customer_Survey = Transition(label='Customer Survey')
Recipe_Adjust = Transition(label='Recipe Adjust')
Compliance_Audit = Transition(label='Compliance Audit')
Seasonal_Sourcing = Transition(label='Seasonal Sourcing')

# Build the main production sequence PO:
# Milk Sourcing --> Quality Testing --> Fermentation Check --> Curd Formation --> Molding Cheese --> Aging Control
production_seq = StrictPartialOrder(nodes=[
    Milk_Sourcing, Quality_Testing, Fermentation_Check, Curd_Formation, Molding_Cheese, Aging_Control
])
production_seq.order.add_edge(Milk_Sourcing, Quality_Testing)
production_seq.order.add_edge(Quality_Testing, Fermentation_Check)
production_seq.order.add_edge(Fermentation_Check, Curd_Formation)
production_seq.order.add_edge(Curd_Formation, Molding_Cheese)
production_seq.order.add_edge(Molding_Cheese, Aging_Control)

# Sensory Evaluation and Packaging:
# Sensory Eval -> Batch Packaging -> Label Printing -> Inventory Logging
sensory_packaging_seq = StrictPartialOrder(nodes=[
    Sensory_Eval, Batch_Packaging, Label_Printing, Inventory_Logging
])
sensory_packaging_seq.order.add_edge(Sensory_Eval, Batch_Packaging)
sensory_packaging_seq.order.add_edge(Batch_Packaging, Label_Printing)
sensory_packaging_seq.order.add_edge(Label_Printing, Inventory_Logging)

# Distribution coordination: Retail Coordination --> Transport Scheduling
distribution_seq = StrictPartialOrder(nodes=[
    Retail_Coordination, Transport_Scheduling
])
distribution_seq.order.add_edge(Retail_Coordination, Transport_Scheduling)

# Compliance Audit and Seasonal Sourcing can be done concurrently with distribution
distribution_and_compliance = StrictPartialOrder(nodes=[
    distribution_seq, Compliance_Audit, Seasonal_Sourcing
])
# Compliance Audit and Seasonal Sourcing are concurrent with distribution nodes (no added edges)

# Define the loop: Customer Feedback Loop
# Loop: (Customer Survey, Recipe Adjust)
# loop = *(Customer Survey, Recipe Adjust)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Survey, Recipe_Adjust])

# Combine production chain with feedback loop after Aging Control
prod_with_feedback = StrictPartialOrder(nodes=[production_seq, feedback_loop])
prod_with_feedback.order.add_edge(production_seq, feedback_loop)

# Branch: After feedback loop, join Sensory Eval
prod_feedback_sensory = StrictPartialOrder(nodes=[prod_with_feedback, sensory_packaging_seq])
prod_feedback_sensory.order.add_edge(prod_with_feedback, sensory_packaging_seq)

# Then after packaging & logging, distribution & compliance concurrently
full_process = StrictPartialOrder(nodes=[prod_feedback_sensory, distribution_and_compliance])
full_process.order.add_edge(prod_feedback_sensory, distribution_and_compliance)

root = full_process