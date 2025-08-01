# Generated from: 73fb740b-86a2-4c31-88a6-cab5a351820b.json
# Description: This process outlines the complex supply chain and quality assurance workflow involved in producing and distributing artisanal cheese from small-scale dairy farms to niche gourmet retailers. It includes activities such as sourcing rare milk varieties, managing seasonal fermentation conditions, coordinating with independent aging specialists, conducting sensory evaluations, navigating local food safety regulations, and orchestrating tailored logistics for temperature-controlled deliveries. The process ensures product consistency, maintains traditional craftsmanship standards, and adapts dynamically to fluctuating supply and demand while preserving the unique flavor profiles and heritage of each cheese variety.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Fermentation_Setup = Transition(label='Fermentation Setup')
Temperature_Control = Transition(label='Temperature Control')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Coordination = Transition(label='Aging Coordination')
Sensory_Review = Transition(label='Sensory Review')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Regulation_Check = Transition(label='Regulation Check')
Order_Processing = Transition(label='Order Processing')
Cold_Shipping = Transition(label='Cold Shipping')
Inventory_Audit = Transition(label='Inventory Audit')
Customer_Feedback = Transition(label='Customer Feedback')

# The process outline:
# 1. Milk Sourcing
# 2. Quality Testing
# 3. Fermentation Setup + Temperature Control (parallel)
# 4. Curd Cutting
# 5. Whey Separation
# 6. Molding Cheese + Salting Process (parallel)
# 7. Aging Coordination followed by Sensory Review
# 8. Packaging Design and Label Approval (sequential)
# 9. Regulation Check (choice: check or skip)
# 10. Order Processing, Cold Shipping (sequential)
# 11. Inventory Audit and Customer Feedback (concurrent at end)

# Model step 3 parallel: Fermentation Setup and Temperature Control concurrent
fermentation_parallel = StrictPartialOrder(nodes=[Fermentation_Setup, Temperature_Control])

# Model step 6 parallel: Molding Cheese and Salting Process concurrent
molding_salting_parallel = StrictPartialOrder(nodes=[Molding_Cheese, Salting_Process])

# Step 9 choice: Regulation Check or skip (silent)
skip = SilentTransition()
reg_check_choice = OperatorPOWL(operator=Operator.XOR, children=[Regulation_Check, skip])

# Step 11 concurrent: Inventory Audit and Customer Feedback concurrent
end_parallel = StrictPartialOrder(nodes=[Inventory_Audit, Customer_Feedback])

# Build partial orders progressively

# PO1: Milk Sourcing -> Quality Testing
po1 = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing])
po1.order.add_edge(Milk_Sourcing, Quality_Testing)

# PO2: po1 -> parallel fermentation + temperature control
po2 = StrictPartialOrder(nodes=[po1, fermentation_parallel])
po2.order.add_edge(po1, fermentation_parallel)

# PO3: After fermentation parallel, Curd Cutting
po3 = StrictPartialOrder(nodes=[po2, Curd_Cutting])
po3.order.add_edge(po2, Curd_Cutting)

# PO4: After Curd Cutting, Whey Separation
po4 = StrictPartialOrder(nodes=[po3, Whey_Separation])
po4.order.add_edge(po3, Whey_Separation)

# PO5: After Whey Separation, molding & salting parallel
po5 = StrictPartialOrder(nodes=[po4, molding_salting_parallel])
po5.order.add_edge(po4, molding_salting_parallel)

# PO6: After molding & salting parallel, Aging Coordination -> Sensory Review sequential
aging_sensory = StrictPartialOrder(nodes=[Aging_Coordination, Sensory_Review])
aging_sensory.order.add_edge(Aging_Coordination, Sensory_Review)
po6 = StrictPartialOrder(nodes=[po5, aging_sensory])
po6.order.add_edge(po5, aging_sensory)

# PO7: After sensory review, Packaging Design -> Label Approval
packaging_seq = StrictPartialOrder(nodes=[Packaging_Design, Label_Approval])
packaging_seq.order.add_edge(Packaging_Design, Label_Approval)
po7 = StrictPartialOrder(nodes=[po6, packaging_seq])
po7.order.add_edge(po6, packaging_seq)

# PO8: After packaging, regulation check choice
po8 = StrictPartialOrder(nodes=[po7, reg_check_choice])
po8.order.add_edge(po7, reg_check_choice)

# PO9: After regulation check choice, Order Processing -> Cold Shipping
order_shipping = StrictPartialOrder(nodes=[Order_Processing, Cold_Shipping])
order_shipping.order.add_edge(Order_Processing, Cold_Shipping)
po9 = StrictPartialOrder(nodes=[po8, order_shipping])
po9.order.add_edge(po8, order_shipping)

# PO10: After cold shipping, concurrent Inventory Audit and Customer Feedback
root = StrictPartialOrder(nodes=[po9, end_parallel])
root.order.add_edge(po9, end_parallel)