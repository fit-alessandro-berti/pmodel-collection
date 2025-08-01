# Generated from: b82a6146-51df-4ccf-8610-6c48eba74d96.json
# Description: This process involves the sourcing, crafting, and distribution of small-batch artisan cheeses with an emphasis on traditional methods and quality control. Starting from selecting rare milk varieties, the process includes multiple fermentation stages, aging in controlled environments, and detailed sensory evaluations. Packaging is customized for different markets, followed by a logistics phase targeting niche retailers and direct consumer deliveries. Throughout, traceability and sustainability metrics are continuously monitored to ensure product integrity and minimal environmental impact, making this supply chain complex yet highly specialized and adaptive to market preferences.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Prep = Transition(label='Starter Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Press_Molding = Transition(label='Press Molding')
Salt_Application = Transition(label='Salt Application')
Fermentation_Stage = Transition(label='Fermentation Stage')
Aging_Control = Transition(label='Aging Control')
Sensory_Review = Transition(label='Sensory Review')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Order_Processing = Transition(label='Order Processing')
Distribution_Plan = Transition(label='Distribution Plan')
Sustainability_Audit = Transition(label='Sustainability Audit')
Customer_Feedback = Transition(label='Customer Feedback')

# Partial order for initial sourcing and prep stages
prep_po = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Starter_Prep])
prep_po.order.add_edge(Milk_Sourcing, Quality_Testing)
prep_po.order.add_edge(Quality_Testing, Starter_Prep)

# Partial order for milk processing
milk_processing_po = StrictPartialOrder(nodes=[Milk_Pasteurize, Curd_Cutting, Whey_Draining, Press_Molding, Salt_Application])
milk_processing_po.order.add_edge(Milk_Pasteurize, Curd_Cutting)
milk_processing_po.order.add_edge(Curd_Cutting, Whey_Draining)
milk_processing_po.order.add_edge(Whey_Draining, Press_Molding)
milk_processing_po.order.add_edge(Press_Molding, Salt_Application)

# Partial order for fermentation, aging and review
fermentation_po = StrictPartialOrder(nodes=[Fermentation_Stage, Aging_Control, Sensory_Review])
fermentation_po.order.add_edge(Fermentation_Stage, Aging_Control)
fermentation_po.order.add_edge(Aging_Control, Sensory_Review)

# Partial order for packaging
packaging_po = StrictPartialOrder(nodes=[Packaging_Design, Label_Printing])
packaging_po.order.add_edge(Packaging_Design, Label_Printing)

# Partial order for order handling and distribution
distribution_po = StrictPartialOrder(nodes=[Order_Processing, Distribution_Plan])
distribution_po.order.add_edge(Order_Processing, Distribution_Plan)

# Sustainability audit runs concurrently with distribution and customer feedback follows distribution plan
sustainability_po = StrictPartialOrder(nodes=[Distribution_Plan, Sustainability_Audit, Customer_Feedback])
sustainability_po.order.add_edge(Distribution_Plan, Customer_Feedback)

# Combine packaging and distribution related partial orders with sustainability
post_prod_po = StrictPartialOrder(nodes=[packaging_po, distribution_po, Sustainability_Audit, Customer_Feedback])
post_prod_po.order.add_edge(packaging_po, distribution_po)
post_prod_po.order.add_edge(distribution_po, Sustainability_Audit)
post_prod_po.order.add_edge(Sustainability_Audit, Customer_Feedback)

# Compose the full process partial order
root = StrictPartialOrder(nodes=[
    prep_po,
    milk_processing_po,
    fermentation_po,
    post_prod_po
])

# Define ordering between major phases
root.order.add_edge(prep_po, milk_processing_po)
root.order.add_edge(milk_processing_po, fermentation_po)
root.order.add_edge(fermentation_po, post_prod_po)