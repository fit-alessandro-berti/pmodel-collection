# Generated from: 88399049-9771-46c9-85fb-f07a1dc31720.json
# Description: This process involves the intricate creation of bespoke artisan perfumes, starting from sourcing rare natural ingredients globally to blending unique scent profiles tailored for individual clients. It includes rigorous quality testing, aging phases, and custom packaging design. The process requires coordination between botanists, chemists, and designers to ensure a harmonious final product that meets personalized fragrance desires while maintaining sustainable and ethical standards throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Ingredient_Sourcing = Transition(label='Ingredient Sourcing')
Sample_Testing = Transition(label='Sample Testing')
Client_Interview = Transition(label='Client Interview')
Scent_Blending = Transition(label='Scent Blending')
Stability_Check = Transition(label='Stability Check')
Aging_Monitor = Transition(label='Aging Monitor')
Quality_Review = Transition(label='Quality Review')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Client_Approval = Transition(label='Client Approval')
Batch_Mixing = Transition(label='Batch Mixing')
Compliance_Audit = Transition(label='Compliance Audit')
Order_Fulfillment = Transition(label='Order Fulfillment')
Shipping_Arrange = Transition(label='Shipping Arrange')
Feedback_Collection = Transition(label='Feedback Collection')
Inventory_Update = Transition(label='Inventory Update')

# Loop for iterative Aging phases: Aging_Monitor and Stability_Check repeated until stable quality
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Monitor, Stability_Check])

# Partial order for the initial preparation and testing steps
prep_testing = StrictPartialOrder(
    nodes=[Ingredient_Sourcing, Sample_Testing, Client_Interview, Scent_Blending, Batch_Mixing]
)
prep_testing.order.add_edge(Ingredient_Sourcing, Sample_Testing)
prep_testing.order.add_edge(Sample_Testing, Client_Interview)
prep_testing.order.add_edge(Client_Interview, Scent_Blending)
prep_testing.order.add_edge(Scent_Blending, Batch_Mixing)

# Partial order for Quality Review and Compliance Audit, after aging loop
quality_compliance = StrictPartialOrder(
    nodes=[Quality_Review, Compliance_Audit]
)
quality_compliance.order.add_edge(Quality_Review, Compliance_Audit)

# Partial order for packaging steps
packaging = StrictPartialOrder(
    nodes=[Packaging_Design, Label_Printing]
)
packaging.order.add_edge(Packaging_Design, Label_Printing)

# Partial order for finalization and feedback steps
finalization = StrictPartialOrder(
    nodes=[Client_Approval, Order_Fulfillment, Shipping_Arrange, Feedback_Collection, Inventory_Update]
)
finalization.order.add_edge(Client_Approval, Order_Fulfillment)
finalization.order.add_edge(Order_Fulfillment, Shipping_Arrange)
finalization.order.add_edge(Shipping_Arrange, Feedback_Collection)
finalization.order.add_edge(Feedback_Collection, Inventory_Update)

# Construct the main workflow PO combining all parts
root = StrictPartialOrder(
    nodes=[prep_testing, aging_loop, quality_compliance, packaging, finalization]
)

# Define the partial order edges connecting these phases
root.order.add_edge(prep_testing, aging_loop)
root.order.add_edge(aging_loop, quality_compliance)
root.order.add_edge(quality_compliance, packaging)
root.order.add_edge(packaging, finalization)