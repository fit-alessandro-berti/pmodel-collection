# Generated from: 8cf01db4-b1eb-47cb-9fbe-fa99d06fa21d.json
# Description: This process manages the intricate supply chain of artisan cheese production, starting from raw milk sourcing from local farms to aging in specialized cellars. It involves quality testing, custom flavor blending, packaging in eco-friendly materials, coordinating seasonal demand fluctuations, compliance with food safety regulations, and direct-to-consumer delivery logistics. Each step ensures traceability and maintains product authenticity while optimizing for shelf life and market responsiveness. The process also incorporates feedback loops from retailers and consumers to refine production batches and flavor profiles, balancing artisanal craftsmanship with efficient distribution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Batch_Blending = Transition(label='Batch Blending')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Aging_Control = Transition(label='Aging Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Prep = Transition(label='Packaging Prep')
Eco_Packaging = Transition(label='Eco Packaging')
Label_Printing = Transition(label='Label Printing')
Inventory_Audit = Transition(label='Inventory Audit')
Regulatory_Check = Transition(label='Regulatory Check')
Order_Processing = Transition(label='Order Processing')
Shipping_Setup = Transition(label='Shipping Setup')
Customer_Feedback = Transition(label='Customer Feedback')
Demand_Forecast = Transition(label='Demand Forecast')
Batch_Refinement = Transition(label='Batch Refinement')

# Silent transition for loop exits and concurrency handling
skip = SilentTransition()

# Loop for Demand Forecast and Batch Refinement incorporating feedback from retailers and consumers
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Demand_Forecast, Batch_Refinement])

# Partial order for Packaging steps: Packaging Prep -> Eco Packaging and Label Printing concurrent after Eco Packaging
packaging_po = StrictPartialOrder(nodes=[Packaging_Prep, Eco_Packaging, Label_Printing])
packaging_po.order.add_edge(Packaging_Prep, Eco_Packaging)
packaging_po.order.add_edge(Eco_Packaging, Label_Printing)

# Quality and regulatory compliance check combined as partial order (Inventory Audit and Regulatory Check can happen concurrently after Packaging)
compliance_po = StrictPartialOrder(nodes=[Inventory_Audit, Regulatory_Check])
# no order between Inventory Audit and Regulatory Check => concurrent

# Shipping setup and order processing as partial order (Order Processing-> Shipping Setup)
shipping_po = StrictPartialOrder(nodes=[Order_Processing, Shipping_Setup])
shipping_po.order.add_edge(Order_Processing, Shipping_Setup)

# Customer feedback is after shipping, feeding into feedback loop

# Main production sequence partial order before packaging:
# Milk Sourcing -> Quality Testing -> Batch Blending -> Curd Formation -> Pressing Cheese -> Aging Control -> Flavor Profiling -> Packaging Prep
production_po = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Quality_Testing,
    Batch_Blending,
    Curd_Formation,
    Pressing_Cheese,
    Aging_Control,
    Flavor_Profiling,
    packaging_po  # packaging_po is a node here
])

# Add ordering edges for main production
production_po.order.add_edge(Milk_Sourcing, Quality_Testing)
production_po.order.add_edge(Quality_Testing, Batch_Blending)
production_po.order.add_edge(Batch_Blending, Curd_Formation)
production_po.order.add_edge(Curd_Formation, Pressing_Cheese)
production_po.order.add_edge(Pressing_Cheese, Aging_Control)
production_po.order.add_edge(Aging_Control, Flavor_Profiling)
production_po.order.add_edge(Flavor_Profiling, packaging_po)

# Combine shipping and compliance with production
# Packaging then compliance and shipping in parallel (concurrent)
# Create partial order with production_po, compliance_po, shipping_po, Customer Feedback, feedback_loop
# Edges:
# packaging_po --> compliance_po (Inventory Audit & Regulatory Check)
# packaging_po --> shipping_po (Order Processing start)
# shipping_po --> Customer_Feedback
# Customer_Feedback --> feedback_loop

root = StrictPartialOrder(nodes=[
    production_po,
    compliance_po,
    shipping_po,
    Customer_Feedback,
    feedback_loop
])
# Add edges to root partial order
# Packaging end triggers compliance and shipping
root.order.add_edge(production_po, compliance_po)
root.order.add_edge(production_po, shipping_po)
# shipping_po leads to customer feedback
root.order.add_edge(shipping_po, Customer_Feedback)
# customer feedback leads to feedback loop (demand forecasting and batch refinement)
root.order.add_edge(Customer_Feedback, feedback_loop)